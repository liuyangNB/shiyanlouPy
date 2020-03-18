"""如果 __init__.py 文件内有一个名为 __all__ 的列表，那么只有在列表内列出的名字将会被公开。"""

if __name__ == '__main__':
    print("作为主程序运行")
else:
    print("package 初始化")