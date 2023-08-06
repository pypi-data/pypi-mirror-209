import pathlib
from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.1.2'
DESCRIPTION = 'DevCellPy is a Python package designed for hierarchical multilayered classification of cells based on single-cell RNA-sequencing (scRNA-seq). It implements the machine learning algorithm Extreme Gradient Boost (XGBoost) (Chen and Guestrin, 2016) to automatically predict cell identities across complex permutations of layers and sublayers of annotation.'

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="devcellpy",
    version=VERSION,
    author = "Francisco Galdos and Sidra Xu",
    author_email="<fxgaldos@stanford.edu> and <sidraxu@stanford.edu>",
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "xgboost",
        "sklearn",
        "shap",
        "scanpy"],
    url="https://github.com/DevCellPy-Team/DevCellPy",
    license='MIT',
    keywords=["python","cardiology","scRNA","genetics","machine learning","biology","bioinformatics","devcellpy"],
    classifiers=["Intended Audience :: Science/Research","Programming Language :: Python"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "devcellpy=devcellpy.devcellpy:main",
        ]
    }
    
    )
