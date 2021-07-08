import json

def dragonModel(event, context):
    response = {
        "statusCode": 200,
        "body": pow(int(event['queryStringParameters']['number1']), 2)+pow(int(event['queryStringParameters']['number2']), 2)
    }
    
    return response

