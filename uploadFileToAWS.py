import boto3
bucket_name = 'bucket_name' # having public access


def upload_text_file():
    content = open('local_file.txt', 'rb')
    s3 = boto3.client('s3')
    s3.put_object(
       Bucket=bucket_name,
       Key='remote-file.txt',
       Body=content
    )


upload_text_file()


def upload_media_file(f1):
    content = open(f1, 'rb')
    s3 = boto3.client('s3')
    s3.put_object(
       Bucket=bucket_name,
       Key='remote-file-2.png',
       Body=content
    )


# f1 = 'python_java.mp4'

# f1 = 'local_file.txt'
f1 = 'bitmoji.png'
upload_media_file(f1)


def upload_media_file(f1, key1):
    content = open(f1, 'rb')
    s3 = boto3.client('s3')
    s3.put_object(
       Bucket=bucket_name,
       Key=key1,
       Body=content
    )


f1 = 'python_java.mp4'
key1 = 'remote-file-3.mp4'
upload_media_file(f1, key1)

print("done")
