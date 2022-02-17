import boto3
s3 = boto3.resource('s3')
s3.Bucket('music-converter-bucket').upload_file('dummy_movie/test.mp3', 'music/test.mp3')
