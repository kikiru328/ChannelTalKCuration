class User:
    def __init__(self):
        self.test_id = self.get_id()
        self.curation()
        
    def get_id(self):
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


    def curation(test_id):
        return print(test_id)