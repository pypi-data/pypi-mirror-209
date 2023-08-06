from setuptools import setup, find_packages


filepath = 'README.md'

# python setup.py bdist_wheel # 打包为whl文件
# python setup.py sdist # 打包为tar.gz文件

setup(
    name="FishProcessManagement",
    version="2023.5.23.4",
    author="FishProcessManagement",
    author_email="2645602049@qq.com",
    description="一个后台项目管理器，适用于启动或关闭多个毫不相关的项目，注意他不是函数，只允许启动时指定程序的位置",

    # 项目主页
    url="https://space.bilibili.com/698117971?spm_id_from=333.1007.0.0",
    # 长描述
    long_description=open(filepath, encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    # 你要安装的包，通过 setuptools.find_packages 找到当前目录下有哪些包
    packages=find_packages(),


    # 依赖包，没有将会自动下载
    install_requires=[],
        package_data={
        'my_package': ['main.py','child.py'],
    },
)
