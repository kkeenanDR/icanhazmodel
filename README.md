# A simple cli interface for downloading AML model artifacts

## Overview

The Data Strategy and Financial Services Data Science teams contribute to and maintain a conduct surveillance pretrained model object repository in aws::s3. This tool provides a simple interface for downloading those model artifacts, and saving them to disk, following the directory structure define within the object keys.

By maintaining the directory structure of the actual model artifacts increases the accuracy with which we can communicate about specific data and model components, since their location on disk matches that in aws::s3, meaning collaborators can easily locate them for themselves.

## Implementation

The tool is a python package providing a simple cli interface. This cli tool can be made globally available, or restricted to a virtual environment.

## Installation

The best way to install the package is with `pip`. If you have `pip` installed you can run the following command:

```sh
pip install git+https://git.corp.digitalreasoning.com/scm/~kevin.keenan/icanhazmodel.git
```

## Usage

The basic usage of the tool can be view with

```sh
icanhazmodel --help
```

Which returns:

```sh
Usage: icanhazmodel [OPTIONS]

  A simple function for downloading all files within a bucket and under a
  given key prefix, which will write objects to local locations that are
  faithful to the path structure as defined in the object keys

  Parameters

      aws_profile (str): the profile you would like to use from
      ~/.aws/credentials     bucket (str): the name of the bucket that the
      target objects are stored in on s3     model_dir (str): the directory
      that you would like the s3 objects to be written within     model_key
      (str): the object key underwhich to download all objects

  Returns

      Writes all detected objects to disk

Options:
  -p, --profile TEXT    the profile you would like to use from
                        ~/.aws/credentials
  -b, --bucket TEXT     the name of the bucket that the target objects are
                        stored in on s3
  -m, --model_dir TEXT  the directory that you would like the s3 objects to be
                        written within
  -k, --model_key TEXT  the object key underwhich to download all objects
  --help                Show this message and exit.
  ```

Once the package has successfully installed, you can download all model model artifacts under the model key as follows:

```sh
icanhazmodel --profile "kevin-digitalreasoning" --model_key "conduct/secrecy/en/version_1.2"
```

This may take some time to complete depending on your network speed, since all model components under the model key will be downloaded, including the training data. Below is a view of the directory tree following the above command:

```sh
cd ptms
23:01 $ tree
.
└── conduct
    └── secrecy
        └── en
            └── version_1.2
                ├── data
                │   ├── README.txt
                │   ├── all_train.csv
                │   └── ft
                │       ├── test.csv
                │       └── train.csv
                └── models
                    ├── ft
                    │   ├── cognition-normalization.zip
                    │   ├── cs-secrecy-avg-pool.cognition.archive.zip
                    │   ├── cs-secrecy-avg-pool.cognition.spec.yaml
                    │   ├── cs-secrecy-max-pool.cognition.archive.zip
                    │   └── cs-secrecy-max-pool.cognition.spec.yaml
                    └── lr
                        ├── cs-secrecy-lr.engine
                        └── secrecy.model_pipeline.pkl
```

Similarly, if you would like to download only a specific field from a model key, you can do that too:

```sh
icanhazmodel --profile "kevin-digitalreasoning" --model_key "conduct/secrecy/en/version_1.2/models/ft/cs-secrecy-avg-pool.cognition.spec.yaml"
```

This will download the artifact to the following tree:

```sh
cd ptms
tree
.
└── conduct
    └── secrecy
        └── en
            └── version_1.2
                └── models
                    └── ft
                        └── cs-secrecy-avg-pool.cognition.spec.yaml
```