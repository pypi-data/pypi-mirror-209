import click
from tqdm import tqdm
import boto3
import os
from dotenv import load_dotenv


load_dotenv()

@click.group()
def cli():
    pass



@click.command()
@click.option(
    "--bucket",
    "-b",
    required=True,
    type=str,
    help="The name of the S3 bucket to download from",
)
@click.option(
    "--object-path",
    "-o",
    required=True,
    type=str,
    help="Path to the object in the S3 bucket",
)
@click.option(
    "--file-path",
    "-f",
    required=True,
    help="The file to save the object to",
    type=click.Path(exists=False, dir_okay=False, resolve_path=True),
)
def download_object(bucket: str, object_path: str, file_path: str):

    endpoint_url = os.environ["AWS_ENDPOINT_URL"]
    key_id = os.environ["AWS_ACCESS_KEY_ID"]
    access_key = os.environ["AWS_SECRET_ACCESS_KEY"]
    region_name = os.environ["AWS_REGION_NAME"]

    client = boto3.client(
        "s3",
        endpoint_url=endpoint_url,
        region_name=region_name,
        aws_access_key_id=key_id,
        aws_secret_access_key=access_key,
    )

    response = client.head_object(
        Bucket=bucket,
        Key=object_path,
        ExpectedBucketOwner=key_id,
    )

    total_size = response["ContentLength"] / 1024 / 1024

    with tqdm(
        total=round(total_size, 2),
        desc=f"Downloading model to {file_path}",
        unit="MB",
        colour="cyan",
        bar_format="{l_bar}{bar:10}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]",
    ) as pbar:
        client.download_file(
            bucket,
            object_path,
            file_path,
            Callback=lambda bytes_transferred: pbar.update(
                round(bytes_transferred / 1024 / 1024, 2)
            ),
        )

@click.command()
@click.option(
    "--bucket",
    "-b",
    required=True,
    type=str,
    help="The name of the S3 bucket to upload to",
)
@click.option(
    "--object-path",
    "-o",
    required=True,
    type=str,
    help="Path in the S3 bucket to save the object to",
)
@click.option(
    "--file-path",
    "-f",
    required=True,
    help="The file to upload to S3",
    type=click.Path(exists=False, dir_okay=False, resolve_path=True),
)
def upload_object(bucket: str, object_path: str, file_path: str):
    endpoint_url = os.environ["AWS_ENDPOINT_URL"]
    key_id = os.environ["AWS_ACCESS_KEY_ID"]
    access_key = os.environ["AWS_SECRET_ACCESS_KEY"]
    region_name = os.environ["AWS_REGION_NAME"]


    # Get total size of the model in MB with 2 decimals
    total_size = round(os.path.getsize(file_path) / 1024 / 1024, 2)
    if file_path is None:
        file_path = os.path.basename(object_path)

    with tqdm(
        total=total_size,
        desc=f"Uploading model to {file_path}",
        unit="MB",
        colour="cyan",
        bar_format="{l_bar}{bar:10}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]",
    ) as pbar:
        client = boto3.client(
            "s3",
            endpoint_url=endpoint_url,
            region_name=region_name,
            aws_access_key_id=key_id,
            aws_secret_access_key=access_key,
        )

        client.upload_file(
            file_path,
            bucket,
            object_path,
            Callback=lambda bytes_transferred: pbar.update(
                round(bytes_transferred / 1024 / 1024, 2)
            ),
        )



cli.add_command(download_object)
cli.add_command(upload_object)

if __name__ == "__main__":
    cli()
