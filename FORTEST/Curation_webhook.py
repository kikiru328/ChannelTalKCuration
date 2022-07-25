import sys
from flask import Flask, request, Response, render_template
import threading
import json

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/webhook', methods=['GET', 'POST'])

def webhook():

    '''자동화 작업 함수'''
    def auto(content):
        """_summary_

        Args:
            content (str): chat_ID : UserChat ID
            +) Tags : Only for curation
            +) thread : Webhook for flask
            
        """
        import Response        
        import time
        with open('./content_web222.json','w') as file_:
            json.dump(content,file_)
        chat_ID = content.get('entity').get('chatId')
        # print(chat_ID)   
        # print(content.get('entity').get('form'))
        user_name = content.get('refers').get('user')['profile']['name']
        # print(content.get('refers').get('user')['profile']['name'])
        # print(user_name)
        def Introduction(chat_ID,table):
            import requests
            import Functions
            key,pwd = Functions.API_keys()
            headers = {
                'accept': 'application/json',
                # Already added when you pass json=
                # 'Content-Type': 'application/json',
                'x-access-key': f'{key}',
                'x-access-secret': f'{pwd}',
            }
            
            json_data = {
                'blocks': [
                    {
                        'type': 'text',
                        'value': f':bulb: {table}'
                    }
                    ]
                } 
            response = requests.post(f'https://api.channel.io/open/v5/user-chats/{chat_ID}/messages', headers=headers, json=json_data)        
        def Introduction2(chat_ID,table):
            import requests
            import Functions
            key,pwd = Functions.API_keys()
            headers = {
                'accept': 'application/json',
                # Already added when you pass json=
                # 'Content-Type': 'application/json',
                'x-access-key': f'{key}',
                'x-access-secret': f'{pwd}',
            }
            
            json_data = {
                'blocks': [
                    {
                        'type': 'text',
                        'value': f':bulb: {table}'
                    }
                    ]
                } 
            response = requests.post(f'https://api.channel.io/open/v5/user-chats/{chat_ID}/messages', headers=headers, json=json_data)        
        # print(content.get('refers').get('user')['profile'].get('table'))           
        if content.get('entity').get('form').get('inputs')[0].get('label') == f'{user_name}의 성공적인 다이어트를 위해 윤식단이 선물을 준비했어요 받으시겠습니까?' :
            import time
            time.sleep(5)
            
            import requests

            headers = {
                'accept': 'application/json',
                'x-access-key': '62ccfab81187f805e611',
                'x-access-secret': 'f2d2467a158db5b42a2757f79d1477d5',
            }

            params = {
                'sortOrder': 'desc',
                'limit': '1',
            }

            response = requests.get(f'https://api.channel.io/open/v5/user-chats/{chat_ID}/messages', params=params, headers=headers)
            
            # print(type(response.content))
            contents = response.json()
            # print(contents.keys())
            if contents.get('messages')[0].get('form')['inputs'][0]['value'] == True:
                table = "True"
                Introduction(chat_ID,table)
            elif contents.get('messages')[0].get('form')['inputs'][0]['value'] == False:
                table = 'False'
                Introduction2(chat_ID,table)
            else:
                table = 'None'
                Introduction2(chat_ID,table)
            
                

            # print(e)
            # print('No form')
            
        # if content.get('entity').get('tags') != ['식단큐레이션받기']:
        #     pass
        # else:
        #     chat_ID = content.get('refers').get('message')['chatId'] 
        #     print(chat_ID)
        #     thirdparty = content.get('refers').get('user')['profile']['thirdPartyAgree']
        #     print(thirdparty)
        #     if thirdparty != True:
        #         pass
        #     else:
        #         time.sleep(2)
        #         Response.Introduction(chat_ID) # 분석중 > Simple Text
        #         time.sleep(2)
        #         Response.Personal_Information_BMR(chat_ID, content) # 기본정보 > Functions : BMR_c
        #         time.sleep(2)
        #         Response.Activation_food_amount(chat_ID, content) # 활동량 칼로리 > Functions : BMR_c,activation_c,goal_c,macro_c,activation_r,goal_r
        #         time.sleep(2)
        #         Response.Calories_per_dining(chat_ID,content) # 칼로리 섭취 > Functions : BMR_c,activation_c,goal_c,macro_c,activation_r,goal_r
        #         time.sleep(2)
        #         Response.Hydration(chat_ID,content) # 수분 > Functions : hydrate_response
        #         time.sleep(2)
        #         Response.Dining_Habit(chat_ID,content) # 식사 > Functions : dining_response
        #         time.sleep(2)
        #         Response.Recommendation(chat_ID,content) # 추천 > Functions : Recommendation
        #         time.sleep(2)
        #         Response.Recommendation_Link(chat_ID,content) # 추천링크 > Functions : Recommendation for Link ( fifith_block + )
        #         time.sleep(2)
        #         Response.Dining_Schedule(chat_ID,content) # 식단표 > Fucntions : table
        #         time.sleep(2)
        #         Response.Final_Introduction(chat_ID) # 마무리 > Functions :  X 
                
    if request.method == 'GET':
        content = request.args.to_dict()
    elif request.method == 'POST':
        if request.is_json is True:  # Content-Type: json
            content = request.get_json()
        else:  # Content-Type: x-www-form-urlencoded
            content = request.form.to_dict()

    '''스레드 실행'''
    thread = threading.Thread(target=auto, kwargs={'content': content})
    thread.start()

    return 'Success!'


if __name__ == '__main__':
    app.run(port=82, debug=True)