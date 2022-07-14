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
        import Util        
        import time
        with open('./content.json','w') as file_:
            json.dump(content,file_)
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
                Util.Processing(chat_ID) # 분석중
                time.sleep(2)
                Util.first_block(chat_ID, content) # 기본정보
                time.sleep(2)
                Util.second_block(chat_ID, content) # 활동량 칼로리
                time.sleep(2)
                Util.second_1_block(chat_ID,content) # 칼로리 섭취
                time.sleep(2)
                Util.third_block(chat_ID,content) # 수분
                time.sleep(2)
                Util.fourth_block(chat_ID,content) # 식사
                time.sleep(2)
                Util.fifith_block(chat_ID,content) # 추천
                time.sleep(2)
                Util.recommend_url(chat_ID,content) # 추천링크
                time.sleep(2)
                Util.image_block(chat_ID,content) # 식단표
                time.sleep(2)
                Util.final_block(chat_ID) # 마무리
                
        
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
    # app.run(port=80, debug=True)
    app.run(port=80, debug=True)