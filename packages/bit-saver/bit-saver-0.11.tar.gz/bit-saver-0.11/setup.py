from setuptools import setup, find_packages

setup(
    name="bit-saver",
    version="0.11",
    description="A package to save OHLCV data from Upbit exchange to local storage.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Choi Sun",
    author_email="choisun@tritech.co.kr",
    url="https://github.com/choisun0924/bit-saver",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(),
    install_requires=[
        'pyupbit',
        'pandas'
    ]
)
