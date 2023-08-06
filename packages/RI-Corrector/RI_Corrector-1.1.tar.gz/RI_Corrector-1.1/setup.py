#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

VERSION = "1.1"
DESCRIPTION = "A tool base on RI to correct RT"
LONG_DESCRIPTION = 'An acquisition time correction tool based on the retention index system for LC-MS data'
    
# Setting up
setup(
      name="RI_Corrector",
      version=VERSION,
      author="Lacter",
      author_email="<740318407@qq.com>",
      description=DESCRIPTION,
      long_description_content_type = "text/markdown",
      long_description = LONG_DESCRIPTION,
      packages=find_packages(),
      install_requires=['pyopenms','pandas','progress','matplotlib','numpy'],
      keywords=['LC-MS','RI system','RT Correct','Raw LC-MS Data'],
      classifiers=[
          "Programming Language :: Python :: 3",
          "Operating System :: MacOS :: MacOS X",
          "Operating System :: Microsoft :: Windows"
          ]     
      )