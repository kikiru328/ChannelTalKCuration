

def GET_MSG(chat_ID,post_type):
    import second_function as Functions
    key,pwd = Functions.API_keys()
    import requests
    headers = {
        'accept': 'application/json',
        'x-access-key': f'{key}',
        'x-access-secret': f'{pwd}',
    }

    params = {
        'sortOrder': 'desc',
        'limit': '1',
    }

    response = requests.get(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', params=params, headers=headers)
    return response




# def Introduction(chat_ID,content,post_type):
#     """_summary_

#     Args:
#         chat_ID (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
#         post_type (str) : groups : post message to groups
#     """
#     import requests
    
#     import second_function as Functions
#     key,pwd = Functions.API_keys()
#     headers = {
#         'accept': 'application/json',
#         # Already added when you pass json=
#         # 'Content-Type': 'application/json',
#         'x-access-key': f'{key}',
#         'x-access-secret': f'{pwd}',
#     }
#     user_name = content.get('refers').get('user')['profile']['name']
#     user_goal = content.get('refers').get('user')['profile']['goal']
#     if  '이상의 감량을' in user_goal : user_goal= '<b>5Kg 이상 감량</b>을'
#     elif '5Kg 미만' in user_goal : user_goal= '<b>5Kg 미만 감량</b>을'
#     elif '증량' in user_goal : user_goal= '<b>5Kg 이상 증량</b>을'
#     else: user_goal= '<b>유지</b>를'

#     json_data = {
#         'blocks': [
#             {
#               "type" : "text",
#               "value": ":banana: :sweet_potato: :rice: :cut_of_meat: :meat_on_bone: :chicken:"
#             },
#             {
#               "type" : "text",
#               "value": ":clipboard:\n<b>[아무개]</b>님의\n<b>성공적인 식단 관리</b>를 위해\n<b>한 끼 섭취량 </b>을 알려드릴게요!"  
#             },
#             {
#               "type" : "text",
#               "value": ":relaxed:\n목적이 같다고 해서\n<b>가는 길이 같을 필요는 없어요!</b>\n\n<b>체중 유지라는 나의 목적</b>과\n상황을 고려한 <b>식단</b>\n\n<b>나에게 필요한 영양소</b>를\n고려한 <b>식단</b>으로 관리를 하면\n\n<b>폭식, 과식</b>을 예방할 수 있고\n충분한 <b>영양공급</b>으로\n\n<b>요요없이</b>, 원하는 체중으로\n오래 유지할 수 있어요. :+1:"  
#             },
#             {
#               "type" : "text",
#               "value": ":anguished:\n이렇게 <b>아무개</b>님에게\n<b>맞지 않는</b><b>식사</b>를 지속한다면\n\n<b>부족한 영양 공급</b>으로 인해\n<b>요요</b>,<b>과식</b>,<b>폭식</b> 등의\n\n다이어트 <b>부작용</b>을 만날\n<b>가능성</b>이 무려 <b>89%이상</b>이에요!:fearful:"  
#             },
#             {
#               "type" : "text",
#               "value": ":question:\n아무개님은 현재 <b>식단관리</b>를\n<b>어떻게</b> 하고 있으세요?\n\n인터넷에 검색?\n유튜브를 찾아서?\n\n시중에 판매되는 <b>대부분</b>의\n<b>샐러드</b>, <b>다이어트 도시락</b>은\n\n<b>양</b>을 줄이거나, <b>칼로리</b>만 줄여\n제공하고 있어요:cry:"  
#             },
#             {
#               "type" : "text",
#               "value": ":muscle:\n2015년부터 현재까지\n<b>트레이너</b>로 활동하면서\n<b>1,000명 이상</b>의 회원님들의\n<b>식단과 건강관리</b>를 도와드렸고\n지금까지 총 <b>2,000Kg</b> 이상의 \n<b>지방 감량</b>에 성공했어요!"
#             },
#             {
#               "type" : "text",
#               "value": ":raised_hands: <b>아무개님</b>의 <b>식단</b>을 설명해드리기 전\n    짧게 제 <b>이력</b>을 소개할게요!"
#             },
#             {
#               'type':'text',
#               "value": ":health_worker:\n<b>안녕하세요!</b>\n윤식단 식단 관리 팀장 <b>'제니'</b>입니다!:clap:"
#             },
#             {
#                 'type': 'text',
#                 'value': f':gift: <b>[{user_name}]님</b>의 <b>성공적인 다이어트</b>에\n    도움이 되는 <b>식단표</b>를\n    <b>선물</b>로 드릴게요!.\n\n'
#             }, # 나누기.
#             {
#                 'type' : 'text',
#                 'value' : '":sunglasses: <b>8년</b>간의 노하우와 데이터로 만든\n    <b>가장 성공 확률이 높은</b>\n    <b>식단표</b>에요!\n\n"'
#             }, # 나누기
#             {
#                 'type' : 'text',
#                 'value' : f":trophy: <b>식단표</b>를 잘 활용한다면 <b>3개월 이내</b>\n    {user_goal} 달성할 수 있어요!"
#             }, # 나누기
#             {
#                 'type' : 'text',
#                 'value' : f":crossed_fingers: <b>윤식단이 {user_name}님의\n    {user_goal[:-1]} 성공을 응원해요!"
#             },
#             {
#                 'type':'text',
#                 'value' : ":ticket: 오늘 <b>22시까지 주문시</b>\n    단돈 <b>6,800원</b>으로\n    <b>1:1 맞춤 식단</b>을 체험해보세요!"
#             },
#             {
#                 'type':'text',
#                 'value':":seedling: <b>[건강 관리의 시작은]</b>\n    '<b>내일</b>'이 아닌\n    '<b>지금</b>'시작해야 <b>성공</b>합니다."
#             },
#             ],
        
#         "blocks": [
#             {
#                 "type": "text",
#                 "value": "      :corn: <b>맞춤 식단 바로 주문하기</b>   "
#             }
#             ],
#         "buttons": [
#             {
#                 "title": "이벤트 맞춤 식단 프로그램 ",
#                 "colorVariant": "green",
#                 "url": "https://yundiet.com/shop_view/?idx=48"
#             }
#             ],
#         "blocks": [
#             {
#                 "type": "text",
#                 "value": "      :corn: <b>맞춤 식단 바로 주문하기</b>   "
#             }
#             ],
#     "buttons": [
#             {
#                 "title": "윤식단 맞춤 식단 프로그램 ",
#                 "colorVariant": "green",
#                 "url": "https://yundiet.com/store_all/?idx=66"
#             }
#             ]
#         } 
#     response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data) 
    
    
    
    
    
                                                                                                            
 ####     ####    ##  ##   ######   ####     ##  ##   ##       ######  
##       ##  ##   ##  ##   ##       ## ##    ##  ##   ##       ##      
 ####    ##       ######   ####     ##  ##   ##  ##   ##       ####    
    ##   ##       ##  ##   ##       ##  ##   ##  ##   ##       ##      
    ##   ##  ##   ##  ##   ##       ## ##    ##  ##   ##       ##      
 ####     ####    ##  ##   ######   ####      ####    ######   ######  
                                                                                                            

def Dining_Schedule(chat_ID,content,post_type):
    import requests
    import second_function as Functions
    key,pwd = Functions.API_keys()
    headers = {
        'accept': 'application/json',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'x-access-key': f'{key}',
        'x-access-secret': f'{pwd}',
    }
    
    user_goal = content.get('refers').get('user')['profile']['goal']
    user_name = content.get('refers').get('user')['profile']['name']
    # print(user_goal)
    json_data={
        'blocks':[
            {
                'type':'text',
                'value':f":calendar: <b>[{user_name}]님</b>에 맞춘\n     <b>맞춤 식단표</b>에요!:v:"
            }
        ],
        'buttons':[
            {   
                'title':'맞춤 식단표 받기',
                "colorVariant": "orange",  
                "url": Functions.table(user_goal)                                      
            }
        ]
    }
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)    
#############################################################################################

                                                                                   
 ######   ######   ##  ##     ##     ##                ######   ##  ##   ######   #####     ####   
 ##         ##     ### ##    ####    ##                  ##     ### ##     ##     ##  ##   ##  ##  
 ####       ##     ######   ##  ##   ##                  ##     ######     ##     ##  ##   ##  ##  
 ##         ##     ## ###   ##  ##   ##                  ##     ## ###     ##     #####    ##  ##  
 ##         ##     ##  ##   ######   ##                  ##     ##  ##     ##     ## ##    ##  ##  
 ##       ######   ##  ##   ##  ##   ######            ######   ##  ##     ##     ##  ##    ####   
                                                                                                   

def Final_Introduction(chat_ID,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] 
    """
    import requests
    import second_function as Functions
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
                'type':'text',
                'value':':herb:\n'
            },
            {
                'type': 'text',
                'value': '나에게 맞지 않는 식단은\n나에게 맞지 않는 옷과 같아요.\n\n요요가 생기거나, 폭식을 하거나\n과도한 스트레스를 받는 문제가\n발생해요.\n\n영양소의 과다 공급을\n점진적으로 줄여가며\n나에게 맞는 식단 관리를 시작하면\n부작용 없이 건강한 내 모습을\n만나 볼 수 있을거에요.\n\n'
            },
            {
                'type' : 'text',
                'value': '건강을 관리하는 것은\n벽돌을 쌓는 것과 같아요.\n\n조금 느리더라도 단단하게 쌓아\n무너지지 않게 하는 것이\n가장 중요하죠.\n\n체중을 빨리 감량하는 것 보다,\n감량한 체중을 오래 유지하는 것이\n더욱 중요합니다.\n\n건강관리, 아직 늦지 않았어요.\n<b>윤식단</b>과 함께 지금부터라도\n시작해 보세요!:grinning:'
            }
            ]
        } 
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)    
    
    
    
def present(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """
    import requests
    
    import second_function as Functions
    key,pwd = Functions.API_keys()
    headers = {
        'accept': 'application/json',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'x-access-key': f'{key}',
        'x-access-secret': f'{pwd}',
    }
    user_name = content.get('refers').get('user')['profile']['name']
    json_data = {
        "blocks" : [
            {
                'type': 'text',
                'value': f':gift: <b>[{user_name}]님</b>의 <b>성공적인 다이어트</b>에\n    도움이 되는 <b>식단표</b>를\n    <b>선물</b>로 드릴게요!.\n\n'
            }   
        ]
        }
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data) 
    
    
def knowhow(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """
    import requests
    
    import second_function as Functions
    key,pwd = Functions.API_keys()
    headers = {
        'accept': 'application/json',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'x-access-key': f'{key}',
        'x-access-secret': f'{pwd}',
    }
    json_data = {
        "blocks" : [
            {
                'type' : 'text',
                'value' : ':sunglasses: <b>8년</b>간의 노하우와 데이터로 만든\n    <b>가장 성공 확률이 높은</b>\n    <b>식단표</b>에요!'
            }  
        ]
        }
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)     
    
def goal_success(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """
    import requests
    
    import second_function as Functions
    key,pwd = Functions.API_keys()
    headers = {
        'accept': 'application/json',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'x-access-key': f'{key}',
        'x-access-secret': f'{pwd}',
    }
    user_goal = content.get('refers').get('user')['profile']['goal']
    if  '이상의 감량을' in user_goal : user_goal= '<b>5Kg 이상 감량</b>을'
    elif '5Kg 미만' in user_goal : user_goal= '<b>5Kg 미만 감량</b>을'
    elif '증량' in user_goal : user_goal= '<b>5Kg 이상 증량</b>을'
    else: user_goal= '<b>유지</b>를'
    json_data = {
        "blocks" : [
            {
                'type' : 'text',
                'value' : f":trophy: <b>식단표</b>를 잘 활용한다면 <b>3개월 이내</b>\n    {user_goal} 달성할 수 있어요!"
            }  
        ]
        }
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)     
    
def yun_cheer(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """
    import requests
    
    import second_function as Functions
    key,pwd = Functions.API_keys()
    headers = {
        'accept': 'application/json',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'x-access-key': f'{key}',
        'x-access-secret': f'{pwd}',
    }
    user_goal = content.get('refers').get('user')['profile']['goal']
    
    if  '이상의 감량을' in user_goal : user_goal= '<b>5Kg 이상 감량</b>'
    elif '5Kg 미만' in user_goal : user_goal= '<b>5Kg 미만 감량</b>'
    elif '증량' in user_goal : user_goal= '<b>5Kg 이상 증량</b>'
    else: user_goal= '<b>유지</b>'

    user_name = content.get('refers').get('user')['profile']['name']
    json_data = {
        "blocks" : [
            {
                'type' : 'text',
                'value' : f":crossed_fingers: <b>윤식단이 [{user_name}]님의\n    {user_goal} 성공을 응원해요!"
            }
        ]
        }
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data) 
    
def marketing(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """
    import requests
    
    import second_function as Functions
    key,pwd = Functions.API_keys()
    headers = {
        'accept': 'application/json',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'x-access-key': f'{key}',
        'x-access-secret': f'{pwd}',
    }
    user_goal = content.get('refers').get('user')['profile']['goal']
    user_name = content.get('refers').get('user')['profile']['name']
    json_data = {
        "blocks" : [
            {
                'type':'text',
                'value' : ":ticket: 오늘 <b>22시까지 주문시</b>\n    단돈 <b>6,800원</b>으로\n    <b>1:1 맞춤 식단</b>을 체험해보세요!"
            }
        ]
        }
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)        
    
def last_quote(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """
    import requests
    
    import second_function as Functions
    key,pwd = Functions.API_keys()
    headers = {
        'accept': 'application/json',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'x-access-key': f'{key}',
        'x-access-secret': f'{pwd}',
    }
    user_goal = content.get('refers').get('user')['profile']['goal']
    user_name = content.get('refers').get('user')['profile']['name']
    json_data = {
        "blocks" : [
            {
                'type':'text',
                'value':":seedling: <b>[건강 관리의 시작은]</b>\n    '<b>내일</b>'이 아닌\n    '<b>지금</b>'시작해야 <b>성공</b>합니다."
            }
        ]
        }
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)              
    
def event_salad(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """
    import requests
    
    import second_function as Functions
    key,pwd = Functions.API_keys()
    headers = {
        'accept': 'application/json',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'x-access-key': f'{key}',
        'x-access-secret': f'{pwd}',
    }
    user_goal = content.get('refers').get('user')['profile']['goal']
    user_name = content.get('refers').get('user')['profile']['name']
    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": "      :corn: <b>맞춤 식단 바로 주문하기</b>   "
            }
            ],
        "buttons": [
            {
                "title": "[이벤트] 맞춤 식단 프로그램 ",
                "colorVariant": "green",
                "url": "https://yundiet.com/shop_view/?idx=48"
            }
            ]
        }
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)      
    
    
    
def normal_salad(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """
    import requests
    
    
    import second_function as Functions
    key,pwd = Functions.API_keys()
    headers = {
        'accept': 'application/json',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'x-access-key': f'{key}',
        'x-access-secret': f'{pwd}',
    }
    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": "      :corn: <b>맞춤 식단 바로 주문하기</b>   "
            }
            ],
        "buttons": [
            {
                "title": "윤식단 맞춤 식단 프로그램 ",
                "colorVariant": "green",
                "url": "https://yundiet.com/store_all/?idx=66"
            }
            ]
        }
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)      