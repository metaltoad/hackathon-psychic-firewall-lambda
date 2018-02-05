
import boto3
import json

print('Loading function')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
    }


def lambda_handler(event, context):

    operation = event['httpMethod']
    if operation == 'POST':

        # return respond(None, event)

        input = json.loads(event['body'])
        text = input['text']

        comprehend = boto3.client(service_name='comprehend', region_name='us-west-2')

        result = {}
        result['entities'] = comprehend.detect_entities(Text=text, LanguageCode='en')
        result['sentiment'] = comprehend.detect_sentiment(Text=text, LanguageCode='en')


        return respond(None, result)
