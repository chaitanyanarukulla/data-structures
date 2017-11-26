"""."""
from setuptools import setup

setup(
    name='data-structures',
    description=('A package for building and '
                 'running the data-structures module'),
    package_dir={'': 'src'},
    author='Mark and Chai',
    author_email='chaitanyanarukulla@gmail.com mreynoso@spu.edu',
    py_modules=['binheap'],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-watch', 'tox'],
        'development': ['ipython']
    },
)
