def API_keys():
    """ API KEY FOR CHANNEL TALK 

    Returns:
        API : API KEY / PWD
    """
    import json
    with open('API_key.json','r') as api_json:
       api = json.load(api_json) 
    key = api.get('x-access-key')
    sec = api.get('x-access-secret')
    return key,sec


def BMR_calories_calculation(user_weight, user_height, user_age):

    """BMR : 기초대사량 계산 

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
    elif user_activation == '보통 (주2~4회)' : return int(BMR * 1.375)
    elif user_activation == '많다(주5~7회)' : return int(BMR * 1.55)
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
    if user_hydrate == '500ml 이하' : return f':droplet:\n<b>[수분{hydration}L]</b>가 <b>[{user_name}]</b>님의\n하루 수분 섭취량이에요.\n\n현재 심각한 수분 부족 상태로,\n충분한 수분 보충을 권장 드립니다!\n\n처음부터 너무 많은 양의 물을 섭취하는 것이 부담스러우시다면\n<b>하루 "1L"</b>섭취로 점진적으로\n시작해 보세요!\n\n'
    elif user_hydrate == '1L 이하' : return f':droplet:\n<b>[수분{hydration}L]</b>가 <b>[{user_name}]</b>님의\n하루 수분 섭취량이에요.\n\n현재 심각한 수분 부족 상태로,\n충분한 수분 보충을 권장 드립니다!\n\n처음부터 너무 많은 양의 물을 섭취하는 것이 부담스러우시다면\n<b>하루 "1.5L"</b>섭취로 점진적으로\n시작해 보세요!\n\n'
    elif user_hydrate == '1.5L 이하' : return f':droplet:\n<b>[수분{hydration}L]</b>가 <b>[{user_name}]</b>님의\n하루 수분 섭취량이에요.\n\n조금만 더 수분 보충에 신경 써주신다면\n더욱 좋은 몸의 상태를\n유지할 수 있을 거예요!\n\n'
    else: return f':droplet:\n<b>[수분{hydration}L]</b>가 <b>[{user_name}]</b>님의\n하루 수분 섭취량이에요.\n\n현재 수분 보충을\n열심히 하시는 것 같아요!\n나에게 맞는 섭취량을 정확히 알아가며\n더욱 좋은 몸의 컨디션을 만들어보세요!\n\n'


def dining_response(user_dining):
    """_summary_

    Args:
        user_dining (str): content.get('refers').get('user')['profile']['number_dining']

    Returns:
        str: response str > fourth_block
    """
    if user_dining == '1회':
        return '<b>에너지 섭취 관리가 필요해요!</b>\n식사는 <b>3~5시간에 한 번씩</b>\n섭취를 해주는 것이 가장 좋아요!\n\n:alarm_clock: 07시 / 12시 / 16시 / 19시\n   이런 방식으로요!\n\n1시간 동안 에너지로\n흡수할 수 있는 양은 정해져있어요\n\n한 번에 많은 양을 섭취하면\n흡수되지 못한 양의 에너지가\n지방으로 전환돼요\n\n또 한 대사율이 떨어져\n<b>살이 찌는 체질</b>로 변하게 돼요.'
    elif user_dining == '2회':
        return '<b>에너지 섭취 관리가 필요해요!</b>\n식사는 <b>3~5시간에 한 번씩</b>\n섭취를 해주는 것이 가장 좋아요!\n\n:alarm_clock: 07시 / 12시 / 16시 / 19시\n   이런 방식으로요!\n\n1시간 동안 에너지로\n흡수할 수 있는 양은 정해져있어요\n\n한 번에 많은 양을 섭취하면\n흡수되지 못한 양의 에너지가\n지방으로 전환돼요\n\n또 한 대사율이 떨어져\n<b>살이 찌는 체질</b>로 변하게 돼요.' 
    elif user_dining == '3회':
        return '<b>에너지 섭취 관리를\n 너무 잘하고 있습니다!</b>\n식사는 <b>3~5시간에 한 번씩</b>\n섭취를 해주는 것이 가장 좋아요!\n\n:alarm_clock: 07시 / 12시 / 16시 / 19시\n   이런 방식으로요!\n\n1시간 동안 에너지로\n흡수할 수 있는 양은 정해져있어요\n\n한 번에 많은 양을 섭취하면\n흡수되지 못한 양의 에너지가\n지방으로 전환돼요\n\n또 한 대사율이 떨어져\n<b>살이 찌는 체질</b>로 변하게 돼요.' 
    elif user_dining == '4회':
        return '<b>에너지 섭취 관리를\n 너무 잘하고 있습니다!</b>\n식사는 <b>3~5시간에 한 번씩</b>\n섭취를 해주는 것이 가장 좋아요!\n\n:alarm_clock: 07시 / 12시 / 16시 / 19시\n   이런 방식으로요!\n\n1시간 동안 에너지로\n흡수할 수 있는 양은 정해져있어요\n\n한 번에 많은 양을 섭취하면\n흡수되지 못한 양의 에너지가\n지방으로 전환돼요\n\n또 한 대사율이 떨어져\n<b>살이 찌는 체질</b>로 변하게 돼요.' 
    else: 
        return '<b>에너지 섭취 관리를\n 너무 잘하고 있습니다!</b>\n식사는 <b>3~5시간에 한 번씩</b>\n섭취를 해주는 것이 가장 좋아요!\n\n:alarm_clock: 07시 / 12시 / 16시 / 19시\n이런 방식으로요!\n\n1시간 동안 에너지로\n흡수할 수 있는 양은 정해져있어요\n\n한 번에 많은 양을 섭취하면\n흡수되지 못한 양의 에너지가\n지방으로 전환돼요\n\n또 한 대사율이 떨어져\n<b>살이 찌는 체질</b>로 변하게 돼요.\n\n<b>5회 이상의 식사</b>는 좋은 방법이지만\n과식의 우려가 있어 하루 권장 섭취량을\n잘 분배해 섭취해 주세요!' 


def Recommendation(carbohydrate,protein):
    if (int(carbohydrate/4) in range(0,56)) and (int(protein/4) in range(0,36)): url = 'https://yundiet.com/curation_program/?idx=23'
    elif (int(carbohydrate/4) in range(0,56)) and (int(protein/4) in range(36,40)): url = 'https://yundiet.com/curation_program/?idx=30'
    elif (int(carbohydrate/4) in range(0,56)) and (int(protein/4) in range(40,101)): url = 'https://yundiet.com/curation_program/?idx=33'
        
    elif (int(carbohydrate/4) in range(56,69)) and (int(protein/4) in range(0,36)): url = 'https://yundiet.com/curation_program/?idx=38'
    elif (int(carbohydrate/4) in range(56,69)) and (int(protein/4) in range(36,40)): url ='https://yundiet.com/curation_program/?idx=39'
    elif (int(carbohydrate/4) in range(56,69)) and (int(protein/4) in range(40,101)): url = 'https://yundiet.com/curation_program/?idx=40'
        
    elif (int(carbohydrate/4) in range(69,81)) and (int(protein/4) in range(0,36)): url = 'https://yundiet.com/curation_program/?idx=41'
    elif (int(carbohydrate/4) in range(69,81)) and (int(protein/4) in range(36,40)): url = 'https://yundiet.com/curation_program/?idx=42'
    elif (int(carbohydrate/4) in range(69,81)) and (int(protein/4) in range(40,101)): url = 'https://yundiet.com/curation_program/?idx=45'                
    
    else : url = 'https://yundiet.com/curation_program/?idx=45' 
    
    yun_diet ={
        'blocks':[
            {
                'type':'text',
                'value':':herb: 식단관리를 간편하게\n   도와줄 <b>윤식단 맞춤 정기구독</b>을\n   추천해 드려요!'
            }
        ],
        'buttons':[
            {
                'title':'윤식단 샐러드 정기배송 프로그램',
                'colorVariant':'green',
                'url': url
            }
        ]
    }

    
    honest = {
        'blocks':[
            {
                'type':'text',
                'value':':pray: 당신을 위한 \n    정직한 한끼, <b>어니스트</b>를\n   추천해 드려요!'
            }
        ],
        'buttons':[
            {
                'title':'진정한 윤식단 어니스트',
                'colorVariant':'green',
                'url':'https://yundiet.com/store_all/?idx=47'
            }
        ]
    }
    return yun_diet, honest


def table(user_goal):
    url = 'http://3.38.103.219:5000/static/img'
    print('tabel : ' , user_goal)
    if  '이상의 감량을' in user_goal : return f'{url}/more_5_reduce.png'
    elif '5Kg 미만' in user_goal : return f'{url}/less_5_reduce.png'
    elif '증량' in user_goal : return f'{url}/gain_5.png'
    else: return f'{url}/maintain.png'












