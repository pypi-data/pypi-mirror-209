from setuptools import setup, find_packages

setup(
    name='sql2dataframe',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'sqlalchemy'
    ],
    entry_points={
        'console_scripts': [
            'my_package_name=my_package_name.__main__:main'
        ]
    },
    author='zk',
    author_email='1475923992@qq.com',
    description='A package for connecting to a database and saving data to files',
    url='https://github.com/2413567/sql2pandas#/',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
