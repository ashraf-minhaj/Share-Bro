"""
Backend API for Share Bro

purpose:
    * Generate Presigned URL
"""

from flask import Flask, request, jsonify
import boto3
from botocore.config import Config

# env specific vars
REGION = 'ap-south-1'
BUCKET = ''

# init
app = Flask(__name__)

@app.route('/getpresignedurl', methods=["GET"])
def testget():
    return jsonify({
        "success" : True,
        "httpStatusCode" : 200,
        "sirgnedUrl" : "http://xyz.com"
    })