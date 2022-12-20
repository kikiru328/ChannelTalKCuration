"""
Main curation Responses
<content direction>
chat_id (str): content.get('refers').get('message')['chatId']
post_type (str) : groups : post message to groups
"""
import requests
import main_function

headers = main_function.api_header()


def get_variables(content: dict) -> tuple:
    """
    get_variables for functions

    Args:
        content (dict): post dictionary

    Returns:
        list: functions variables
    """
    user_name = content.get("refers").get("user")["profile"]["name"]
    user_weight = content.get("refers").get("user")["profile"]["weight"]
    user_height = content.get("refers").get("user")["profile"]["height"]
    user_age = content.get("refers").get("user")["profile"]["age"]
    user_activation = content.get("refers")["user"]["profile"]["activation"]
    user_goal = content.get("refers").get("user")["profile"]["goal"]
    bmr = main_function.get_bmr(user_weight, user_height, user_age)
    maintenance = main_function.get_cal_by_activation(user_activation, bmr)
    goal_calories = main_function.get_cal_for_goal(user_goal, maintenance)
    carbohydrate, protein, fat = main_function.get_macro_cal(goal_calories)
    return (
        user_name,
        user_weight,
        user_height,
        user_age,
        user_activation,
        user_goal,
        bmr,
        maintenance,
        goal_calories,
        carbohydrate,
        protein,
        fat,
    )


def introduction1(chat_id: str, post_type: str) -> requests:
    """_summary_

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
    """
    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": ":health_worker:\n<b>안녕하세요!</b>"
                + "\n윤식단 식단 관리 팀장 <b>'제니'</b>입니다!:clap:",
            }
        ]
    }

    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def introduction2(chat_id: str, content: dict, post_type: str) -> requests:
    """_summary_

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
        content : dict, content of post
    """

    user_name: str = get_variables(content)[0]
    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": ":raised_hands:"
                + f"\n<b>{user_name}님</b>의 <b>식단</b>을 설명해드리기 전"
                + "\n짧게 제 <b>이력</b>을 소개할게요!",
            }
        ]
    }

    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def introduction3(chat_id: str, post_type: str) -> requests:
    """_summary_

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
    """

    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": ":muscle:\n2015년부터 현재까지\n<b>트레이너</b>로 활동하면서"
                + "\n\n<b>1,000명 이상</b>의 회원님들의\n<b>식단과 건강관리</b>를 도와드렸고"
                + "\n\n지금까지 총 <b>2,000Kg</b> 이상의 \n<b>지방 감량</b>에 성공했어요!",
            }
        ]
    }

    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def introduction4(chat_id: str, content: dict, post_type: str) -> requests:
    """_summary_

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
        content : dict, content of post
    """

    user_name: str = get_variables(content)[0]
    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": f":question:\n<b>{user_name}님</b>은 현재 <b>식단관리</b>를"
                + "\n<b>어떻게</b> 하고 있으세요?\n\n인터넷에 검색?\n유튜브를 찾아서?"
                + "\n\n시중에 판매되는 <b>대부분</b>의"
                + "\n<b>샐러드</b>,<b>다이어트 도시락</b>은"
                + "\n\n<b>양</b>을 줄이거나, <b>칼로리</b>만 줄여"
                + "\n제공하고 있어요:cry:",
            }
        ]
    }

    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def introduction5(chat_id: str, content: dict, post_type: str) -> requests:
    """_summary_

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
        content : dict, content of post
    """

    user_name: str = get_variables(content)[0]
    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": f":anguished:\n이렇게 <b>{user_name}</b>님에게"
                + "\n<b>맞지 않는</b><b>식사</b>를 지속한다면"
                + "\n\n<b>부족한 영양 공급</b>으로 인해"
                + "\n<b>요요</b>,<b>과식</b>,<b>폭식</b> 등의"
                + "\n\n다이어트 <b>부작용</b>을 만날"
                + "\n<b>가능성</b>이 무려 <b>89%이상</b>이에요!:fearful:",
            }
        ]
    }

    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def introduction6(chat_id: str, post_type: str) -> requests:
    """_summary_

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
        content : dict, content of post
    """

    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": ":relaxed:\n목적이 같다고 해서"
                + "\n<b>가는 길이 같을 필요는 없어요!</b>"
                + "\n\n<b>체중 유지라는 나의 목적</b>과\n상황을 고려한 <b>식단</b>"
                + "\n\n<b>나에게 필요한 영양소</b>를\n고려한 <b>식단</b>으로 관리를 하면"
                + "\n\n<b>폭식, 과식</b>을 예방할 수 있고\n충분한 <b>영양공급</b>으로"
                + "\n\n<b>요요없이</b>, 원하는 체중으로\n오래 유지할 수 있어요. :+1:",
            }
        ]
    }

    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def introduction7(chat_id: str, content: dict, post_type: str) -> requests:
    """_summary_

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
        content : dict, content of post
    """

    user_name: str = get_variables(content)[0]
    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": f":clipboard:\n<b>[{user_name}]</b>님의"
                + "\n<b>성공적인 식단 관리</b>를 위해"
                + "\n<b>한 끼 섭취량 </b>을 알려드릴게요!",
            }
        ]
    }

    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def get_food_amount(chat_id: str, content: dict, post_type: str) -> requests:
    """_summary_

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
        content : dict, content of post
    """

    user_name: str = get_variables(content)[0]
    carbohydrate: int = get_variables(content)[9]
    protein: int = get_variables(content)[10]
    fat: int = get_variables(content)[11]
    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": ":fork_and_knife:"
                + f"\n<b>[{user_name}]님의 성공적인 식단관리를 위해"
                + "\n<b>한 끼 섭취량</b>을 알려드릴게요!\n\n",
            },
            {
                "type": "text",
                "value": f":rice: <b>탄수화물 {int(carbohydrate/4)}g</b>"
                + f"\n:meat_on_bone: <b>단백질 {int(protein/4)}g</b>"
                + f"\n:chestnut: <b>지방 {int(fat/4)}g</b>",
            },
        ]
    }
    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def cal_per_dining(chat_id: str, content: dict, post_type: str) -> requests:
    """_summary_

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
        content : dict, content of post
    """

    carbohydrate: int = get_variables(content)[9]
    protein: int = get_variables(content)[10]

    json_data = {
        "blocks": [
            {"type": "text", "value": ":rice:\n"},
            {
                "type": "text",
                "value": f"<b>탄수화물 {int(carbohydrate/4)}g</b>을 섭취하기 위해서는"
                + "\n아래를 참조해주세요!\n\n",
            },
            {
                "type": "bullets",
                "blocks": [
                    {
                        "type": "text",
                        "value": ":sweet_potato: 고구마"
                        + f" {round((int(carbohydrate/4)*(100/31)),1)}g",
                    },
                    {
                        "type": "text",
                        "value": ":rice: 현미밥"
                        + f" {round((int(carbohydrate/4)*(100/33)),1)}g",
                    },
                    {
                        "type": "text",
                        "value": ":banana: 바나나"
                        + f" {round((int(carbohydrate/4)/27),1)}개",
                    },
                ],
            },
            {"type": "text", "value": "\n\n:meat_on_bone:\n"},
            {
                "type": "text",
                "value": f"<b>단백질 {int(protein/4)}g</b>을 섭취하기 위해서는"
                + "\n아래를 참조해주세요!\n\n",
            },
            {
                "type": "bullets",
                "blocks": [
                    {
                        "type": "text",
                        "value": ":chicken: 닭가슴살"
                        + f" {round((int(protein/4)*(100/22)),1)}g",
                    },
                    {
                        "type": "text",
                        "value": ":cut_of_meat: 돼지안심"
                        + f" {round((int(protein/4)*(100/20)),1)}g",
                    },
                    {
                        "type": "text",
                        "value": ":meat_on_bone: 돼지목살"
                        + f" {round((int(protein/4)*(100/21)),1)}g",
                    },
                ],
            },
        ]
    }
    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def before_form(chat_id: str, content: dict, post_type: str) -> requests:
    """_summary_

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
        content : dict, content of post
    """

    user_name: str = get_variables(content)[0]
    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": f":gift:\n<b>[{user_name}]</b>님의 성공적인 다이어트를"
                + "\n도와주기 위해 <b>윤식단</b>이\n<b>선물</b>을 준비했어요!\n",
            }
        ]
    }

    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def question_present(chat_id: str, content: dict, post_type: str) -> requests:
    """_summary_

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
        content : dict, content of post
    """
    user_name: str = get_variables(content)[0]
    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": "<b>선물</b> 이라고 메시지를 남겨주시면"
                + f"<b>{user_name}</b>님에게 맞는 선물을 준비해드릴게요! :blush:",
            }
        ]
    }
    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )
