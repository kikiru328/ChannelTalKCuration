"""
Functions for Present curation
API header and included calculation functions

<content direction>
user_goal (int): content.get('refers').get('user')['profile']['goal'] (목표량)
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

# ... and so on
# make functions for response value