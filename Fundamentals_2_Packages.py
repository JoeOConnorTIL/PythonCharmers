# Python Packages
# A package in Python is like a toolbox that contains a variety of tools (called functions and modules) which you can use to perform specific tasks more easily and efficiently.

# These packages are created by other developers and can be installed and used in your own Python programs.

# For data analysts, packages are particularly useful because they provide specialized tools and functions that are tailored for data analysis tasks.

# Let's take the example of the pandas library/package:

# Data Handling and Manipulation: Pandas makes it easy to handle and manipulate data. It provides functions to read data from various file formats (like CSV, Excel, etc.), clean data, and transform it into a useful format.
# Data Analysis: With pandas, you can perform complex data analysis tasks with just a few lines of code. It offers functionalities for grouping data, calculating statistics, and performing aggregations.
# Efficiency: Writing the code for all these tasks from scratch would be time-consuming and error-prone. Pandas provides a tested and optimized set of functions that can save a lot of time and effort.
# Not all packages are installed by default
# Installing a package using pip.

# pipis the package installer for Python. You can use it to install packages from the Python Package Index (PyPI).

# Basic command: pip install package_name
# I have done pip install pandas within the terminal in the virtual environment for this project.

import pandas as pd # type: ignore
data = pd.read_csv('C:\\Users\\JOE\\Documents\\Data for Python\\2019_Yellow_Taxi_Trip_Data.csv')
print(data.head())

# note in the file path, using double backslashes escapes the backslashes so that python doesn't interpret \U or \D or \P escape sequences

# Alternatively you can install packages from the notebook

# Exercise 2: Install Numpy via Notebook

# The script below will allow you to execute a terminal command here in the notebook
#  - sys is part of Python's standard library and provides access to variables used or maintained by the Python interpreter
#  - sys.executable holds the path to the Python interpreter that your Jupyter notebook is using
#  - '-m' is a flag is used with the Python interpreter to run a 'pip' as a script, i.e to install the package

#import sys
#!{sys.executable} -m pip install numpy

# Package Versions
# Packages in Python, as in most software, have different versions for several important reasons:

# Feature Updates and Improvements
# Bug Fixes
# Security Updates, and many more
# Different versions allow users to choose which version best fits their needs. For instance, a user may stick with an older, stable release for a critical application, while another might prefer the latest version for access to the newest features. Managing these versions and understanding the implications of updating (or not updating) is an important aspect of working with Python packages.

# Check a Package's Version
# Python packages often have their version information accessible via a version attribute. To check the version of a package, you first need to import it and then access this attribute.

# Checking a package's version:

import numpy  # type: ignore
print(numpy.__version__)

# Downgrading a Package
# Sometimes, you might need to downgrade a package to ensure compatibility with other packages or specific codebases. To downgrade, specify the package name along with the desired version. For example:

# pip install package_name==1.23.5

# Exercise: Downgrade numpy to version 1.18.5
# Using:
# - Terminal: pip install numpy==1.18.5
# - Notebook: 
# import sys
# !{sys.executable} -m pip install numpy==1.18.
# Remember to restart the Jupyter kernel after upgrading to use the updated package.
# Upgrading a Package
# Upgrading a package ensures that you have the latest features and bug fixes. Use pip with the --upgrade flag to update a package. For example:

# pip install --upgrade package_name

# Exercise: Upgrade Numpy to latest version
# Either in Terminal or in the script below

# import sys
# !{sys.executable} -m [insert your code here]