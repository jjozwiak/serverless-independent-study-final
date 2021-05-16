import json
import copy
import logging

class BaseProvider:
    def __init__(self):
        print('Generic platform initialized')
    
    def getRouteParam(self, event, key):
        return ''

    def getQueryStringParam(self, event, key):
        return ''
    
    def getPostData(self, event, key):
        return ''

    def buildResponse():
        return ''


class AzureProvider(BaseProvider):
    
    def __init__(self):
        print('Azure platform initialized')

    def getRouteParam(self, event, key):
        return event.route_params.get(key)

    def getQueryStringParam(self, event, key):
        title = event.params.get(key)
        if title is None:
            return ''
        else:
            return title

    def getPostData(self, event, key):
        data = event.get_json()
        return data[key]

    def buildResponse(self, body):
        response = {
            "body" : json.dumps(body)
        }
        return json.dumps(response)

class AWSProvider(BaseProvider):

    def __init__(self):
        print('AWS platform initialized')

    def getRouteParam(self, event, key):
        return event['pathParameters'][key]

    def getQueryStringParam(self, event, key):
        if 'queryStringParameters' in event and 'title' in event['queryStringParameters']:
            return event['queryStringParameters'][key]
        else:
            return ''

    def getPostData(self, event, key):
        data = json.loads(event['body'])
        if (key == 'body'):
            return copy.deepcopy(data)
        else:
            return copy.deepcopy(data[key])

    def buildResponse(self, body):
        response = {
            "statusCode" : 200,
            "headers" : {
                'Access-Control-Allow-Origin': '*'
            },
            "body" : json.dumps(body)
        }
        return response
