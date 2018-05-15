from setuptools import setup

setup(
    name="script",
    version='0.1',
    py_modules=['hello.py'],
    install_requires=['Click',],
    entry_points='''
    [console_scripts]
    script=hello.py:cli
    ''',
)
