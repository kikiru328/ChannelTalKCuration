
######                                            
#     # ###### #      ######   ##    ####  ###### 
#     # #      #      #       #  #  #      #      
######  #####  #      #####  #    #  ####  #####  
#   #   #      #      #      ######      # #      
#    #  #      #      #      #    # #    # #      
#     # ###### ###### ###### #    #  ####  ###### 
                                                  
global main_function
import main_function


 ######  #######    ####    #####   ##  ###  #####    
#####    ##  ###   ## ###  ##  ##   ### ###  ## ###   
##       ##   ##  ##       ##  ###  #######  ##  ###  
 #####   ###      ###      ##   ##  ## ####  ##   ##  
    ###  ####     #### ##  ###  ##  ##   ##  ##   ##  
###  ##  ##   ##   ######   ##  ##  ###  ##  ### ###  
######   #######    ####    #####   ###  ##  ######   
                                                      
def SECOND(chat_ID,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """
    import requests
    import main_function
    key,pwd = main_function.API_keys()
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
                'value': ':bulb: 공사중입니다! :bulb:\n\n'
            },
            {
                'type' : 'text',
                'value' : ':bulb: 최대한 빨리 고치겠습니다 :bulb:'
            }
            ]
        } 
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)    

                                                                                 
######   ##  ##   ######   #####     ####   
  ##     ### ##     ##     ##  ##   ##  ##  
  ##     ######     ##     ##  ##   ##  ##  
  ##     ## ###     ##     #####    ##  ##  
  ##     ##  ##     ##     ## ##    ##  ##  
######   ##  ##     ##     ##  ##    ####   
                                                                                 


def Introduction(chat_ID,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """
    import requests
    import main_function
    key,pwd = main_function.API_keys()
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
                'value': ':bulb: 나에게 맞는 식단을 분석중입니다'
            }
            ]
        } 

    
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)    
#############################################################################################   

                                                           
#####    ##   ##  #####   
##  ##   #######  ##  ##  
#####    #######  ##  ##  
##  ##   ## # ##  #####   
##  ##   ##   ##  ## ##   
#####    ##   ##  ##  ##  
                                                               

def Personal_Information_BMR(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] 
        content (_type_): content by webhook
    """
    import requests
    import main_function
    key,pwd = main_function.API_keys()
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
    
    BMR = main_function.BMR_calories_calculation(user_weight, user_height, user_age)
    json_data = {
        'blocks': [
            {
                'type': 'text',
                'value': f'<b>[{user_name}]님</b>의\n 기초대사량은 <b>[{BMR}Kcal]</b>입니다!'   
            }
            ]
        } 
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)
############################################################################################# 
                                                                                              
                                                                                                                                  
  ##      ####    ######   ######   ##  ##   ######              ##     ##   ##  ######  
 ####    ##  ##     ##       ##     ##  ##   ##                 ####    #######    ##    
##  ##   ##         ##       ##     ##  ##   ####              ##  ##   #######    ##    
##  ##   ##         ##       ##     ##  ##   ##                ##  ##   ## # ##    ##    
######   ##  ##     ##       ##      ####    ##                ######   ##   ##    ##    
##  ##    ####      ##     ######     ##     ######            ##  ##   ##   ##    ##    
                                                                                              
                                                                                                                                 
def Activation_food_amount(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] 
        content (_type_): content by webhook
    """
    import requests
    import main_function
    key,pwd = main_function.API_keys()
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
    BMR = main_function.BMR_calories_calculation(user_weight, user_height, user_age)
    maintenance = main_function.activation_calories_calculation(user_activation,BMR)
    goal_calories = main_function.goal_calories_calculation(user_goal,maintenance)
    carbohydrate, protein, fat = main_function.macro_calories_calucation(goal_calories)    
    activation = main_function.activation_response(user_activation)
    goal = main_function.goal_response(user_goal)
    
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
                'value':f':fork_and_knife:<b>[{user_name}]</b>님의 <b>하루 총 섭취량</b>을\n알려드릴게요!\n\n'
            },
            {
                'type':'text',
                'value':f':rice: <b>탄수화물 {carbohydrate}g</b>\n:meat_on_bone: <b>단백질 {protein}g</b>\n:chestnut: <b>지방 {fat}g</b>'
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
                'type':'text',
                'value':f':rice: <b>탄수화물 {int(carbohydrate/4)}g</b>\n:meat_on_bone: <b>단백질 {int(protein/4)}g</b>\n:chestnut: <b>지방 {int(fat/4)}g</b>'
            }
        ]
    }
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)
#############################################################################################

                                                                                                                              
 ####      ##     ##                ####     ######   ##  ##   ######   ##  ##    ####   
##  ##    ####    ##                ## ##      ##     ### ##     ##     ### ##   ##  ##  
##       ##  ##   ##                ##  ##     ##     ######     ##     ######   ##      
##       ##  ##   ##                ##  ##     ##     ## ###     ##     ## ###   ## ###  
##  ##   ######   ##                ## ##      ##     ##  ##     ##     ##  ##   ##  ##  
 ####    ##  ##   ######            ####     ######   ##  ##   ######   ##  ##    ####   
                                                                                                                              

# 4th : Calories per dining
def Calories_per_dining(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] 
        content (_type_): content by webhook
    """
    import requests
    import main_function
    key,pwd = main_function.API_keys()
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
    BMR = main_function.BMR_calories_calculation(user_weight, user_height, user_age)
    maintenance = main_function.activation_calories_calculation(user_activation,BMR)
    goal_calories = main_function.goal_calories_calculation(user_goal,maintenance)
    carbohydrate, protein, fat = main_function.macro_calories_calucation(goal_calories)    
    activation = main_function.activation_response(user_activation)
    goal = main_function.goal_response(user_goal)
    
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
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)
#############################################################################################


                                                                                                                     
##  ##   ##  ##   ####     #####      ##     ######   ######    ####    ##  ##  
##  ##   ##  ##   ## ##    ##  ##    ####      ##       ##     ##  ##   ### ##  
######    ####    ##  ##   ##  ##   ##  ##     ##       ##     ##  ##   ######  
##  ##     ##     ##  ##   #####    ##  ##     ##       ##     ##  ##   ## ###  
##  ##     ##     ## ##    ## ##    ######     ##       ##     ##  ##   ##  ##  
##  ##     ##     ####     ##  ##   ##  ##     ##     ######    ####    ##  ##  
                                                                                                                     

def Hydration(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] 
        content (_type_): content by webhook
    """
    import requests
    import main_function
    key,pwd = main_function.API_keys()
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
    response = main_function.hydrate_response(user_hydrate,user_weight,user_name)
    json_data = {
        'blocks': [
            {
                'type': 'text',
                'value': f'{response}'
            },
            {
                'type': 'text',
                'value': '커피, 차, 음료의 경우 수분 보충보다\n<b>이뇨작용</b>을 하기 때문에\n수분으로 간주하지 않습니다!\n\n수분 섭취는 <b>물</b>로 해야 된다는 사실을\n<b>꼭</b> 기억해 주세요!:wink:'
                
            }
            ]
        } 
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)
#############################################################################################  
    
                                                                                                                     
####     ######   ##  ##            ##  ##     ##     #####    ######   ######  
## ##      ##     ### ##            ##  ##    ####    ##  ##     ##       ##    
##  ##     ##     ######            ######   ##  ##   #####      ##       ##    
##  ##     ##     ## ###            ##  ##   ##  ##   ##  ##     ##       ##    
## ##      ##     ##  ##            ##  ##   ######   ##  ##     ##       ##    
####     ######   ##  ##            ##  ##   ##  ##   #####    ######     ##    
                                                                                                                     

def Dining_Habit(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] 
        content (_type_): content by webhook
    """
    import requests
    import main_function
    key,pwd = main_function.API_keys()
    headers = {
        'accept': 'application/json',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'x-access-key': f'{key}',
        'x-access-secret': f'{pwd}',
    }
    
    user_dining = content.get('refers').get('user')['profile']['number_dining']
    response =main_function.dining_response(user_dining)
    
    json_data = {
        'blocks': [
            {
                'type':'text',
                'value':':fork_and_knife:\n'
            },
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
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)    
#############################################################################################    


                                                                                                                                                                  
#####    ######    ####     ####    ##   ##  ##   ##  ######   ##  ##   ####       ##     ######   ######    ####    ##  ##  
##  ##   ##       ##  ##   ##  ##   #######  #######  ##       ### ##   ## ##     ####      ##       ##     ##  ##   ### ##  
##  ##   ####     ##       ##  ##   #######  #######  ####     ######   ##  ##   ##  ##     ##       ##     ##  ##   ######  
#####    ##       ##       ##  ##   ## # ##  ## # ##  ##       ## ###   ##  ##   ##  ##     ##       ##     ##  ##   ## ###  
## ##    ##       ##  ##   ##  ##   ##   ##  ##   ##  ##       ##  ##   ## ##    ######     ##       ##     ##  ##   ##  ##  
##  ##   ######    ####     ####    ##   ##  ##   ##  ######   ##  ##   ####     ##  ##     ##     ######    ####    ##  ##  
                                                                                                                                                                  

def Recommendation(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] 
        content (_type_): content by webhook
    """
    import requests
    import main_function
    key,pwd = main_function.API_keys()
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
    
    BMR = main_function.BMR_calories_calculation(user_weight, user_height, user_age)
    maintenance = main_function.activation_calories_calculation(user_activation,BMR)
    goal_calories = main_function.goal_calories_calculation(user_goal,maintenance)
    carbohydrate, protein, fat = main_function.macro_calories_calucation(goal_calories)  
    
    json_data = {
        'blocks': [
            {
                'type': 'text',
                'value': f'<b>[{user_name}]</b>님의 식단관리에\n도움을 줄 수 있는 제품이에요.\n\n:pushpin: <b>탄수화물 {int(carbohydrate/4)}g</b>와 <b>단백질 {int(protein/4)}g</b>의 \n<b>   한끼 권장 섭취량</b>에 맞는\n   식단을 준비했어요.\n\n식단관리를 쉽고 편하게 시작해보세요!\n\n'
            }
        ]
    }

    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)    
#############################################################################################    


                                                                                                                              
#####    ######    ####     ####    ##   ##           ##       ######   ##  ##   ##  ##  
##  ##   ##       ##  ##   ##  ##   #######           ##         ##     ### ##   ## ##   
##  ##   ####     ##       ##  ##   #######           ##         ##     ######   ####    
#####    ##       ##       ##  ##   ## # ##           ##         ##     ## ###   ####    
## ##    ##       ##  ##   ##  ##   ##   ##           ##         ##     ##  ##   ## ##   
## ###   ######    ####     ####    ##   ##           ######   ######   ##  ##   ##  ##  
                                                                                                                              

def Recommendation_Link(chat_ID, content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] 
        content (_type_): content by webhook
    """
    import requests
    import main_function
    import time
    key,pwd = main_function.API_keys()
    headers = {
        'accept': 'application/json',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'x-access-key': f'{key}',
        'x-access-secret': f'{pwd}',
    }
    
    user_worries =content.get('refers').get('user')['profile']['worries']
    user_activation = content.get('refers').get('user')['profile']['activation']    
    user_goal = content.get('refers').get('user')['profile']['goal']
    user_name = content.get('refers').get('user')['profile']['name']
    user_weight = content.get('refers').get('user')['profile']['weight']
    user_height = content.get('refers').get('user')['profile']['height']
    user_age = content.get('refers').get('user')['profile']['age']
    
    BMR = main_function.BMR_calories_calculation(user_weight, user_height, user_age)
    maintenance = main_function.activation_calories_calculation(user_activation,BMR)
    goal_calories = main_function.goal_calories_calculation(user_goal,maintenance)
    carbohydrate, protein, fat = main_function.macro_calories_calucation(goal_calories) 
    yun_diet,honest = main_function.Recommendation(carbohydrate,protein)
    
    if '빠른 체중 감량 (3개월 이내)' in user_worries:
        response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=honest)
        # time.sleep(1)         
        response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=yun_diet)       
        # time.sleep(1)
        # response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=abc)   
    elif ('빠른 체중 감량 (3개월 이내)' not in user_worries) and ('적당한 체중 감량 (3개월 이상)' in user_worries):
        response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=yun_diet)
        # time.sleep(1)
        # response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=abc)
    elif ('빠른 체중 감량 (3개월 이내)' and '적당한 체중 감량 (3개월 이상)') not in user_worries:
        response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=yun_diet) 
#############################################################################################        


                                                                                                            
 ####     ####    ##  ##   ######   ####     ##  ##   ##       ######  
##       ##  ##   ##  ##   ##       ## ##    ##  ##   ##       ##      
 ####    ##       ######   ####     ##  ##   ##  ##   ##       ####    
    ##   ##       ##  ##   ##       ##  ##   ##  ##   ##       ##      
    ##   ##  ##   ##  ##   ##       ## ##    ##  ##   ##       ##      
 ####     ####    ##  ##   ######   ####      ####    ######   ######  
                                                                                                            

def Dining_Schedule(chat_ID,content,post_type):
    import requests
    import main_function
    key,pwd = main_function.API_keys()
    headers = {
        'accept': 'application/json',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'x-access-key': f'{key}',
        'x-access-secret': f'{pwd}',
    }
    
    user_goal = content.get('refers').get('user')['profile']['goal']
    user_name = content.get('refers').get('user')['profile']['name']
    json_data={
        'blocks':[
            {
                'type':'text',
                'value':f"ㅤㅤ\n:calendar: <b>[{user_name}]님</b>에 맞춘\n     <b>맞춤 식단표</b>에요!:v:"
            }
        ],
        'buttons':[
            {   
                'title':'맞춤 식단표 받기',
                "colorVariant": "orange",  
                "url": main_function.table(user_goal)                                      
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
    import main_function
    key,pwd = main_function.API_keys()
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




def RESET(chat_ID,content,post_type):
    """_summary_

    Args:
        chat_ID (str): content.get('refers').get('message')['chatId'] 
    """
    import requests
    import main_function
    key,pwd = main_function.API_keys()
    headers = {
        'accept': 'application/json',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'x-access-key': f'{key}',
        'x-access-secret': f'{pwd}',
    }
    user_name = content.get('refers').get('user')['profile']['name']
    json_data = {
        'form': {
            "inputs" : [
                {
                    "value" : {},
                    "readOnly" : False,
                    "type" : "bool",
                    "label" : f'{user_name} 중 입니다.',
                    "dataType" : 'boolean',
                    "bindingKey" : "user.profile.table"
                }
            ],
            "type" : "bool"
        }
        } 
    response = requests.post(f'https://api.channel.io/open/v5/{post_type}/{chat_ID}/messages', headers=headers, json=json_data)    
    