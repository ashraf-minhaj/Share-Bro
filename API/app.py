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
BUCKET = ''
REGION = boto3.Session().region_name    # aws configure list | grep region | awk '{print $2}'


# init flask
app = Flask(__name__)

# init aws client(s)
s3 = boto3.client('s3', region_name=REGION, config=Config(signature_version='s3v4'))

@app.route('/getpresignedurl', methods=["GET"])
def generate_presigned_url():
    return jsonify({
        "success"           : True,
        "httpStatusCode"    : 200,
        "sirgnedUrl"        : "http://xyz.com",
        "aws_region"        : REGION
    })