from flask import Flask
app = Flask(__name__)
@app.route('/')
# def home():
#     return 'Hello, World!'
def get_id():
    import requests
    headers = {
        'accept': 'application/json',
        'x-access-key': '62c7984897721f282db3',
        'x-access-secret': 'ef5f908abc1a0d2dfadeac988dd8cef2',
    }

    params = {
        'state': 'opened',
        'sortOrder': 'desc',
        'limit': '100',
    }

    response = requests.get('https://api.channel.io/open/v5/user-chats', params=params, headers=headers)
    chats = response.json().get('userChats')
    test_id = chats[0].get('id')
    return test_id

def home():
    test_id = get_id()
    return test_id

if __name__ == '__main__':
    app.run(debug=True)