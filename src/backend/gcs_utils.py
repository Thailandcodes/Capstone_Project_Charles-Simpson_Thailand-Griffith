from google.cloud import storage


def upload_file_to_gcs(
        bucket_name: str,
        source_file: str,
        destination_blob: str):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob)
    blob.upload_from_filename(source_file)

    return {
        "message": "File uploaded successfully",
        "bucket": bucket_name,
        "file": destination_blob
    }


def get_gcs_file_url(bucket_name: str, blob_name: str):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    return {
        "bucket": bucket_name,
        "file": blob_name,
        "public_url": blob.public_url
    }
