"""
present curation Responses
<content direction>
chat_id (str): content.get('refers').get('message')['chatId']
post_type (str) : groups : post message to groups
"""
import requests
import present_function

headers = present_function.api_header()


def get_message(chat_id: str, post_type: str) -> dict:
    """
    Get a message from the chat
    Args:
        chat_id (str): chat_id of customer
        post_type (str): request contains

    Returns:
        dict: content (context)
    """
    params: dict = {
        "sortOrder": "desc",
        "limit": "1",
    }
    response: dict = requests.get(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        params=params,
        headers=headers,
        timeout=10,
    )
    return response


def get_variables(content: dict) -> tuple:
    """
    get_variables for functions

    Args:
        content (dict): post dictionary

    Returns:
        list: functions variables
    """
    user_name: str = content.get("refers").get("user")["profile"]["name"]
    user_goal: str = content.get("refers").get("user")["profile"]["goal"]
    return (user_name, user_goal)


def quote_present(chat_id: str, content: dict, post_type: str) -> requests:
    """
    Introduce gift (table)

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
    """
    user_name: str = get_variables(content)[0]
    json_data: dict = {
        "blocks": [
            {
                "type": "text",
                "value": f":gift: <b>[{user_name}]님</b>의 "
                + "<b>성공적인 다이어트</b>에\n    도움이 되는 "
                + "<b>식단표</b>를\n    <b>선물</b>로 드릴게요!.\n\n",
            }
        ]
    }
    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def quote_knowhow(chat_id: str, post_type: str) -> requests:
    """
    Quote for we have knowhow

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
    """
    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": ":sunglasses: <b>8년</b>간의 노하우와 데이터로 만든"
                + "\n    <b>가장 성공 확률이 높은</b>\n    <b>식단표</b>에요!",
            }
        ]
    }
    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def give_dining_schedule(chat_id: str, content: dict, post_type: str) -> requests:
    """
    give dining_schedule table
    """
    user_name: str = get_variables(content)[0]
    user_goal: str = get_variables(content)[1]
    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": f":calendar: <b>[{user_name}]님</b>에 "
                + "맞춘\n     <b>맞춤 식단표</b>에요!:v:",
            }
        ],
        "buttons": [
            {
                "title": "맞춤 식단표 받기",
                "colorVariant": "orange",
                "url": present_function.table(user_goal),
            }
        ],
    }
    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def quote_goal_success(chat_id: str, content: dict, post_type: str) -> requests:
    """
    Remind goal and table

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
    """
    user_goal: str = get_variables(content)[1]

    def add_string(user_goal: str) -> str:
        if "이상의 감량을" in user_goal:
            return "<b>5Kg 이상 감량</b>을"
        if "5Kg 미만" in user_goal:
            return "<b>5Kg 미만 감량</b>을"
        if "증량" in user_goal:
            return "<b>5Kg 이상 증량</b>을"
        return "<b>유지</b>를"

    add_response = add_string(user_goal)
    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": ":trophy: <b>식단표</b>를 잘 활용한다면 "
                + f"<b>3개월 이내</b>\n    {add_response} 달성할 수 있어요!",
            }
        ]
    }
    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def cheering_quote(chat_id: str, content: dict, post_type: str) -> requests:
    """
    Cheer message

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
    """
    user_name: str = get_variables(content)[0]
    user_goal: str = get_variables(content)[1]

    def add_string2(user_goal: str) -> str:
        if "이상의 감량을" in user_goal:
            return "<b>5Kg 이상 감량</b>"
        if "5Kg 미만" in user_goal:
            return "<b>5Kg 미만 감량</b>"
        if "증량" in user_goal:
            return "<b>5Kg 이상 증량</b>"
        return "<b>유지</b>"

    add_response2 = add_string2(user_goal)
    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": ":crossed_fingers: <b>윤식단이 "
                + f"[{user_name}]님의\n    {add_response2} 성공을 응원해요!",
            }
        ]
    }
    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def marketing_quote(chat_id: str, post_type: str) -> requests:
    """
    Selling a marketing message

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
    """
    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": ":ticket: 오늘 <b>22시까지 주문시</b>\n"
                + "    단돈 <b>6,800원</b>으로\n    <b>1:1 맞춤 식단</b>을 체험해보세요!",
            }
        ]
    }
    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def last_quote(chat_id: str, post_type: str) -> requests:
    """
    Message to start yun now

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
    """
    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": ":seedling: <b>[건강 관리의 시작은]</b>"
                + "\n    '<b>내일</b>'이 아닌"
                + "\n    '<b>지금</b>'시작해야 <b>성공</b>합니다.",
            }
        ]
    }
    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def give_link_event_salad(chat_id: str, post_type: str) -> requests:
    """
    link to purchase

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
    """
    json_data = {
        "blocks": [
            {"type": "text", "value": "      :corn: " + "<b>맞춤 식단 바로 주문하기</b>   "}
        ],
        "buttons": [
            {
                "title": "[이벤트] 맞춤 식단 프로그램 ",
                "colorVariant": "green",
                "url": "https://yundiet.com/shop_view/?idx=48",
            }
        ],
    }
    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def give_link_normal_salad(chat_id: str, post_type: str) -> requests:
    """
    link to purchase

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
    """
    json_data = {
        "blocks": [
            {"type": "text", "value": "      :corn: " + "<b>맞춤 식단 바로 주문하기</b>   "}
        ],
        "buttons": [
            {
                "title": "윤식단 맞춤 식단 프로그램 ",
                "colorVariant": "green",
                "url": "https://yundiet.com/store_all/?idx=66",
            }
        ],
    }
    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def final_quote(chat_id: str, post_type: str) -> requests:
    """
    The Final Introduction

    Args:
        chat_id (str): content.get('refers').get('message')['chatId']
    """

    json_data = {
        "blocks": [
            {"type": "text", "value": ":herb:\n"},
            {
                "type": "text",
                "value": "나에게 맞지 않는 식단은\n나에게 맞지 않는 옷과 같아요."
                + "\n\n요요가 생기거나, 폭식을 하거나"
                + "\n과도한 스트레스를 받는 문제가\n발생해요."
                + "\n\n영양소의 과다 공급을\n점진적으로 줄여가며"
                + "\n나에게 맞는 식단 관리를 시작하면"
                + "\n부작용 없이 건강한 내 모습을"
                + "\n만나 볼 수 있을거에요.\n\n",
            },
            {
                "type": "text",
                "value": "건강을 관리하는 것은\n벽돌을 쌓는 것과 같아요."
                + "\n\n조금 느리더라도 단단하게 쌓아\n무너지지 않게 하는 것이\n가장 중요하죠."
                + "\n\n체중을 빨리 감량하는 것 보다,"
                + "\n감량한 체중을 오래 유지하는 것이\n더욱 중요합니다."
                + "\n\n건강관리, 아직 늦지 않았어요.\n<b>윤식단</b>과 함께 지금부터라도"
                + "\n시작해 보세요!:grinning:",
            },
        ]
    }
    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )
