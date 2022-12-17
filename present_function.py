"""
Functions for Present curation
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


def table(user_goal: str) -> str:
    """
    giving table to customer by user_goal

    Args:
        str, 목표향

    Returns:
        str, table image url
    """
    url: str = "http://3.38.103.219:5000/static/img"
    if "이상의 감량을" in user_goal:
        return f"{url}/more_5_reduce.png"
    if "5Kg 미만" in user_goal:
        return f"{url}/less_5_reduce.png"
    if "증량" in user_goal:
        return f"{url}/gain_5.png"
    return f"{url}/maintain.png"
