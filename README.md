# A simple cli interface for downloading AML model artifacts

## Overview

The Data Strategy and Financial Services Data Science teams contribute to and maintain a conduct surveillance pretrained model object repository in aws::s3. This tool provides a simple interface for downloading those model artifacts, and saving them to disk, following the directory structure define within the object keys.

## Implementation

The tool is a python package providing a simple cli interface. This cli tool can be made globally available, or restricted to a virtual environment.

## Installation

The best way to install the package is with `pip`. If you have `pip` installed you can run the following command:

```sh
pip install git+https://git.corp.digitalreasoning.com/scm/~kevin.keenan/icanhazmodel.git
```

## Usage

Once the package has successfully installed, you can download model artifacts as follows

```sh
icanhazmodel -p "kevin-digitalreasoning" -k "conduct/secrecy/en/version_1.2"
```

This may take some time to complete depending on your network speed, since all model components under the model key will be downloaded, including the training data. Below is a view of the directory tree following the above command:

```sh
cd ptms
tree .
```

```
