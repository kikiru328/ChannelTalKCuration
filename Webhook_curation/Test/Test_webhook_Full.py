from flask import Flask, request, Response
import threading
import json

app = Flask(__name__)
@app.route('/')
def background():
    print('Success')
    return 'Test webhook for full response'

@app.route('/webhook', methods=['GET','POST'])

def webhook():
    """ Auto code """
    def auto(content):
        import Test
        import time
        """_summary_

        Args:
            content (json) : Auto code for total one step
        """
        chat_ID = content.get('refers').get('message')['chatId']
        print(chat_ID)
        thirdparty = content.get('refers').get('user')['profile']['thirdPartyAgree']
        print(thirdparty)
        if thirdparty != True:
            pass
        else:
            time.sleep(2)
            Test.total_block(chat_ID, content)
            
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