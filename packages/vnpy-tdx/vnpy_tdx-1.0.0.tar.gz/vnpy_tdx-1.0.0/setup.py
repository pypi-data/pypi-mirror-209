from setuptools import setup, find_packages
setup(
    name="vnpy_tdx",
    version="1.0.0",
    keywords=("vnpy", "vnpy_tdx", "vnpytdx"),
    description="vnpy通达信数据服务",
    long_description="vnpy通达信数据服务",
    license="MIT Licence",
    url="https://github.com/bthuntergg/vnpy_tdx",
    author="jan",
    author_email="bthuntergg@qq.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[]
)