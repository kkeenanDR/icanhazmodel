# -*- coding: utf-8 -*-
"""Click commands."""
import os
import click
import boto3

@click.command()
@click.option(
    "-p",
    "--profile",
    default="default",
    help="the profile you would like to use from ~/.aws/credentials",
)
@click.option(
    "-b",
    "--bucket",
    default="appliedml",
    help="the name of the bucket that the target objects are stored in on s3",
)
@click.option(
    "-m",
    "--model_dir",
    default="ptms",
    help="the directory that you would like the s3 objects to be written within",
)
@click.option(
    "-k",
    "--model_key",
    default=None,
    help="the object key underwhich to download all objects",
)
def cli(profile="default", bucket="appliedml", model_dir="ptms", model_key=None):
    """
    A simple function for downloading all files within a bucket
    and under a given key prefix, which will write objects to
    local locations that are faithful to the path structure
    as defined in the object keys
    
    Parameters
    
        aws_profile (str): the profile you would like to use from ~/.aws/credentials
        bucket (str): the name of the bucket that the target objects are stored in on s3
        model_dir (str): the directory that you would like the s3 objects to be written within
        model_key (str): the object key underwhich to download all objects
    
    Returns
    
        Writes all detected objects to disk
    """
    # create the path structure required
    ptm_dir_full = model_dir + "/" + model_key
    if not os.path.exists(ptm_dir_full):
        os.makedirs(ptm_dir_full.replace(os.path.basename(ptm_dir_full), ""))
    # instantiate an aws::s3 client
    session = boto3.session.Session(profile_name=profile)
    s3 = session.client('s3')
    # detect all target objects
    all_objects = s3.list_objects(Bucket=bucket, Prefix=model_key)
    if all_objects["Contents"]:
        for obj in all_objects["Contents"]:
            target = model_dir + "/" + obj["Key"]
            non_basename = target.replace(os.path.basename(target), "")
            if not os.path.exists(non_basename):
                os.makedirs(non_basename)
                if not os.path.isdir(target):
                    with open(target, 'wb') as f:
                        s3.download_fileobj(bucket, obj["Key"], f)
    else:
        print("No objects detected")
