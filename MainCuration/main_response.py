"""
Main curation Responses
<content direction>
chat_id (str): content.get('refers').get('message')['chatId']
post_type (str) : groups : post message to groups
"""
import requests
from MainCuration import main_function

headers = main_function.api_header()

def quote_example(chat_id: str, post_type: str) -> requests:
    """_summary_

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
    """
    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": "Write down the message."
            }
        ]
    }

    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )