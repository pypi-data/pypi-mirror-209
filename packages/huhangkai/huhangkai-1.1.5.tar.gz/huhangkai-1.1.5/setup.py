from setuptools import setup, find_packages

setup(
    name='huhangkai',  # 对外模块的名字
    version='1.1.5',  # 版本号
    description='接口自动化',  # 描述
    author='胡杭凯',  # 作者
    author_email='3173825608@qq.com',
    # package_dir={"": "commen"},
    packages=find_packages(),
    package_data={'by': ['常用命令.bat'],},
    python_requires=">=3.0",
    install_requires=[
        "faker==15.1.3",
        "openpyxl==3.0.10",
        "apscheduler",
        "rsa==4.9",
        "pyDes==2.0.1",
        "pycryptodome==3.17",
    ],
)