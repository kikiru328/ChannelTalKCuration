global API_keys
def API_keys():
    import json
    with open('API_key.json','r') as api_json:
       api = json.load(api_json) 
    key = api.get('x-access-key')
    sec = api.get('x-access-secret')
    return key,sec


global BMR_calories_calculation, activation_calories_calculation, goal_calories_calculation, macro_calories_calucation
def BMR_calories_calculation(user_weight, user_height, user_age):

    """_summary_

    Args:
        user_weight (int): content.get('refers').get('user')['profile']['weight']
        user_height (int): content.get('refers').get('user')['profile']['height']
        user_age (int): content.get('refers').get('user')['profile']['age']

    Returns:
        int: BMR : int > activation_calculation parameter ( trunc ) 
    """
    return int(66 + (13.7 * user_weight) + (5 * user_height) -  (6.8 * user_age))


def activation_calories_calculation(user_activation:str,BMR):
    """_summary_

    Args:
        user_activation (str): content.get('refers').get('user')['profile']['activation']
        BMR (int): Calculation by user_profile functions

    Returns:
        int: maintenance : int > goal_calculation parameter ( trunc )
    """
    if user_activation == '거의 없다 (주1회이하)' : return int(BMR * 1.2)
    elif user_activation == '보통 (주2회이상)' : return int(BMR * 1.375)
    elif user_activation == '꽤있다 (주4회)' : return int(BMR * 1.55)
    else : return int(BMR * 1.725)
    
def goal_calories_calculation(user_goal,maintenance):
    """_summary_

    Args:
        user_goal (int): content.get('refers').get('user')['profile']['goal']
        maintenance (int): Calculation by return of activation_calculation functions

    Returns:
        int: goal_calories : int > macro_calucation parameter ( trunc )
    """
    if user_goal == '5Kg 이상의 감량을 원하세요?' : return int(maintenance * 0.8)
    elif user_goal == '5Kg 미만의 감량을 원하세요?' : return int(maintenance * 0.9)
    elif user_goal == '5kg 이상의 증량을 원하세요?' : return int(maintenance * 1.1)
    else: return int(maintenance)
    
def macro_calories_calucation(goal_calories):
    """_summary_

    Args:
        goal_calories (int): Calculation by goal_calculation functions

    Returns:
        _type_: carbon/protein/fat by gram  int ( trunc )
    """
    carbohydrate = int(goal_calories * 0.5 / 4)
    protein = int(goal_calories * 0.3 / 4)
    fat = int(goal_calories * 0.2 / 9)
    return carbohydrate, protein, fat



###### SECOND ########
    
global activation_response, goal_response
def activation_response(user_activation):
    """_summary_

    Args:
        user_activation (str): content.get('refers').get('user')['profile']['activation']

    Returns:
        str : str > second_block
    """
    if user_activation == '거의 없다 (주1회이하)' : return "거의 없으세요.\n\n일주일에 한 번 운동 습관을\n만들어 보는 것은 어떠실까요?"
    elif user_activation == '보통 (주2회이상)' : return "적당합니다.아주 좋습니다!"
    elif user_activation == '꽤있다 (주4회)' : return "꽤 있으시네요. 아주 좋습니다!"
    else: return "많으시군요. 아주 좋습니다!"
    
def goal_response(user_goal):
    """_summary_

    Args:
        user_goal (str): content.get('refers').get('user')['profile']['goal']

    Returns:
        str: str > second_block
    """
    if user_goal == '5Kg 이상의 감량을 원하세요?' : return "<b>[5Kg 이상 감량]</b>을 원하신다고\n답변을 하셨어요!\n\n<b>[5Kg 이상 감량]</b>을 위해서는\n<b>하루 4번</b>의 식사를 권장 드리고 있어요!"
    elif user_goal == '5Kg 미만의 감량을 원하세요?': return "<b>[5kg 미만 감량]</b>을 원한다고\n답변을 하셨어요!\n\n<b>[5kg 미만 감량]</b>을 위해서는\n<b>하루 4번</b>의 식사를 권장 드리고 있어요!"
    elif user_goal == '5Kg 이상의 증량을 원하세요?': return "<b>[5Kg 이상 증량]</b>을 원한다고\n답변을 하셨어요!\n\n<b>[5Kg 이상 증량]</b>을 위해서는\n<b>하루 4번</b>의 식사를 권장 드리고 있어요!"
    else: return "<b>[유지]</b>를 원한다고\n답변을 하셨어요!\n\n<b>[유지]</b>를 위해서는\n<b>하루 4번</b>의 식사를 권장 드리고 있어요!"

###### THIRD ######
global hydrate_response 
def hydrate_response(user_hydrate,user_weight,user_name):
    """_summary_

    Args:
        user_name (str): content.get('refers').get('user')['profile']['name']
        user_hydrate (str): content.get('refers').get('user')['profile']['hydrate']
        user_weight (str): content.get('refers').get('user')['profile']['weight']
        
    Returns:
        str: response str > third_block
    """
    hydration = round(user_weight * 0.03,1)
    if user_hydrate == '500ml 이하' : return f'<b>[수분{hydration}L]</b>가 <b>[{user_name}]</b>님의\n하루 수분 섭취량이에요.\n\n현재 심각한 수분 부족 상태로,\n충분한 수분 보충을 권장 드립니다!\n\n처음부터 너무 많은 양의 물을 섭취하는 것이 부담스러우시다면\n<b>하루 "1L"</b>섭취로 점진적으로\n시작해 보세요!\n\n'
    elif user_hydrate == '1L 이하' : return f'<b>[수분{hydration}L]</b>가 <b>[{user_name}]</b>님의\n하루 수분 섭취량이에요.\n\n현재 심각한 수분 부족 상태로,\n충분한 수분 보충을 권장 드립니다!\n\n처음부터 너무 많은 양의 물을 섭취하는 것이 부담스러우시다면\n<b>하루 "1.5L"</b>섭취로 점진적으로\n시작해 보세요!\n\n'
    elif user_hydrate == '1.5L 이하' : return f'<b>[수분{hydration}L]</b>가 <b>[{user_name}]</b>님의\n하루 수분 섭취량이에요.\n\n조금만 더 수분 보충에 신경 써주신다면\n더욱 좋은 몸의 상태를 유지할 수 있을 거예요!\n\n'
    else: return f'<b>[수분{hydration}L]</b>가 <b>[{user_name}]</b>님의\n하루 수분 섭취량이에요.\n\n현재 수분 보충을 열심히 하시는 것 같아요!\n나에게 맞는 섭취량을 정확히 알아가며\n더욱 좋은 몸의 컨디션을 만들어보세요!\n\n'



##### FOURTH #####
global dining_response
def dining_response(user_dining):
    """_summary_

    Args:
        user_dining (str): content.get('refers').get('user')['profile']['number_dining']

    Returns:
        str: response str > fourth_block
    """
    if user_dining == '1회':
        return '<b>에너지 섭취 관리가 필요해요!</b>\n식사는 <b>3~5시간에 한 번씩</b>\n섭취를 해주는 것이 가장 좋아요!\n\n07시 / 12시 / 16시 / 19시 이런 방식으로요!\n\n1시간 동안 에너지로\n흡수할 수 있는 양은 정해져있어요\n\n한 번에 많은 양을 섭취하면\n흡수되지 못한 양의 에너지가\n지방으로 전환돼요\n\n또 한 대사율이 떨어져\n<b>살이 찌는 체질</b>로 변하게 돼요.'
    elif user_dining == '2회':
        return '<b>에너지 섭취 관리가 필요해요!</b>\n식사는 <b>3~5시간에 한 번씩</b>\n섭취를 해주는 것이 가장 좋아요!\n\n07시 / 12시 / 16시 / 19시 이런 방식으로요!\n\n1시간 동안 에너지로\n흡수할 수 있는 양은 정해져있어요\n\n한 번에 많은 양을 섭취하면\n흡수되지 못한 양의 에너지가\n지방으로 전환돼요\n\n또 한 대사율이 떨어져\n<b>살이 찌는 체질</b>로 변하게 돼요.' 
    elif user_dining == '3회':
        return '<b>에너지 섭취 관리를 너무 잘하고 있습니다!</b>\n식사는 <b>3~5시간에 한 번씩</b>\n섭취를 해주는 것이 가장 좋아요!\n\n07시 / 12시 / 16시 / 19시 이런 방식으로요!\n\n1시간 동안 에너지로\n흡수할 수 있는 양은 정해져있어요\n\n한 번에 많은 양을 섭취하면\n흡수되지 못한 양의 에너지가\n지방으로 전환돼요\n\n또 한 대사율이 떨어져\n<b>살이 찌는 체질</b>로 변하게 돼요.' 
    elif user_dining == '4회':
        return '<b>에너지 섭취 관리를 너무 잘하고 있습니다!</b>\n식사는 <b>3~5시간에 한 번씩</b>\n섭취를 해주는 것이 가장 좋아요!\n\n07시 / 12시 / 16시 / 19시 이런 방식으로요!\n\n1시간 동안 에너지로\n흡수할 수 있는 양은 정해져있어요\n\n한 번에 많은 양을 섭취하면\n흡수되지 못한 양의 에너지가\n지방으로 전환돼요\n\n또 한 대사율이 떨어져\n<b>살이 찌는 체질</b>로 변하게 돼요.' 
    else: 
        return '<b>에너지 섭취 관리를 너무 잘하고 있습니다!</b>\n식사는 <b>3~5시간에 한 번씩</b>\n섭취를 해주는 것이 가장 좋아요!\n\n07시 / 12시 / 16시 / 19시 이런 방식으로요!\n\n1시간 동안 에너지로\n흡수할 수 있는 양은 정해져있어요\n\n한 번에 많은 양을 섭취하면\n흡수되지 못한 양의 에너지가\n지방으로 전환돼요\n\n또 한 대사율이 떨어져\n<b>살이 찌는 체질</b>로 변하게 돼요.\n\n<b>5회 이상의 식사</b>는 좋은 방법이지만\n과식의 우려가 있어 하루 권장 섭취량을\n잘 분배해 섭취해 주세요!' 



##### FINAL ######
global Recommendation
def Recommendation():
    yun_diet_main =                 {
                    'type':'text',
                    'value':'\n고객님의 식단관리를 간편하게 도와줄\n<b>윤식단 맞춤 정기구독</b>을 추천해 드려요!\n\n'
                }
    yun_diet_link =                 {
                    'type':'bullets',
                    'blocks':[
                        {
                            'type':'text',
                            'value': '<link type="url" value="https://smartstore.naver.com/yundiet/products/6032323719">"윤식단 샐러드 정기배송1일 1식 20일\n프로그램 도시락 배달\n건강 식단 새벽 구독 저염"</link>'   
                        }
                    ]
                }
    yun_honest_main =                 {
                    'type':'text',
                    'value':'\n어니스트어니스트어니스트어니스트\n<b>어니스트어니스트어니스트</b>을 추천해 드려요!\n\n'
                }
    
    yun_honest_link =                 {
                    'type':'bullets',
                    'blocks':[
                        {
                            'type':'text',
                            'value': '<link type="url" value="https://smartstore.naver.com/yundiet/products/5960404693">"어니스트어니스트어니스트어니스트어니스트어니스트어니스트"</link>'   
                        }
                    ]
                }    
    abc_main =                 {
                    'type':'text',
                    'value':'\n공복 섭취시 체지방 감소에 도움이 되는\n<b>ABC주스</b>를 추천해 드려요!\n\n'   
                }
    abc_link = {
                    'type':'bullets',
                    'blocks':[
                        {
                            'type':'text',
                            'value':'<link type="url" value="https://smartstore.naver.com/latib/products/4661326066?n_media=27758&n_query=%EB%9D%BC%ED%8B%B0%EB%B8%8C&n_rank=1&n_ad_group=grp-a001-02-000000027136859&n_ad=nad-a001-02-000000183759162&n_campaign_type=2&n_mall_id=ncp_1nt80m_01&n_mall_pid=4661326066&n_ad_group_type=2&NaPm=ct%3Dl5dnidx4%7Cci%3D0A80001FeGzw4OvR%5F0ZH%7Ctr%3Dpla%7Chk%3Dd633f149dc91e977e4d06d49e2d3db59c256261c">"라티브 ABC쥬스 클렌즈 건강 주스\n200ml x 10포"</link>'
                        }
                    ]
                }
    return yun_diet_main, yun_diet_link, yun_honest_main, yun_honest_link, abc_main, abc_link
            































### A1 . Personal Information  ###
def first_block(chat_ID,content):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] 
        content (_type_): content by webhook
    """
    import requests
    key,pwd = API_keys()
    headers = {
        'accept': 'application/json',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'x-access-key': f'{key}',
        'x-access-secret': f'{pwd}',
    }
    
    user_name = content.get('refers').get('user')['profile']['name']
    user_weight = content.get('refers').get('user')['profile']['weight']
    user_height = content.get('refers').get('user')['profile']['height']
    user_age = content.get('refers').get('user')['profile']['age']
    
    BMR = BMR_calories_calculation(user_weight, user_height, user_age)
    json_data = {
        'blocks': [
            {
                'type': 'text',
                'value': f'<b>[{user_name}]님</b>의\n 기초대사량은 <b>[{BMR}Kcal]</b>입니다!'   
            }
            ]
        } 
    response = requests.post(f'https://api.channel.io/open/v5/user-chats/{chat_ID}/messages', headers=headers, json=json_data)
    
    

def second_block(chat_ID,content):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] 
        content (_type_): content by webhook
    """
    import requests
    key,pwd = API_keys()
    headers = {
        'accept': 'application/json',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'x-access-key': f'{key}',
        'x-access-secret': f'{pwd}',
    }
    
    user_activation = content.get('refers').get('user')['profile']['activation']    
    user_goal = content.get('refers').get('user')['profile']['goal']
    user_name = content.get('refers').get('user')['profile']['name']
    user_weight = content.get('refers').get('user')['profile']['weight']
    user_height = content.get('refers').get('user')['profile']['height']
    user_age = content.get('refers').get('user')['profile']['age']
    BMR = BMR_calories_calculation(user_weight, user_height, user_age)
    maintenance = activation_calories_calculation(user_activation,BMR)
    goal_calories = goal_calories_calculation(user_goal,maintenance)
    carbohydrate, protein, fat = macro_calories_calucation(goal_calories)    
    activation = activation_response(user_activation)
    goal = goal_response(user_goal)
    
    json_data = {
        'blocks': [
            {
                'type': 'text',
                'value': f'활동량이 {activation}\n\n'
            },
            {
                'type':'text',
                'value':f'{goal}\n\n\n'
            },
            {
                'type':'text',
                'value':f'\n<b>[{user_name}]</b>님의 <b>하루 총 섭취량</b>을 알려드릴게요!\n\n'
            },
            {
                'type':'bullets',
                'blocks':[
                    {
                        'type':'text',
                        'value':f'<b>탄수화물 {carbohydrate}g</b'
                    },
                    {
                        'type':'text',
                        'value':f'<b>단백질 {protein}g</b'
                    },
                    {
                        'type':'text',
                        'value':f'<b>지방 {fat}g</b'
                    }
                ]
            },
            {
                'type':'text',
                'value':'\n\n총 <b>4번</b>에 나누어 섭취하시면 되세요!\n\n'
            },
            {
                'type':'text',
                'value':f'따라서 <b>한 끼 섭취량</b>는 아래와 같아요!\n\n'
            },
            {
                'type':'bullets',
                'blocks':[
                    {
                        'type':'text',
                        'value':f'<b>탄수화물 {int(carbohydrate/4)}g</b>'
                    },
                    {
                        'type':'text',
                        'value':f'<b>단백질 {int(protein/4)}g</b>'
                    },
                    {
                        'type':'text',
                        'value':f'<b>지방 {int(fat/4)}g</b>'
                    }
                ]
            }
        ]
    }
    response = requests.post(f'https://api.channel.io/open/v5/user-chats/{chat_ID}/messages', headers=headers, json=json_data)

### SECOND_1_BLOCK ### 
def second_1_block(chat_ID,content):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] 
        content (_type_): content by webhook
    """
    import requests
    key,pwd = API_keys()
    headers = {
        'accept': 'application/json',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'x-access-key': f'{key}',
        'x-access-secret': f'{pwd}',
    }
    
    user_activation = content.get('refers').get('user')['profile']['activation']    
    user_goal = content.get('refers').get('user')['profile']['goal']
    user_name = content.get('refers').get('user')['profile']['name']
    user_weight = content.get('refers').get('user')['profile']['weight']
    user_height = content.get('refers').get('user')['profile']['height']
    user_age = content.get('refers').get('user')['profile']['age']
    BMR = BMR_calories_calculation(user_weight, user_height, user_age)
    maintenance = activation_calories_calculation(user_activation,BMR)
    goal_calories = goal_calories_calculation(user_goal,maintenance)
    carbohydrate, protein, fat = macro_calories_calucation(goal_calories)    
    activation = activation_response(user_activation)
    goal = goal_response(user_goal)
    
    json_data = {
        'blocks':[
            {
                'type':'text',
                'value': f'\n\n<b>탄수화물 {int(carbohydrate/4)}g</b>을 섭취하기 위해서는\n아래를 참조해주세요!\n\n' 
            },
            {
                'type':'bullets',
                'blocks':[
                    {
                        'type':'text',
                        'value':f'바나나 {round((int(carbohydrate/4)/27),1)}개'
                    },
                    {
                        'type':'text',
                        'value':f'단호박 {round((int(carbohydrate/4)*(100/18)),1)}g'
                    },
                    {
                        'type':'text',
                        'value':f'고구마 {round((int(carbohydrate/4)*(100/31)),1)}g'
                    },
                    {
                        'type':'text',
                        'value':f'현미밥 {round((int(carbohydrate/4)*(100/33)),1)}g'
                    },
                    {
                        'type':'text',
                        'value':f'오트밀 {round((int(carbohydrate/4)*(100/69)),1)}g'
                    }
                ]
            },
            {
                'type':'text',
                'value':f'\n\n<b>단백질 {int(protein/4)}g</b>을 섭취하기 위해서는\n아래를 참조해주세요!\n\n' 
            },
            {
                'type':'bullets',
                'blocks':[
                    {
                        'type':'text',
                        'value':f'닭가슴살 {round((int(protein/4)*(100/22)),1)}g' 
                    },
                    {
                        'type':'text',
                        'value':f'돼지안심 {round((int(protein/4)*(100/20)),1)}g'
                    },
                    {
                        'type':'text',
                        'value':f'돼지목살 {round((int(protein/4)*(100/21)),1)}g'
                    },
                    {
                        'type':'text',
                        'value':f'소우둔살 {round((int(protein/4)*(100/20)),1)}g'
                    },
                    {
                        'type':'text',
                        'value':f'두부 {round((int(protein/4)*(100/8)),1)}g'
                    },
                    {
                        'type':'text',
                        'value':f'연어 {round((int(protein/4)*(100/21)),1)}g'
                    },
                    {
                        'type':'text',
                        'value':f'계란 {round(int(protein/4)/6,1)}개'
                    },
                    {
                        'type':'text',
                        'value':f'참치 {round((int(protein/4)*(100/19)),1)}g'
                    }
                ]
            }
        ]
    }
    response = requests.post(f'https://api.channel.io/open/v5/user-chats/{chat_ID}/messages', headers=headers, json=json_data)










### A3 . Personal Hydrate ###    
def third_block(chat_ID,content):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] 
        content (_type_): content by webhook
    """
    import requests
    key,pwd = API_keys()
    headers = {
        'accept': 'application/json',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'x-access-key': f'{key}',
        'x-access-secret': f'{pwd}',
    }
    
    user_name = content.get('refers').get('user')['profile']['name']
    user_weight = content.get('refers').get('user')['profile']['weight']
    user_hydrate =content.get('refers').get('user')['profile']['hydrate']
    response = hydrate_response(user_hydrate,user_weight,user_name)
    json_data = {
        'blocks': [
            {
                'type': 'text',
                'value': f'{response}'
            },
            {
                'type': 'text',
                'value': '커피, 차, 음료의 경우 수분 보충보다\n이뇨작용을 하기 때문에\n수분으로 간주하지 않습니다!\n\n수분 섭취는 <b>물</b>로 해야 된다는 사실을\n꼭 기억해 주세요!'
            }
            ]
        } 
    response = requests.post(f'https://api.channel.io/open/v5/user-chats/{chat_ID}/messages', headers=headers, json=json_data)
    
    
### A4 . Personal Dining ###
def fourth_block(chat_ID,content):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] 
        content (_type_): content by webhook
    """
    import requests
    key,pwd = API_keys()
    headers = {
        'accept': 'application/json',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'x-access-key': f'{key}',
        'x-access-secret': f'{pwd}',
    }
    
    user_dining = content.get('refers').get('user')['profile']['number_dining']
    response = dining_response(user_dining)
    
    json_data = {
        'blocks': [
            {
                'type': 'text',
                'value': f'식사횟수가 <b>[{user_dining}]</b>이네요!\n\n'
            },
            {
                'type': 'text',
                'value': f'{response}\n\n'
            },
            {
                'type': 'text',
                'value': '\n앞으로도 좋은 타이밍에 식사 해주세요!'                
            }
            ]
        } 
    response = requests.post(f'https://api.channel.io/open/v5/user-chats/{chat_ID}/messages', headers=headers, json=json_data)    
    

### A5 . Personal recommendation ###
def fifith_block(chat_ID,content):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] 
        content (_type_): content by webhook
    """
    import requests
    key,pwd = API_keys()
    headers = {
        'accept': 'application/json',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'x-access-key': f'{key}',
        'x-access-secret': f'{pwd}',
    }
    
    user_activation = content.get('refers').get('user')['profile']['activation']    
    user_goal = content.get('refers').get('user')['profile']['goal']
    user_name = content.get('refers').get('user')['profile']['name']
    user_weight = content.get('refers').get('user')['profile']['weight']
    user_height = content.get('refers').get('user')['profile']['height']
    user_age = content.get('refers').get('user')['profile']['age']
    user_worries =content.get('refers').get('user')['profile']['worries']
    
    BMR = BMR_calories_calculation(user_weight, user_height, user_age)
    maintenance = activation_calories_calculation(user_activation,BMR)
    goal_calories = goal_calories_calculation(user_goal,maintenance)
    carbohydrate, protein, fat = macro_calories_calucation(goal_calories)  
    yun_diet_main, yun_diet_link, yun_honest_main, yun_honest_link, abc_main, abc_link = Recommendation()
    json_data = {
        'blocks': [
            {
                'type': 'text',
                'value': f'<b>[{user_name}]</b>님의 식단관리에\n도움을 줄 수 있는 제품이에요.\n\n<b>탄수화물 {int(carbohydrate/4)}g</b>와 <b>단백질 {int(protein/4)}g</b>의 \n<b>한끼 권장 섭취량</b>에 맞는\n식단을 준비했어요.\n\n식단관리를 쉽고 편하게 시작해보세요!\n\n'
            }
        ]
    }
    
    if '빠른 체중 감량 (3개월 이내)' in user_worries:
        json_data.get('blocks').append(yun_honest_main)
        json_data.get('blocks').append(yun_honest_link)
        json_data.get('blocks').append(yun_diet_main)
        json_data.get('blocks').append(yun_diet_link)
        json_data.get('blocks').append(abc_main)
        json_data.get('blocks').append(abc_link)
    elif ('빠른 체중 감량 (3개월 이내)' not in user_worries) and ('적당한 체중 감량 (3개월 이상)' in user_worries):
        json_data.get('blocks').append(yun_diet_main)
        json_data.get('blocks').append(yun_diet_link)
        json_data.get('blocks').append(abc_main)
        json_data.get('blocks').append(abc_link)
    elif ('빠른 체중 감량 (3개월 이내)' and '적당한 체중 감량 (3개월 이상)') not in user_worries:
        json_data.get('blocks').append(yun_diet_main)
        json_data.get('blocks').append(yun_diet_link)        
        
        
    response = requests.post(f'https://api.channel.io/open/v5/user-chats/{chat_ID}/messages', headers=headers, json=json_data)    
    
### FINAL ###
def final_block(chat_ID):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] 
    """
    import requests
    key,pwd = API_keys()
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
                'value': '나에게 맞지 않는 식단은\n나에게 맞지 않는 옷과 같아요.\n\n요요가 생기거나, 폭식을 하거나\n과도한 스트레스를 받는 문제가 발생해요.\n\n영양소의 과다 공급을 점진적으로 줄여가며\n나에게 맞는 식단 관리를 시작하면\n부작용 없이 건강한 내 모습을\n만나 볼 수 있을거에요.\n\n'
            },
            {
                'type' : 'text',
                'value': '건강을 관리하는 것은\n벽돌을 쌓는 것과 같아요.\n\n조금 느리더라도 단단하게 쌓아\n무너지지 않게 하는 것이 가장 중요하죠.\n\n체중을 빨리 감량하는 것 보다,\n감량한 체중을 오래 유지하는 것이\n더욱 중요합니다.\n\n건강관리, 아직 늦지 않았어요.\n<b>윤식단</b>과 함께 지금부터라도 시작해 보세요!'
            }
            ]
        } 
    response = requests.post(f'https://api.channel.io/open/v5/user-chats/{chat_ID}/messages', headers=headers, json=json_data)    
    