"""
refund_calculator operating py
"""
import logging
import time
import datetime
from RefundCuration import refund_response


def refund_curation(content):
    """
    auto functinos for refund_calculator

    Args:
        content (str): chat_id : UserChat ID
    """

    try:
        if content["entity"]["source"]["supportBot"]["id"] in [
            "51767",
            "43684",
            "47423",
        ]:
            if content["entity"]["tags"][0] == "환불결제조회":
                chat_id = content.get("refers").get("message")["chatId"]
                post_type = "user-chats"
                time.sleep(2)
                refund_response.refund_response_introduction1(chat_id, post_type)
                time.sleep(2)
                refund_response.refund_response_introduction2(chat_id, post_type)
                time.sleep(2)
                refund_response.refund_response1(chat_id, content, post_type)
                time.sleep(2)
                refund_response.refund_response2(chat_id, content, post_type)
                time.sleep(2)
                refund_response.refund_response3(chat_id, content, post_type)
                time.sleep(2)
                refund_response.refund_response4(chat_id, content, post_type)
                time.sleep(2)
                refund_response.refund_response5(chat_id, content, post_type)
                time.sleep(2)
                refund_response.refund_response6(chat_id, post_type)
    except ValueError as value_error:
        logging.warning("RESPONSE Refund ERROR OCCURED")
        print(f"DATETIME : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logging.warning("Exception Name: %s", type(value_error).__name__)
        logging.warning("Exception Desc: %s", {value_error})
    else:
        logging.warning("RESPONSE Refund ERROR OCCURED - else")
