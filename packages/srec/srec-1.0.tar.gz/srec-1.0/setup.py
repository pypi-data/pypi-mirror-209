from setuptools import setup, find_packages

setup(
    name='srec',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'calculate = calculate:main'
        ]
    },
    install_requires=[
        'datetime',
    ],
    author='Trrrrw',
    author_email='wzhhenry@qq.com',
    description='A simple module to calculate the time required for leveling up in Honkai: Star rail.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
