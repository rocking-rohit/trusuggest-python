import requests
import json


def upload(accessToken, indexName, uploadData):
    url = 'https://api.trusuggest.com/dev/index/upload'
    payload = {
        'indexName':indexName,
        'uploadData':uploadData
    }
    headers = {'content-type': 'application/json','Authorization': 'Bearer '+accessToken}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    response_status = r.status_code
    response_message = 'Error with server'
    if response_status == 200:
        response_message = json.loads(r._content)['message']
        return {'message':response_message, 'success': 'true', 'status':response_status}
    else:
        return {'message':'Some Thing Went Wrong', 'success': 'false', 'status':response_status}

def bulkUpload(accessToken, indexName, uploadData):
    url = 'https://api.trusuggest.com/dev/index/bulk-upload'
    payload = {
        'indexName':indexName,
        'uploadData':uploadData
    }
    headers = {'content-type': 'application/json','Authorization': 'Bearer '+accessToken}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    response_status = r.status_code
    response_message = 'Error with server'
    if response_status == 200:
        size = json.loads(r._content)['data']['size']
        response_message = json.loads(r._content)['message']
        if size > 50:
            return {'message':response_message, 'success': 'false', 'status':response_status}
        return {'message':response_message, 'success': 'true', 'status':response_status}
    else:
        return {'message':'Some Thing Went Wrong', 'success': 'false', 'status':response_status}

    