import json
import sklearn
import pandas

def dragonModel(event, context):
    response = {
        "statusCode": 200,
        "body": pow(event['queryStringParameters']['number1'], 2)+pow(event['queryStringParameters']['number2'], 2)
    }
    
    return response
