import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name = "easyrun",
        version = "3.0",
        author = "ruifengyun",
        author_email = "rfyiamcool@163.com",
        description = "a simple subprocess manage",
        packages=['easyrun'],
        license = "MIT",
        keywords = "subprocess easyrun fengyun",
        url = "https://github.com/rfyiamcool",
        long_description = read('README.md'),
        classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Topic :: Software Development :: Libraries :: Python Modules',
            ]
        )

