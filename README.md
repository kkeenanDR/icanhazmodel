# A simple cli interface for downloading AML model artifacts

## Overview

The Data Strategy and Financial Services Data Science teams contribute to and maintain a conduct surveillance pretrained model object repository in aws::s3. This tool provides a simple interface for downloading those model artifacts, and saving them to disk, following the directory structure define within the object keys.

## Implementation

The tool is a python package providing a simple cli interface. This cli tool can be made globally available, or restricted to a virtual environment.

## Installation

The best way to install the package is with `pip`. If you have `pip` installed you can run the following command:

```sh
pip install git+https://github.com/jkbr/httpie.git