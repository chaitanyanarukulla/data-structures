from setuptools import setup

setup(
    name='data-structures',
    description='A package for building and running the data-structures module',
    package_dir={'':'src'},
    author='Mark and chai',
    author_email='chaitanyanarukulla@gmail.com mreynoso@spu.edu',
    py_modules=['linked_list'],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-watch', 'tox'],
        'development': ['ipython']
    },
    # entry_points={
    #     'console_scripts': [
    #     ]
    # }
)