import setuptools #导入setuptools打包工具
 
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="dhmsaiffconverter", 
    version="1.0",    #包版本号，便于维护版本
    author="David Bao",    #作者，可以写自己的姓名
    author_email="daijiebao0617@outlook.com",    #作者联系方式，可写自己的邮箱地址
    description="converter raw aiff vibration data to csv data file",#包的简述
    long_description=long_description,    #包的详细介绍，一般在README.md文件内
    long_description_content_type="text/markdown",
    url="https://github.com/DJ0617/DHMS_aiff_to_csv",    #自己项目地址，比如github的项目地址
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',    #对python的最低版本要求
)

