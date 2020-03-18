from PIL import Image
import argparse

"""-------------处理命令行参数---------------"""
"""这是是设置终端里面输入一些参数的时候可以设置的东西：
python ascii_img.py -o liuyangout --width 30 --height 30 IMG.jpg这样就能解析出输入参数的含义
"""
#首先构建命令行输入参数处理 ArgumentParser 实例
parser = argparse.ArgumentParser()

# 定义输入文件、输出文件、输出字符画的宽和高
parser.add_argument('file')#输入文件
parser.add_argument('-o','--output')#输出文件
parser.add_argument('--width',type = int, default=80)#输出字符画 宽
parser.add_argument('--height',type=int, default=80)#输出字符画 高

#解析并获取参数
args = parser.parse_args()

#输入图片文件路径
IMG = args.file

#input ASCmag's width
WIDTH = args.width

#imout ASCmag's height
HEIGHT = args.height

OUTPUT = args.output

"""-------------实现RGB值转字符的函数---------------"""
ascii_charlist = list("!@#$%^&*()_+qwertyuiop[]\\asdfghjkl;'zxcvbnm,./QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?")

def get_char(r,g,b,alpha = 256):
    #RGB转字符的函数
    if alpha == 0:
        return ' '

    length = len(ascii_charlist)

    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0+1)/length

    return ascii_charlist[int(gray/unit)]

"""-------------处理图片---------------"""

if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    #初始化输出的字符串
    txt = ""

    for j in range(HEIGHT):
        for i in range(WIDTH):
            txt += get_char(*im.getpixel((i,j)))

        txt += '\n'

    print(txt)

    if OUTPUT:
        with open(OUTPUT,'W') as f:
            f.write(txt)
    else:
        with open("output.txt", "w") as f:
            f.write(txt)