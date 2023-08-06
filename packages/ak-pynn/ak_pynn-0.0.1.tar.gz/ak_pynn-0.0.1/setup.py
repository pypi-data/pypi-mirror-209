# To publish on PyPi, run the following
# python setup.py sdist
# twine upload dist/* 
import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "ak_pynn",
    version = "0.0.1", # DONT FORGET TO CHANGE THE VERSION IN __INIT__.py
    author = "Ankit kohli",
    author_email = "contact.ankitkohli@gmail.com",
    description = ("A simplistic and efficient pure-python neural network library"),
    license = "MIT",
    keywords = ["neural network", "pure python","machine learning", "ML", "deep learning", "deepL", "MLP", "ANN" ,"perceptron","ankit kohli","ak_pynn","aknn"],
    packages=['ak_pynn'],
    # long_description=read('README.md'),
    # long_description_content_type='text/markdown',
    install_requires=['numba>=0.54.1',
                      'numpy==1.19.2', 
                      'tqdm',
                      'opt_einsum',
                      'nnv',
                      'matplotlib',
                      'opencv-python' ,
                      'seaborn' ,
                      'time' ,
                      'random'              
                      ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        'Programming Language :: Python :: 3.0',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
    ],
)