from flask import Flask, request, Response
import threading
import json

app = Flask(__name__)
@app.route('/')
def hello_world():
    print('Success!')
    return 'Hello World!'

@app.route('/webhook', methods=['GET', 'POST'])

def webhook():

    '''자동화 작업 함수'''
    def auto(content):

        with open(f'content.json','w',encoding='UTF-8-sig') as file_:
            json.dump(content,file_,ensure_ascii = False,indent=4)
            # file_.write('\n')
    

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