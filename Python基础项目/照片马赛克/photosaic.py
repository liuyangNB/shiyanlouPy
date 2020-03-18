import argparse
import os

import numpy as np
from PIL import Image

def getImages(imageDir):
    """
    从给定的目录里加载所有的替换图像
    :param imageDir: 目录路径
    :return: 替换图像路径list[Image]
    """

    files = os.listdir(imageDir)
    images = []

    for file in files:
        #get absolute pathroot
        filePath = os.path.abspath(os.path.join(imageDir,file))

        try:
            fp = open(filePath,"rb")
            im = Image.open(fp)#Image.open() 确定了图像，但它实际上没有读取全部图像数据，直到使用该图像时才会那么做。
            images.append(im)

            #确定了图像信息，但没用加载全部图像数据，用到时候才会下载
            im.load()
            fp.close()
        except:
            print("这个图片识别出错：%s",filePath)

    return images

def getAverageRGB(img):
    """
    计算图像的平均RGB值,整个图像的平均RGB
    将图像包含的每个像素点的RGB值累加再除以像素点，得到平均值
    :param image: PIL Image对象
    :return: 平均RGB值
    """

    #计算像素点数
    npixels = img.size[0]*img.size[1]

    #获取每种颜色及其计数： [(c1, (r1, g1, b1)), (c2, (r2, g2, b2)), ...]
    cols = img.getcolors(npixels)

    #每种颜色的rgb值的各自总和
    sumRGB = [(x[0]*x[1][0], x[0]*x[1][1], x[0]*x[1][2]) for x in cols]

    avg = tuple([(int(sum(x)/npixels)) for x in zip(*sumRGB)])#要知道 zip(*[(r,g,b)(r,g,b)...])的涵义

    return avg

def splitImage(image,size):
    """
    将图像按网格分割成多个小图片
    :param image: PIL Image对象
    :param size: 网格的行数列数
    :return: 小图像列表
    """
    W, H = image.size[0],image.size[1]#原始图像的宽高
    row, col = size
    k_w, k_h = int(W/col), int(H/row)#小图的宽高

    imgs = []

    #先按行再按列裁剪出
    for i in range(row):
        for j in range(col):
            imgs.append(image.crop((j*k_w,i*k_h,(j+1)*k_w,(i+1)*k_h)))#把(x0,y0,x1,y1)的图像复制

    return imgs#大图像变成小图片了

def getBestMatchIndex(input_avg, avgs):
    """
    找出颜色最近的索引

    :param input_avg: {Tuple[int,int,int]} input_avg 目标颜色值
    :param avgs:  {List[Tuple[int,int,int]]} avgs 要搜索的颜色值列表
    :return:
    """
    index = 0
    min_index = 0
    min_distance = float('inf')

    for val in avgs:

        dist = (val[0]-input_avg[0])^2+(val[1]-input_avg[1])^2+(val[1]-input_avg[1])^2

        if dist < min_distance:
            min_distance = dist
            min_index = index

        index += 1

    return min_index

def creatImageGrid(images, dims):
    """
    将图像列表中的小图像按先后顺序拼接为一个大图像

    :param images: list[Image] 小图像列表
    :param dims: Tuple[int,int] 大图像的行数和列数,也对应小图像的坐标
    :return: 拼接得到的大图像
    """

    row, col = dims

    #确保小图像个数得到满足
    assert row*col == len(images)

    #计算所有小图像的最大宽度和高度
    width= max(img.size[0] for img in images)
    height = max(img.size[1] for img in images)

    #创建大图像对象
    grid_img = Image.new('RGB',(col*width,row*height))

    #依次将每个小图贴到大图
    for index in range(len(images)):
        row_ind = int(index/col)
        col_ind = index - row_ind*col#不是row_ind-1是因为从0开始计数的

        grid_img.paste(images[index], (col_ind*width,row_ind*height))

    return grid_img

def creatPhotoMosaic(target_image, input_imges,grid_size,reuse_images = True):
    """
    图片马赛克生成

    :param target_image: {Image} 目标图像
    :param input_imges: {List[Image]} 替换图像列表
    :param grid_size:   {Tuple[int,int]} 网格行数列数
    :param reuse_images: 是否允许重复使用替换图像
    :return: 马赛克图像
    """
    print("将目标图像切割成小图像。。。")
    target_images = splitImage(target_image,grid_size)


    print("为每个网格小图像在替换图像列表中找到颜色最接近的图像。。。")
    output_images = []
    count = 0
    #分10组进行，每组打印完成后打印进度信息
    batch_size = int(len(target_images)/10)

    #计数替换图像列表里每个小图像的颜色平均值
    avgs = []
    for img in input_imges:
        avg = getAverageRGB(img)
        avgs.append(avg)

    #对灭个网格小图，从替换列表中找到颜色最相近的那个，并添加到输出小图列表
    for img in target_images:
        avg = getAverageRGB(img)

        match_ind = getBestMatchIndex(avg,avgs)

        output_images.append(input_imges[match_ind])

        #打印进度
        if count > 0 and batch_size>10 and count%batch_size == 0:
            print("进度进行了%d",count)
        count+=1

        #如果不允许重用替换图像，用过的图像就丢掉
        if not reuse_images:
            input_imges.remove(match_ind)

    print("创建好马赛克")
    mosaic_image= creatImageGrid(output_images,grid_size)
    return mosaic_image


def main():
    # 定义程序接收的命令行参数
    parser = argparse.ArgumentParser(
        description='Creates a photomosaic from input images')
    parser.add_argument('--target-image', dest='target_image', required=True)
    parser.add_argument('--input-folder', dest='input_folder', required=True)
    parser.add_argument('--grid-size', nargs=2,
                        dest='grid_size', required=True)
    parser.add_argument('--output-file', dest='outfile', required=False)

    # 解析命令行参数
    args = parser.parse_args()

    grid_size = (int(args.grid_size[0]),int(args.grid_size[1]))
    out_filename = "mosaic.jpg"

    if args.outfile:
        out_filename = args.outfile


    #打开目标图片
    print("正在读目标图。。。")
    target_image = Image.open(args.target_image)

    #从指定文件夹下加载所有替换图像
    input_images = getImages(args.input_folder)
    #print("------------------替代图片的数量%d",int(len(input_images)))

    #如果替换图像为空就退出
    if input_images == []:
        print("没用发现这个目录下的图像")
        exit()

    # 将所有替换图像缩放到指定的网格大小
    print('resizing images...')
    dims = (int(target_image.size[0] / grid_size[1]),
            int(target_image.size[1] / grid_size[0]))
    for img in input_images:
        img.thumbnail(dims)
    #print("------------------", len(input_images))
    # 生成马赛克图像
    print('starting photomosaic creation...')
    mosaic_image = creatPhotoMosaic(target_image, input_images, grid_size)

    # 保存马赛克图像
    mosaic_image.save(out_filename, 'PNG')
    print("saved output to %s" % (out_filename,))

    print('done.')

if __name__ == '__main__':
    main()

