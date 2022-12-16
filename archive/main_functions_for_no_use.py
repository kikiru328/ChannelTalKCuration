"""
***
Here, main_functions is for <main_no_use_response>
***
Functions for Main curation.
API header and included calculation functions

<content direction>
user_name (str): content.get('refers').get('user')['profile']['name'] (이름))
user_hydrate (str): content.get('refers').get('user')['profile']['hydrate'] (수분섭취량)
user_weight (str): content.get('refers').get('user')['profile']['weight'] (몸무게)
user_height (int): content.get('refers').get('user')['profile']['height'] (신장)
user_age (int): content.get('refers').get('user')['profile']['age'] (나이)
user_activation (str): content.get('refers').get('user')['profile']['activation'] (활동량)
user_goal (int): content.get('refers').get('user')['profile']['goal'] (목표량)
user_dining (str): content.get('refers').get('user')['profile']['number_dining'] (식사횟수)
"""

import json


def api_header() -> dict:
    """
    Returns for API key and pwd

    Args: None
    Return:
        Dictionary headers for API request
    """
    with open("API_key.json", "r", encoding="utf-8") as api_json:
        api = json.load(api_json)
    key: str = api.get("x-access-key")
    pwd: str = api.get("x-access-secret")
    headers: dict = {
        "accept": "application/json",
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        "x-access-key": f"{key}",
        "x-access-secret": f"{pwd}",
    }
    return headers


def get_bmr(user_weight: int, user_height: int, user_age: int) -> int:

    """BMR : 기초대사량 계산

    Args:
        user_weight : int, 몸무게
        user_height : int, 신장
        user_age : int, 나이
    Returns:
        BMR : int , activation_calculation parameter ( trunc )
    """
    return int(66 + (13.7 * user_weight) + (5 * user_height) - (6.8 * user_age))


def get_cal_by_activation(user_activation: str, bmr: int) -> int:
    """_summary_

    Args:
        user_activation : str, 활동량
        bmr : int, return by `get_bmr`

    Returns:
        maintenance : int , goal_calculation parameter ( trunc )
    """
    if user_activation == "거의 없다 (주1회이하)":
        return int(bmr * 1.2)
    if user_activation == "보통 (주2~4회)":
        return int(bmr * 1.375)
    if user_activation == "많다(주5~7회)":
        return int(bmr * 1.55)
    return int(bmr * 1.725)


def get_cal_for_goal(user_goal: str, maintenance: int) -> int:
    """_summary_

    Args:
        user_goal : str, 목표량
        maintenance : int, Calculation by return of activation_calculation functions

    Returns:
        goal_calories : int > macro_calucation parameter ( trunc )
    """
    if user_goal == "5Kg 이상의 감량을 원하세요?":
        return int(maintenance * 0.8)
    if user_goal == "5Kg 미만의 감량을 원하세요?":
        return int(maintenance * 0.9)
    if user_goal == "5kg 이상의 증량을 원하세요?":
        return int(maintenance * 1.1)
    return int(maintenance)


def get_macro_cal(goal_calories: int) -> list:
    """_summary_

    Args:
        goal_calories (int): Calculation by goal_calculation functions

    Returns:
        _type_: carbon/protein/fat by gram  int ( trunc )
    """
    carbohydrate: int = int(goal_calories * 0.5 / 4)
    protein: int = int(goal_calories * 0.3 / 4)
    fat: int = int(goal_calories * 0.2 / 9)
    return carbohydrate, protein, fat
