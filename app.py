from flask import Flask, request, render_template, jsonify
import threading
import json

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/main_curation', methods=['GET', 'POST'])

def main_curation():
    
    '''자동화 작업 함수'''
    def auto(content):
        """_summary_

        Args:
            content (str): chat_ID : UserChat ID
            +) Tags : Only for curation
            +) thread : Webhook for flask
            
        """
        import main_response
        import time
        if (content['entity']['source']['supportBot']['id']=='51767') and (content['entity']['tags'][0] == '식단큐레이션받기'):
            print('############################        DEFINE_CURATION       ############################')
            chat_ID = content.get('refers').get('message')['chatId'] 
            post_type = 'user-chats' 
            thirdparty = content.get('refers')\
                            .get('user')['profile']['thirdPartyAgree']
            if thirdparty != True:
                pass
            else:
                time.sleep(2)
                main_response.Introduction1(chat_ID,content,post_type) 
                time.sleep(2)
                main_response.Introduction2(chat_ID,content,post_type) 
                time.sleep(2)
                main_response.Introduction3(chat_ID,content,post_type) 
                time.sleep(2)
                main_response.Introduction4(chat_ID,content,post_type)
                time.sleep(2)
                main_response.Introduction5(chat_ID,content,post_type)
                time.sleep(2)
                main_response.Introduction6(chat_ID,content,post_type)
                time.sleep(2)
                main_response.Introduction7(chat_ID,content,post_type) 
                time.sleep(2)
                main_response.Activation_food_amount(chat_ID,content,post_type)
                time.sleep(2)
                main_response.Calories_per_dining(chat_ID,content,post_type) 
                time.sleep(2)
                main_response.Before_form(chat_ID,content,post_type)
                time.sleep(2)
                main_response.RESET(chat_ID,content,post_type)
            
        elif (content['entity']['source']['supportBot']['id']=='43684') and (content['entity']['tags'][0] == '식단큐레이션받기'): ## Normal
            chat_ID = content.get('refers').get('message')['chatId'] 
            # chat_ID = '@%ED%81%90%EB%A0%88%EC%9D%B4%EC%85%98%EC%83%81%EB%8B%B4'
            post_type = 'user-chats' 
            thirdparty = content.get('refers')\
                            .get('user')['profile']['thirdPartyAgree']
            print(thirdparty)
            if thirdparty != True:
                pass
            else:
                time.sleep(2)
                main_response.Introduction1(chat_ID,content,post_type) 
                time.sleep(2)
                main_response.Introduction2(chat_ID,content,post_type) 
                time.sleep(2)
                main_response.Introduction3(chat_ID,content,post_type) 
                time.sleep(2)
                main_response.Introduction4(chat_ID,content,post_type)
                time.sleep(2)
                main_response.Introduction5(chat_ID,content,post_type)
                time.sleep(2)
                main_response.Introduction6(chat_ID,content,post_type)
                time.sleep(2)
                main_response.Introduction7(chat_ID,content,post_type) 
                time.sleep(2)
                main_response.Activation_food_amount(chat_ID,content,post_type)
                time.sleep(2)
                main_response.Calories_per_dining(chat_ID,content,post_type) 
                time.sleep(2)
                main_response.Before_form(chat_ID,content,post_type)
                time.sleep(2)
                main_response.RESET(chat_ID,content,post_type)
        else:
            print(f'\n##############################        CANNOT RESPONSE CONTENTS        ##############################\n')
            print(content['entity']['source']['supportBot']['id'])
            print(content['entity']['tags'])
            


                
    if request.method == 'GET':
        content = request.args.to_dict()
    elif request.method == 'POST':
        if request.is_json is True:  
            content = request.get_json()
        else:
            content = request.form.to_dict()

    '''스레드 실행'''
    thread = threading.Thread(target=auto, kwargs={'content': content})
    thread.start()

    return 'main_curation successfully operated'


@app.route('/curation_presents', methods=['GET', 'POST'])

def curation_present():

    '''자동화 작업 함수'''
    def auto(content):
        # print('<<<<<<<<<<', content)
        """_summary_

        Args:
            content (str): chat_ID : UserChat ID
            +) Tags : Only for curation
            +) thread : Webhook for flask
            
        """
        import time
        import present_response
        chat_ID = content['entity']['chatId']
        post_type = 'user-chats'
        try:
            user_name = content['refers']['user']['profile']['name']
        except:
            pass

        try:
            if content['refers']['userChat']['source']['supportBot']['id'] == '51767':
                print('############################        DEFINE_CURATION_ PRESENT       ############################')
                if content['entity']['form']['inputs'][0]['label'] == "받으시겠어요?" : 
                    print('YES')
                    import time
                    time.sleep(5)
                    chat_ID = content['entity']['chatId']

                    post_type = 'user-chats' 
                    
                    import present_response
            
                    response = present_response.GET_MSG(chat_ID,post_type)    
                    contents = json.loads(response.content)
                    
                    try:
                        if contents['messages'][0]['form']['inputs'][0]['value']\
                                                == True:
                            print('TRUE')
                            import time
                            time.sleep(2)
                            present_response.present(chat_ID,content,post_type)
                            print('present')
                            time.sleep(2)
                            present_response.knowhow(chat_ID,content,post_type)
                            print('knowhow')
                            time.sleep(2)
                            present_response.Dining_Schedule(chat_ID,content,post_type)
                            print('ds')
                            time.sleep(2)
                            present_response.goal_success(chat_ID,content,post_type)
                            print('suc')
                            time.sleep(2)
                            present_response.yun_cheer(chat_ID,content,post_type)
                            print('ch')
                            time.sleep(2)
                            present_response.marketing(chat_ID,content,post_type)
                            print('ma')
                            time.sleep(2)
                            present_response.last_quote(chat_ID,content,post_type)
                            print('lq')
                            time.sleep(2)
                            present_response.event_salad(chat_ID,content,post_type)
                            print('ev')
                            time.sleep(2)
                            present_response.Final_Introduction(chat_ID,post_type)
                            
                        elif contents['messages'][0]['form']['inputs'][0]['value'] \
                                                    == False:
                            print('False')
                            time.sleep(2)
                            present_response.Final_Introduction(chat_ID,post_type)
                            print('fi')
                            time.sleep(1)
                            present_response.normal_salad(chat_ID,content,post_type)
                            print('False')
                    except Exception as e:
                        print(e)
                        time.sleep(2)
                        present_response.Final_Introduction(chat_ID,post_type)
                        print('fi')
                        time.sleep(1)
                        present_response.normal_salad(chat_ID,content,post_type)
                                            
            elif content['refers']['userChat']['source']['supportBot']['id'] == '43684':
                if content['entity']['form']['inputs'][0]['label'] == "받으시겠어요?" : 
                    print('YES')
                    import time
                    time.sleep(5)
                    chat_ID = content['entity']['chatId']

                    post_type = 'user-chats' 
                    
                    import present_response
            
                    response = present_response.GET_MSG(chat_ID,post_type)    
                    contents = json.loads(response.content)
                    
                    try:
                        if contents['messages'][0]['form']['inputs'][0]['value']\
                                                == True:
                            print('TRUE')
                            import time
                            time.sleep(2)
                            present_response.present(chat_ID,content,post_type)
                            print('present')
                            time.sleep(2)
                            present_response.knowhow(chat_ID,content,post_type)
                            print('knowhow')
                            time.sleep(2)
                            present_response.Dining_Schedule(chat_ID,content,post_type)
                            print('ds')
                            time.sleep(2)
                            present_response.goal_success(chat_ID,content,post_type)
                            print('suc')
                            time.sleep(2)
                            present_response.yun_cheer(chat_ID,content,post_type)
                            print('ch')
                            time.sleep(2)
                            present_response.marketing(chat_ID,content,post_type)
                            print('ma')
                            time.sleep(2)
                            present_response.last_quote(chat_ID,content,post_type)
                            print('lq')
                            time.sleep(2)
                            present_response.event_salad(chat_ID,content,post_type)
                            print('ev')
                            time.sleep(2)
                            present_response.Final_Introduction(chat_ID,post_type)
                            
                        elif contents['messages'][0]['form']['inputs'][0]['value'] \
                                                    == False:
                            print('False')
                            time.sleep(2)
                            present_response.Final_Introduction(chat_ID,post_type)
                            print('fi')
                            time.sleep(1)
                            present_response.normal_salad(chat_ID,content,post_type)
                            print('False')
                    except Exception as e:
                        print(e)
                        time.sleep(2)
                        present_response.Final_Introduction(chat_ID,post_type)
                        print('fi')
                        time.sleep(1)
                        present_response.normal_salad(chat_ID,content,post_type)

            else:
                print(content['entity']['form']['inputs'][0]['label'])

        except Exception as e:
            pass
            # print(e)
            # print('PASS')


                
    if request.method == 'GET':
        content = request.args.to_dict()
    elif request.method == 'POST':
        if request.is_json is True: 
            content = request.get_json()
        else:  
            content = request.form.to_dict()

    '''스레드 실행'''
    thread = threading.Thread(target=auto, kwargs={'content': content})
    thread.start()

    return 'curation_presents successfully operated!'


@app.route('/delivery_curation', methods=['GET', 'POST'])
def delivery_():
    def auto(content):
        print('####DELIVERY####', content)
        """_summary_

        Args:
            content (str): chat_ID : UserChat ID
            +) Tags : Only for curation
            +) thread : Webhook for flask
            
        """
        import time
        import present_response
        chat_ID = content['entity']['chatId']
        post_type = 'user-chats'
        import delivery_date
        import datetime
        now = datetime.datetime.now()
        holiday_dataframe = delivery_date.holiday_dataframe
        print('######### NOW ##########', now)
        time.sleep(0.68)
        try:
            if content['refers']['userChat']['source']['supportBot']['id'] == '52853':
                if content['entity']['plainText'] == '새벽배송':
                    delivery_date.get_delivery_start_date_each.get_deliv_start_date(chat_ID, post_type,now,holiday_dataframe,'새벽배송')
                elif content['entity']['plainText'] == '일반배송':
                    delivery_date.get_delivery_start_date_each.get_deliv_start_date(chat_ID, post_type,now,holiday_dataframe,'일반배송')
                elif content['entity']['plainText'] == '직접배송':
                    delivery_date.get_delivery_start_date_each.get_deliv_start_date(chat_ID, post_type,now,holiday_dataframe,'직접배송')    
        except:
            pass
        
    if request.method == 'GET':
        content = request.args.to_dict()
    elif request.method == 'POST':
        if request.is_json is True: 
            content = request.get_json()
        else:  
            content = request.form.to_dict()

    '''스레드 실행'''
    thread = threading.Thread(target=auto, kwargs={'content': content})
    thread.start()

    return 'delivery_curation successfully operated!'



if __name__ == '__main__':
    app.run(port=80, debug=True)

