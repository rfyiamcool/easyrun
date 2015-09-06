import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name = "easyrun",
        version = "1.0",
        author = "ruifengyun",
        author_email = "rfyiamcool@163.com",
        description = "a simple subprocess manage",
        #wpackages=['easyrun'],
        license = "MIT",
        keywords = "subprocess easyrun fengyun",
        url = "https://github.com/rfyiamcool",
        long_description = read('README.md'),
        classifiers = [
            'Topic :: Utilities',
            'License :: OSI Approved :: MIT License'
            ]
        )

