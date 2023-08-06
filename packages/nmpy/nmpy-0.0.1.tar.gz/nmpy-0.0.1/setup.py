from setuptools import setup

setup(
    name="nmpy",  # 包名字
    version="0.0.1",  # 包版本
    description="A numpy replacement",  # 简单描述
    author="Q",  # 作者
    author_email="",  # 作者邮箱
    py_modules=['nmpy'],  # 要打包的模块名字
    python_requires='>=3.6',  # Python版本依赖
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
