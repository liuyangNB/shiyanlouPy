
"""用于创建原码压缩包或安装软件"""

from setuptools import find_packages, setup

setup(name = 'factorial-ly',
    version = '0.1',
    description = "Factorial module.",
    long_description = "A test module for our book.",
    platforms = "Win10",
    author = 'Lau',
    author_email = 'liuyang.nb@outlook.com',
    url = "mygithub...",
    lcense = "MIT",
    pacages = find_packages()#是一个能够在你源目录下找到所以模块的特殊函数
    )