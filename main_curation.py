def main_curation(content):
    import logging
    import main_response
    import time
    import datetime
    try:
        if content["entity"]["source"]["supportBot"]["id"] in [
            "51767",
            "43684",
            "47423",
        ]:
            if content["entity"]["tags"][0] == "식단큐레이션받기":
                chat_id: str = content.get("refers").get("message")["chatId"]
                post_type: str = "user-chats"
                thirdparty: str = content.get("refers").get("user")["profile"][
                    "thirdPartyAgree"
                ]
                if thirdparty is True:
                    time.sleep(2)
                    main_response.introduction1(chat_id, post_type)
                    time.sleep(2)
                    main_response.introduction2(chat_id, content, post_type)
                    time.sleep(2)
                    main_response.introduction3(chat_id, post_type)
                    time.sleep(2)
                    main_response.introduction4(chat_id, content, post_type)
                    time.sleep(2)
                    main_response.introduction5(chat_id, content, post_type)
                    time.sleep(2)
                    main_response.introduction6(chat_id, post_type)
                    time.sleep(2)
                    main_response.introduction7(chat_id, content, post_type)
                    time.sleep(2)
                    main_response.get_food_amount(chat_id, content, post_type)
                    time.sleep(2)
                    main_response.cal_per_dining(chat_id, content, post_type)
                    time.sleep(2)
                    main_response.before_form(chat_id, content, post_type)
                    time.sleep(2)
                    main_response.question_present(chat_id, content, post_type)
            else:
                pass

    except ValueError as value_error:
        print(f"DATETIME : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logging.warning("Exception Name: %s", type(value_error).__name__)
        logging.warning("Exception Desc: %s", {value_error})