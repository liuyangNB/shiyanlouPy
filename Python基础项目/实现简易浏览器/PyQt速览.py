from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

#第一个窗口
class MainWindow1(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        #设置窗口标题
        self.setWindowTitle("这是我的窗口")

        #设置标签
        label = QLabel("欢迎光临，我是label")
        label.setAlignment(Qt.AlignCenter)#设置标签在中心
        self.setCentralWidget(label)

#信号槽
class MainWindow2(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.windowTitleChanged.connect(self._my_func)##信号被触发的时候给mufun传递了标题窗口参数
        # 设置窗口标题

        self.setWindowTitle("这是我的窗口")

        # 设置标签
        label = QLabel("欢迎光临，我是label")
        label.setAlignment(Qt.AlignCenter)  # 设置标签在中心
        self.setCentralWidget(label)

    def _my_func(self,s='myfunc',a=100):
        dic = {'s':s,'a':a}
        print(dic)

# 信号槽-lambda
class MainWindow3(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.windowTitleChanged.connect(lambda x: self._my_func('shiyanlou',666))  ##信号被触发的时候给mufun传递了标题窗口参数
        # 设置窗口标题

        self.setWindowTitle("这是我的窗口")

        # 设置标签
        label = QLabel("欢迎光临，我是label")
        label.setAlignment(Qt.AlignCenter)  # 设置标签在中心
        self.setCentralWidget(label)

    def _my_func(self, s='myfunc', a=100):
        dic = {'s': s, 'a': a}
        print(dic)

#信号槽-按钮
class MainWindow4(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("My press button app")
        #添加布局
        layout = QHBoxLayout()
        #创建按钮
        for i in range(5):
            button = QPushButton('这是第'+str(i)+'号按钮')
            #将按钮按压信号与自定义函数关联
            button.pressed.connect(lambda x=i:self._my_func(x))
            #将按钮添加到布局
            layout.addWidget(button)

        #创建部件
        #widget = Qwidget() 大小写啊
        widget = QWidget()
        #将布局添加到部件
        widget.setLayout(layout)

        #将部件添加到主窗口
        self.setCentralWidget(widget)

    def _my_func(self,x):
        print('这是',x)

#自定义信号
class MainWindow5(QMainWindow):
    my_dignal = pyqtSignal(str)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)#调用父类的初始化

        #设置窗口标题
        self.setWindowTitle("my 自定义信号 APP")

        button = QPushButton('点我')
        button.pressed.connect(self._click_button)
        # 将自定义信号与相应的槽函数连接
        self.my_dignal.connect(self._my_func_)
        self.setCentralWidget(button)#将部件添加到主窗口

    #自定义的信号处理函数
    def _click_button(self):
        self.my_dignal.emit('这里是_click_button函数')##这里是emit！！！不是connect！！！


    def _my_func_(self,str):
        print(str)

#工具栏 按钮 底部信息提示
class MainWindow6(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowTitle("my 工具栏和菜单 app")

        label = QLabel("welcome!!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)#添加标签到主窗口

        tb = QToolBar('ali')
        tb.setIconSize(QSize(16,20))
        self.addToolBar(tb)

        #添加按钮动作，并加载图标
        button_action = QAction(QIcon('./icons/penguin.png'),'菜单栏',self)
        #状态栏提示
        button_action.setStatusTip("这是菜单按钮")
        button_action.triggered.connect(self.onButtonClick)
        button_action.setCheckable(True)#检查是否按下，按下就不能按了；false就是可以一直按那种

        tb.addAction(button_action)
        self.setStatusBar(QStatusBar(self))

    def onButtonClick(self,s):
        print(s)

#为应用添加菜单栏
class MainWindow7(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowTitle("my 工具栏和菜单 app")

        label = QLabel("welcome!!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)#添加标签到主窗口

        tb = QToolBar('ali')
        tb.setIconSize(QSize(16,20))
        self.addToolBar(tb)

        #添加按钮动作，并加载图标
        button_action = QAction(QIcon('./icons/penguin.png'),'菜单栏',self)
        #状态栏提示
        button_action.setStatusTip("这是菜单按钮")
        button_action.triggered.connect(self.onButtonClick)
        button_action.setCheckable(True)#检查是否按下，按下就不能按了；false就是可以一直按那种

        tb.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

        #添加菜单栏
        mb = self.menuBar()#这类变量没有补全提示，咋么办？
        mb.setNativeMenuBar(False)
        file_menu = mb.addMenu('文件')
        file_menu2 = mb.addMenu('文件2')
        file_menu.addAction(button_action)



    def onButtonClick(self,s):
        print(s)

#实现二级菜单
class MainWindow8(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowTitle("my 工具栏和菜单 app")

        label = QLabel("welcome!!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)#添加标签到主窗口

        tb = QToolBar('没有用！不会显示的')
        tb.setIconSize(QSize(16,20))
        self.addToolBar(tb)

        #添加按钮动作，并加载图标
        button_action1 = QAction(QIcon('./icons/penguin.png'),'菜单栏',self)
        button_action2 = QAction('C++', self)
        button_action3 = QAction('Python', self)
        #状态栏提示
        button_action1.setStatusTip("这是菜单按钮")
        button_action2.setStatusTip("这是C++按钮")
        button_action3.setStatusTip("这是Python按钮")
        button_action1.triggered.connect(self.onButtonClick)
        button_action2.triggered.connect(self.onButtonClick)
        button_action3.triggered.connect(self.onButtonClick)
        button_action1.setCheckable(True)#检查是否按下，按下就不能按了；false就是可以一直按那种
        button_action2.setCheckable(True)
        button_action3.setCheckable(True)

        tb.addAction(button_action1)
        tb.addAction(button_action2)
        tb.addAction(button_action3)

        self.setStatusBar(QStatusBar(self))

        #添加菜单栏
        mb = self.menuBar()#这类变量没有补全提示，咋么办？
        mb.setNativeMenuBar(False)#禁止原生菜单栏

        file_menu = mb.addMenu('文件')
        file_menu2 = mb.addMenu('文件2')
        file_menu.addAction(button_action1)#为文件菜单栏添加动作
        file_menu.addSeparator()#为菜单选项添加分隔符

        #添加二级菜单
        build_system_menu = file_menu.addMenu('Build System')
        build_system_menu.addAction(button_action1)
        build_system_menu.addSeparator()
        build_system_menu.addAction(button_action2)
        build_system_menu.addSeparator()
        build_system_menu.addAction(button_action3)



    def onButtonClick(self,s):
        print(s)




#窗口部件-部件有很多，这里只展示一部分，具体可以参考官方文档
class MainWindow9(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowTitle("my 窗口部件 app")

        #定义布局
        layout = QVBoxLayout()
        #展示的部件列表
        widgets = [QCheckBox,QComboBox,QDateEdit,QDateTimeEdit,QDial,QDoubleSpinBox,QFontComboBox,
                   QLCDNumber,QLineEdit,QProgressBar,QPushButton,QRadioButton,QSlider,QSpinBox,QTimeEdit]

        for item in widgets:
            layout.addWidget(item())

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

#布局--水平布局
class Color(QWidget):
    def __init__(self,color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window,QColor(color))
        self.setPalette(palette)
class MainWindow10(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my 布局-垂直 app")

        colors = ['red','green','blue','yellow']
        #水平布局
        layout = QVBoxLayout()
        for color in colors:
            layout.addWidget(Color(color))

        widqet = QWidget()
        widqet.setLayout(layout)
        self.setCentralWidget(widqet)

#布局--网格布局
class Color(QWidget):
    def __init__(self,color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window,QColor(color))
        self.setPalette(palette)
class MainWindow11(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my 布局-垂直 app")

        colors = ['red','green','blue','yellow']
        #水平布局
        layout = QGridLayout()##这个地方设置很重要噢
        for i,color in enumerate(colors):
            for j in range(len(colors)):
                layout.addWidget(Color(color), i, j)


        widqet = QWidget()
        widqet.setLayout(layout)
        self.setCentralWidget(widqet)

#对话框
class CustomDialog(QDialog):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowTitle("new Dialog")
        #添加按钮
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel###TMD 一个小写的ok写出Ok出错！！！
        buttonBox = QDialogButtonBox(QBtn)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(buttonBox)
        self.setLayout(layout)

class MainWindow12(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(" my 按钮 app")

        label = QLabel('welcome to here')
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)#添加标签到主窗口

        #添加按钮动作
        button_action = QAction('New dialog',self)
        button_action.triggered.connect(self.onButtonClick)

        #添加菜单栏
        mb = self.menuBar()
        mb.setNativeMenuBar(False)#禁用原生菜单栏
        file_menu = mb.addMenu('&File')
        file_menu.addAction(button_action)#为文件菜单栏添加动作

    def onButtonClick(self,s):
        print('11')
        dlg = CustomDialog(self)
        #运行对话框，这一步很重要
        dlg.exec_()







def main():
    #创建应用实例，通过sys.argv传入命令行参数
    app = QApplication(sys.argv)
    #创建窗口实例
    window = MainWindow12()
    #显示窗口
    window.show()
    #执行应用，进入事件循环
    app.exec()

if __name__ == "__main__":
    main()