
"""
    ###     ####         ######
          ###  ###      #    ###
    ###         ###       ######
    ###      ####       ###   ##
    ###    ####        ###    ##
    ###   ##########    ##### ###

i2a creates ASCII art from images right on your terminal.

Usage: i2a [options] [FILE]

Options:
  -h --help            Show this on screen.
  -v --version         Show version.
  -c --colors          Show colored output.
  -b --bold            Output bold characters
  --contrast=<factor>  Manually set contrast [default: 1.5].
  --alt-chars          Use an alternate set of characters.

"""

import subprocess
from colors import *
from PIL import Image, ImageEnhance
from docopt import docopt

__version__ = '1.0'
#_ASACII = "!@#$%^&*-"
_ASACII = "!@#^*(){}|\":><?1234567890"

def display_output(arguements):
    """程序核心： 读取图像、调整格式、转换字符输出"""

    global _ASACII
    # if arguements['--alt-chars']:
    #     _ASACII = _ASCII2

    #加载图片
    try:
        im = Image.open(arguements['FILE'])
    except:
        raise IOError('can\'t open the file')

    #将颜色模式转换为RGBA
    im = im.convert('RGBA')



    #以字符个数为单位，获取当前终端的行数和列数
    try:
        _HEIGHT,_WIDTH = map(int,subprocess.check_output(['stty','size']).split())#该函数的作用就是就是将传入的命令交给系统执行，并以字符串格式返回执行结果
    except:
        _HEIGHT,_WIDTH = 50,50

    #按比例缩放
    aspect_ratio = im.size[0]/im.size[1]
    scaled_height = _WIDTH/aspect_ratio
    scaled_width = _HEIGHT*aspect_ratio*2

    #计算调整后的图像的宽度
    width = scaled_width
    height = scaled_height
    if scaled_width > _WIDTH:
        width = int(_WIDTH)
        height = int(scaled_height / 2)
    elif scaled_height > _HEIGHT:
        width = int(scaled_width)
        height = int(_HEIGHT)


    #将图像的长宽转换为指定值
    im = im.resize((width, height), resample=Image.ANTIALIAS)#resample 参数可选，指定了在变换图像大小过程中的采样方式，为了保证转变之后的图像质量，我们采用 PIL.Image.ANTIALIAS 选项指定高质量的采样滤波器。


    #创建 PIL.ImageEnhance.Contrast 对象，用于调整对比度
    enhance = ImageEnhance.Contrast(im)
    im = enhance.enhance(float(arguements['--contrast']))

    #获取im的图像数据
    img = im.getdata()

    #将图像转换为灰阶图
    im = im.convert('L')

    #定义前景色和背景色
    bg = rgb(0,0,0)
    fg = rgb(5,5,5)


    #是否加粗显示
    bold = None

    if(arguements['--bold']):
        bold = True
    else:
        bold = False

    row_len = 0
    for (count,i) in enumerate(im.getdata()):
        #像素映射到字符
        ascii_char = _ASACII[int((i/255.0) * (len(_ASACII)-1))]

        #如果要求转换为彩色字符
        if arguements['--colors']:
            color = rgb(int((img[count][0]/255.0)*5), int((img[count][1]/255.0)*5),int((img[count][2]/255.0)*5))

            bg = color
            fg = rgb(0,0,0)

        print_color(ascii_char,end='',fg= fg, bg= bg, bold= bold)
        row_len +=1

        #当列数对于终端宽的时候进行换行，并将row_len 重新设置0
        if row_len == width:
            row_len = 0
            print('')







def main():
    #通过docopt获取命令行解析之后的字典
    arguements = docopt(__doc__,version=__version__)

    #若没有FILE参数就打印帮助信息，有就转换
    if arguements['FILE']:
        display_output(arguements)
    else:
        print(__doc__)

if __name__ == "__main__":
    main()