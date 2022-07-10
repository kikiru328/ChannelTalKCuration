import requests
import json
webhook_url = 'http://127.0.0.1:5000/webhook?token=7061f506cfa8e84f3da352e7490851fd'
# POST https://YOUR_SERVER_ENDPOINT/PATH?token=TOKEN_VALUE
data = {'name':'bred',
        'channel_url':'test url'}
r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type':'application/json'})


