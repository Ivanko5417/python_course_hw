from setuptools import setup

setup(
    name='tagcounter',
    version='1.0',
    author='Ivan Drobysh',
    packages=['tagcounter'],
    description='This package will help you to get the number of different tags on web site',
    package_data={'': ['*.yaml']},
    install_requires=[],
    entry_points={'console_scripts': ['tagcounter = tagcounter.__init__:main']},
)
