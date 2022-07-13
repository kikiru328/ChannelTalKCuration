import sys
from flask import Flask, request, Response, render_template
import threading
import json

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html", image_file='식단표.png')

@app.route('/webhook', methods=['GET', 'POST'])

def webhook():

    '''자동화 작업 함수'''
    def auto(content):
        import Util        
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
                Util.first_block(chat_ID, content)
                time.sleep(2)
                Util.second_block(chat_ID, content)
                time.sleep(0.5)
                Util.second_1_block(chat_ID,content)
                time.sleep(2)
                Util.third_block(chat_ID,content)
                time.sleep(2)
                Util.fourth_block(chat_ID,content)
                time.sleep(2)
                Util.fifith_block(chat_ID,content)
                time.sleep(2)
                Util.final_block(chat_ID)
                time.sleep(1)
                Util.image_block(chat_ID)
        
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