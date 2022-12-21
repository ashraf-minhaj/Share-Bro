"""
Backend API for Share Bro

purpose:
    * Generate Presigned URL
"""


import boto3
from botocore.config import Config
from subprocess import Popen, PIPE
from flask import Flask, request, jsonify


# env specific vars
# enter your bucket name here
BUCKET = '' # aws s3 ls | awk 'NR==2{print $3}'
REGION = boto3.Session().region_name    # aws configure list | grep region | awk '{print $2}'


# init flask
app = Flask(__name__)

# init aws client(s)
# session = boto3.Session()
s3 = boto3.client('s3', region_name=REGION, config=Config(signature_version='s3v4'))

@app.route('/getpresignedurl/<file_name>', methods=["GET"])
def generate_presigned_url(file_name):
    # print(file_name)
    pre_signed_url  = None
    error           = None
    success         = False
    httpStatusCode  = 404

    try:
        pre_signed_url = s3.generate_presigned_url(
            'put_object',                             
            Params={
                'Bucket':BUCKET, 
                'Key':file_name
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

    return jsonify({
        "success"           : success,
        "httpStatusCode"    : httpStatusCode,
        "sirgnedUrl"        : pre_signed_url,
        "aws_region"        : REGION,
        "key"               : file_name,
        "error"             : str(error)
    })