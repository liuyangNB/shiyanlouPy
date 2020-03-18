import turtle

def pan_snake():
    turtle.setup(650,350,200,200)#创建一个窗体（w,h,x0,y0)
    turtle.penup()#起笔
    turtle.fd(-250)#向后退（-x方向）250像素
    turtle.pendown()#落笔
    turtle.pensize(10)
    turtle.pencolor("purple")
    turtle.seth(-40)#朝向-40度；相对于极坐标的角度
    for i in range(4):
        turtle.circle(40,80)#圆心在画笔左边40处，画80度
        turtle.circle(-40,80)
    turtle.circle(40,80/2)
    turtle.fd(40)
    turtle.circle(16,180)
    turtle.fd(40*2/3)
    turtle.done()


#from turtle import *
def pen_circle():
    for i in range(500):  # 重复500次
        if i%3==0:
            turtle.penup()
        else:
            turtle.pendown()

        turtle.forward(i)
        turtle.left(89)

pen_circle()