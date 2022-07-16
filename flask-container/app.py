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
        # with open('./content.json','w') as file_:
        #     json.dump(content,file_)
        if content.get('entity').get('tags') != ['식단큐레이션받기']:
            pass
        else:
            chat_ID = content.get('refers').get('message')['chatId'] 
            print(chat_ID)
            thirdparty = content.get('refers').get('user')['profile']['thirdPartyAgree']
            print(thirdparty)
            if thirdparty != True:
                pass
            else:
                time.sleep(2)
                Response.Introduction(chat_ID) # 분석중 > Simple Text
                time.sleep(2)
                Response.Personal_Information_BMR(chat_ID, content) # 기본정보 > Functions : BMR_c
                time.sleep(2)
                Response.Activation_food_amount(chat_ID, content) # 활동량 칼로리 > Functions : BMR_c,activation_c,goal_c,macro_c,activation_r,goal_r
                time.sleep(2)
                Response.Calories_per_dining(chat_ID,content) # 칼로리 섭취 > Functions : BMR_c,activation_c,goal_c,macro_c,activation_r,goal_r
                time.sleep(2)
                Response.Hydration(chat_ID,content) # 수분 > Functions : hydrate_response
                time.sleep(2)
                Response.Dining_Habit(chat_ID,content) # 식사 > Functions : dining_response
                time.sleep(2)
                Response.Recommendation(chat_ID,content) # 추천 > Functions : Recommendation
                time.sleep(2)
                Response.Recommendation_Link(chat_ID,content) # 추천링크 > Functions : Recommendation for Link ( fifith_block + )
                time.sleep(2)
                Response.Dining_Schedule(chat_ID,content) # 식단표 > Fucntions : table
                time.sleep(2)
                Response.Final_Introduction(chat_ID) # 마무리 > Functions :  X 
                
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
    app.run(port=80, debug=True)

