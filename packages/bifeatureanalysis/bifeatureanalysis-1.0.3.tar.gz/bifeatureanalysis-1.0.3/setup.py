'''
Date         : 2023-05-18 10:52:38
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2023-05-18 17:55:59
LastEditors  : BDFD
Description  : 
FilePath     : \setup.py
Copyright (c) 2023 by BDFD, All Rights Reserved. 
'''
'''
Author:  BDFD
Date: 2021-10-27 18:39:19
LastEditTime: 2022-07-26 11:00:44
LastEditors: BDFD
Description: In User Settings Edit
FilePath: \Section5.3-PyPi_Feature_Engineering\setup.py
'''

from setuptools import setup, find_packages
import os
here = os.path.abspath(os.path.dirname(__file__))
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

VERSION = '1.0.3'
DESCRIPTION = 'common usage in feature engineering analysis, make analysis more easily'
PACKAGE_NAME = 'bifeatureanalysis'

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author="BDFD",
    author_email="bdfd2005@gmail.com",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bdfd",
    project_urls={
        "Bug Tracker": "https://github.com/bdfd",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
)
