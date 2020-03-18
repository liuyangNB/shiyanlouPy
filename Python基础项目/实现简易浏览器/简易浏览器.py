from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import sys
#主要窗口
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("我的浏览器")
        self.setWindowIcon(QIcon('./icons/penguin.png'))
        self.show()

        #设置浏览器
        self.browser = QWebEngineView()
        url = 'https://www.shiyanlou.com/'
        self.browser.setUrl(QUrl(url))#打开指定页面的url
        #添加浏览器到窗口
        self.setCentralWidget(self.browser)

#添加导航栏
class MainWindow1(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("我的浏览器")
        self.setWindowIcon(QIcon('./icons/penguin.png'))
        self.show()

        #设置浏览器
        self.browser = QWebEngineView()
        url = 'https://www.shiyanlou.com/'
        self.browser.setUrl(QUrl(url))#打开指定页面的url
        #添加浏览器到窗口
        self.setCentralWidget(self.browser)

        #添加导航栏
        navigation_bar= QToolBar('导航栏目')
        navigation_bar.setIconSize(QSize(16,16))
        self.addToolBar(navigation_bar)

        back_button = QAction(QIcon('./icons/back.png'),"back",self)
        next_button = QAction(QIcon('./icons/next.png'),'Forward',self)
        stop_button = QAction(QIcon('./icons/cross.png'),'stop',self)
        reload_button = QAction(QIcon('./icons/renew.png'),'reload',self)

        #利用 QWebView 封装的槽实现了这些按钮的实际功能。
        back_button.triggered.connect(self.browser.back)
        next_button.triggered.connect(self.browser.forward)
        stop_button.triggered.connect(self.browser.stop)
        reload_button.triggered.connect(self.browser.reload)

        #将按钮添加到导航栏
        navigation_bar.addAction(back_button)
        navigation_bar.addAction(next_button)
        navigation_bar.addAction(stop_button)
        navigation_bar.addAction(reload_button)

#添加地址栏
class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("我的浏览器")
        self.setWindowIcon(QIcon('./icons/penguin.png'))
        self.show()

        #设置浏览器
        self.browser = QWebEngineView()
        url = 'https://www.baidu.com/'
        self.browser.setUrl(QUrl(url))#打开指定页面的url
        #添加浏览器到窗口
        self.setCentralWidget(self.browser)

        #添加导航栏
        navigation_bar= QToolBar('导航栏目')
        navigation_bar.setIconSize(QSize(16,16))
        self.addToolBar(navigation_bar)

        back_button = QAction(QIcon('./icons/back.png'),"back",self)
        next_button = QAction(QIcon('./icons/next.png'),'Forward',self)
        stop_button = QAction(QIcon('./icons/cross.png'),'stop',self)
        reload_button = QAction(QIcon('./icons/renew.png'),'reload',self)

        #利用 QWebView 封装的槽实现了这些按钮的实际功能。
        back_button.triggered.connect(self.browser.back)
        next_button.triggered.connect(self.browser.forward)
        stop_button.triggered.connect(self.browser.stop)
        reload_button.triggered.connect(self.browser.reload)

        #将按钮添加到导航栏
        navigation_bar.addAction(back_button)
        navigation_bar.addAction(next_button)
        navigation_bar.addAction(stop_button)
        navigation_bar.addAction(reload_button)

        #添加URL地址栏
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        navigation_bar.addSeparator()
        navigation_bar.addWidget(self.urlbar)


    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == '':#??
            q.setScheme('http')
        self.browser.setUrl(q)


#再细节的标签页之类的看看教程好了，感觉就是调用轮子


#创建应用
app = QApplication(sys.argv)
window = MainWindow2()
window.show()
app.exec_()
