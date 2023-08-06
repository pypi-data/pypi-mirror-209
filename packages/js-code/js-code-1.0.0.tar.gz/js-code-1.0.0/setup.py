import setuptools
from setuptools import setup

setup(
    name='js-code',
    version='1.0.0',
    author="Aduh",
    author_email="781159384@qq.com",
    packages=setuptools.find_packages(),
    description='A small example package',
    install_requires=['pyexecjs'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

