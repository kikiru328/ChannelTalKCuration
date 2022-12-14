"""
Main curation Responses
"""
import requests
import main_functions
headers = main_functions.API_keys()

def Introduction1(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """    
    json_data = {
        'blocks': [
            {
                'type': 'text',
                "value": ":health_worker:\n<b>안녕하세요!</b>\n윤식단 식단 관리 팀장 <b>'제니'</b>입니다!:clap:"
            }
            ]
        } 
    
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)    


def Introduction2(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """
    
    user_name = content.get('refers').get('user')['profile']['name']
    json_data = {
        'blocks': [
            {
                'type': 'text',
                "value": f":raised_hands:\n<b>{user_name}님</b>의 <b>식단</b>을 설명해드리기 전\n짧게 제 <b>이력</b>을 소개할게요!"
            }
            ]
        } 

    
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)    



def Introduction3(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): cotent.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """
    
    user_name = content.get('refers').get('user')['profile']['name']
    json_data = {
        'blocks': [
            {
                'type': 'text',
                "value": ":muscle:\n2015년부터 현재까지\n<b>트레이너</b>로 활동하면서\n\n<b>1,000명 이상</b>의 회원님들의\n<b>식단과 건강관리</b>를 도와드렸고\n\n지금까지 총 <b>2,000Kg</b> 이상의 \n<b>지방 감량</b>에 성공했어요!"
            }
            ]
        } 

    
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)    



def Introduction4(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """
    
    user_name = content.get('refers').get('user')['profile']['name']
    json_data = {
        'blocks': [
            {
                'type': 'text',
                "value": f":question:\n<b>{user_name}님</b>은 현재 <b>식단관리</b>를\n<b>어떻게</b> 하고 있으세요?\n\n인터넷에 검색?\n유튜브를 찾아서?\n\n시중에 판매되는 <b>대부분</b>의\n<b>샐러드</b>, <b>다이어트 도시락</b>은\n\n<b>양</b>을 줄이거나, <b>칼로리</b>만 줄여\n제공하고 있어요:cry:"  
            }
            ]
        } 

    
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)    




def Introduction5(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """
    
    user_name = content.get('refers').get('user')['profile']['name']
    json_data = {
        'blocks': [
            {
                'type': 'text',
                "value": f":anguished:\n이렇게 <b>{user_name}</b>님에게\n<b>맞지 않는</b><b>식사</b>를 지속한다면\n\n<b>부족한 영양 공급</b>으로 인해\n<b>요요</b>,<b>과식</b>,<b>폭식</b> 등의\n\n다이어트 <b>부작용</b>을 만날\n<b>가능성</b>이 무려 <b>89%이상</b>이에요!:fearful:"  
            }
            ]
        } 

    
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)    





def Introduction6(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """
    
    user_name = content.get('refers').get('user')['profile']['name']
    json_data = {
        'blocks': [
            {
                'type': 'text',
                "value": ":relaxed:\n목적이 같다고 해서\n<b>가는 길이 같을 필요는 없어요!</b>\n\n<b>체중 유지라는 나의 목적</b>과\n상황을 고려한 <b>식단</b>\n\n<b>나에게 필요한 영양소</b>를\n고려한 <b>식단</b>으로 관리를 하면\n\n<b>폭식, 과식</b>을 예방할 수 있고\n충분한 <b>영양공급</b>으로\n\n<b>요요없이</b>, 원하는 체중으로\n오래 유지할 수 있어요. :+1:"  
            }
            ]
        } 

    
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)    




def Introduction7(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """
    
    user_name = content.get('refers').get('user')['profile']['name']
    json_data = {
        'blocks': [
            {
                'type': 'text',
                "value": f":clipboard:\n<b>[{user_name}]</b>님의\n<b>성공적인 식단 관리</b>를 위해\n<b>한 끼 섭취량 </b>을 알려드릴게요!"  
            }
            ]
        } 

    
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)    

                                            
def Activation_food_amount(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] 
        content (_type_): content by webhook
    """
    
    
    user_activation = content.get('refers').get('user')['profile']['activation']    
    user_goal = content.get('refers').get('user')['profile']['goal']
    user_name = content.get('refers').get('user')['profile']['name']
    user_weight = content.get('refers').get('user')['profile']['weight']
    user_height = content.get('refers').get('user')['profile']['height']
    user_age = content.get('refers').get('user')['profile']['age']
    BMR = main_functions.BMR_calories_calculation(user_weight, user_height, user_age)
    maintenance = main_functions.activation_calories_calculation(user_activation,BMR)
    goal_calories = main_functions.goal_calories_calculation(user_goal,maintenance)
    carbohydrate, protein, fat = main_functions.macro_calories_calucation(goal_calories)    
    activation = main_functions.activation_response(user_activation)
    goal = main_functions.goal_response(user_goal)
    
    json_data = {
        'blocks': [
            {
                'type':'text',
                'value':f':fork_and_knife:\n<b>[{user_name}]님의 성공적인 식단관리를 위해\n<b>한 끼 섭취량</b>을 알려드릴게요!\n\n'
            },
            {
                'type':'text',
                'value':f':rice: <b>탄수화물 {int(carbohydrate/4)}g</b>\n:meat_on_bone: <b>단백질 {int(protein/4)}g</b>\n:chestnut: <b>지방 {int(fat/4)}g</b>'
            }
        ]
    }
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)
                               

# 4th : Calories per dining
def Calories_per_dining(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] 
        content (_type_): content by webhook
    """
    
    
    user_activation = content.get('refers').get('user')['profile']['activation']    
    user_goal = content.get('refers').get('user')['profile']['goal']
    user_name = content.get('refers').get('user')['profile']['name']
    user_weight = content.get('refers').get('user')['profile']['weight']
    user_height = content.get('refers').get('user')['profile']['height']
    user_age = content.get('refers').get('user')['profile']['age']
    BMR = main_functions.BMR_calories_calculation(user_weight, user_height, user_age)
    maintenance = main_functions.activation_calories_calculation(user_activation,BMR)
    goal_calories = main_functions.goal_calories_calculation(user_goal,maintenance)
    carbohydrate, protein, fat = main_functions.macro_calories_calucation(goal_calories)    
    activation = main_functions.activation_response(user_activation)
    goal = main_functions.goal_response(user_goal)
    
    json_data = {
        'blocks':[
            {
                'type':'text',
                'value':':rice:\n'
            },
            {
                'type':'text',
                'value': f'<b>탄수화물 {int(carbohydrate/4)}g</b>을 섭취하기 위해서는\n아래를 참조해주세요!\n\n' 
            },
            {
                'type':'bullets',
                'blocks':[
                    {
                        'type':'text',
                        'value':f':sweet_potato: 고구마 {round((int(carbohydrate/4)*(100/31)),1)}g'
                    },
                    {
                        'type':'text',
                        'value':f':rice: 현미밥 {round((int(carbohydrate/4)*(100/33)),1)}g'
                    },
                    {
                        'type':'text',
                        'value':f':banana: 바나나 {round((int(carbohydrate/4)/27),1)}개'
                    }
                ]
            },
            {
                'type':'text',
                'value':'\n\n:meat_on_bone:\n'
            },
            {
                'type':'text',
                'value':f'<b>단백질 {int(protein/4)}g</b>을 섭취하기 위해서는\n아래를 참조해주세요!\n\n' 
            },
            {
                'type':'bullets',
                'blocks':[
                    {
                        'type':'text',
                        'value':f':chicken: 닭가슴살 {round((int(protein/4)*(100/22)),1)}g' 
                    },
                    {
                        'type':'text',
                        'value':f':cut_of_meat: 돼지안심 {round((int(protein/4)*(100/20)),1)}g'
                    },
                    {
                        'type':'text',
                        'value':f':meat_on_bone: 돼지목살 {round((int(protein/4)*(100/21)),1)}g'
                    }
                ]
            }
        ]
    }
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)
##############################################################################       
def Before_form(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """
    
    user_name = content.get('refers').get('user')['profile']['name']
    json_data = {
        'blocks': [
            {
                'type': 'text',
                "value": f":gift:\n<b>[{user_name}]</b>님의 성공적인 다이어트를\n도와주기 위해 <b>윤식단</b>이\n<b>선물</b>을 준비했어요!\n"  
            }
            ]
        } 

    
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)    


def RESET(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] 
    """
    
    user_name = content.get('refers').get('user')['profile']['name']
    json_data = {
        'form': {
            "inputs" : [
                {
                    "value" : {},
                    "readOnly" : False,
                    "type" : "bool",
                    "label" : "받으시겠어요?",
                    "dataType" : 'boolean',
                    "bindingKey" : "user.profile.table"
                }
            ],
            "type" : "bool"
        }
        } 
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)    
    