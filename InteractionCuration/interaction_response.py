"""
present curation Responses
<content direction>
chat_id (str): content.get('refers').get('message')['chatId']
post_type (str) : groups : post message to groups
"""
import requests
from InteractionCuration import interaction_functions

headers = interaction_functions.api_header()

def get_message(chat_id: str, post_type: str) -> dict:
    """
    Get a message from the chat
    Different between maincuration and interaction_functions to get a content
    
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

def quote_example(chat_id: str, content: dict, post_type: str) -> requests:
    """

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
    """

    json_data: dict = {
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

