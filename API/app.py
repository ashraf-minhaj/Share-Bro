"""
Backend API for Share Bro

purpose:
    * Generate Presigned URL: http://127.0.0.1:5000/getpresignedurl/file_extension
"""


import uuid
import boto3
from botocore.config import Config
from flask import Flask, request, jsonify
from flask_cors import CORS


# env specific vars
# enter your bucket name here
BUCKET = 'bucket'             # aws s3 ls | awk 'NR==2{print $3}'
REGION = boto3.Session().region_name    # aws configure list | grep region | awk '{print $2}'


# init flask
app = Flask(__name__)
CORS(app)

# init aws client(s)
s3 = boto3.client('s3', region_name=REGION, config=Config(signature_version='s3v4'))


@app.route('/')
def home():
    return "It works, Kudos Brother!"


@app.route('/getpresignedurl/<file_ext>', methods=["GET"])
def generate_presigned_url(file_ext):
    """ assign uuid with user sent file extention.
    for file.mp4 it will be uuuid.mp4. """
    # print(file_ext)
    pre_signed_url  = None
    error           = None
    success         = False
    httpStatusCode  = 404

    key = generate_key_name(file_ext)
    try:
        pre_signed_url = s3.generate_presigned_url(
            'put_object',                             
            Params={
                'Bucket':BUCKET, 
                'Key': key
                },
            ExpiresIn=3600,
            HttpMethod='PUT'
        )

        print(pre_signed_url)
        if pre_signed_url:
            success         = True
            httpStatusCode  = 200
    except Exception as e:
        error = e

    response = jsonify({
        "success"           : success,
        "httpStatusCode"    : httpStatusCode,
        "signedUrl"         : pre_signed_url,
        "aws_region"        : REGION,
        "key"               : key,
        "error"             : str(error)
    })

    print(response)
    return response


def generate_key_name(file_ext):
    return uuid.uuid4().hex + '.' + file_ext
