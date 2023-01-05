"""
interaction_curation operating py
"""
import json
import time
import logging
import datetime
from InteractionCuration import interaction_response


def interaction_curation(content):
    """
    auto functinos for present curation

    Args:
        content (str): chat_id : UserChat ID
    """

    chat_id = content["entity"]["chatId"]
    post_type = "user-chats"
    try:
        if content["refers"]["userChat"]["source"]["supportBot"]["id"] in [
            "Number of support bots",
        ]:  # Specify which support bot to use.
            
            if content["entity"]["plainText"] == "TEXT": # Condition for operating
                chat_id = content["entity"]["chatId"]
                post_type = "user-chats"
                
                # Differnce between MainCuration (open_userchat) to get content
                response = interaction_response.get_message(chat_id, post_type)
                content = json.loads(response.content)
                
                try:
                    # time.sleep will be need it to make support bot seems like human response
                    time.sleep(2)
                    interaction_response.quote_example(chat_id, content, post_type)
                    
                    # ... so on
                    
                except TypeError as type_mid_error:
                    logging.warning("Exception Name: %s", type(type_mid_error).__name__)
                    logging.warning("Exception Desc: %s", {type_mid_error})
                    
                    # ... so on

    except TypeError as type_error:
        print(f"DATETIME : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logging.warning("Exception Name: %s", type(type_error).__name__)
        logging.warning("Exception Desc: %s", {type_error})
        
        # ... so on

    except KeyError as key_error:
        print(f"DATETIME : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logging.warning("Exception Name: %s", type(key_error).__name__)
        logging.warning("Exception Desc: %s", {key_error})
        
        # ... so on
