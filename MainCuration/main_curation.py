"""
main_curation operating py
"""

import logging
import time
import datetime
from MainCuration import main_response


def main_curation(content):
    """
    functinos for main curation

    Args:
        content (str): chat_id : UserChat ID
    Returns:
        check this main_curation is operated on url
    """
    try:
        if content["entity"]["source"]["supportBot"]["id"] in [
            "Number of support bots",
        ]:
            if content["entity"]["tags"][0] == "TEXT": # condtion for operating
                chat_id: str = content.get("refers").get("message")["chatId"]
                post_type: str = "user-chats"
                
                # time.sleep will be need it to make support bot seems like human response
                time.sleep(2)
                main_response.introduction1(chat_id, post_type)
                
                # ... so on
                
            else:
                pass

    except ValueError as value_error:
        print(f"DATETIME : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logging.warning("Exception Name: %s", type(value_error).__name__)
        logging.warning("Exception Desc: %s", {value_error})

        # ... so on