"""
Flask for curation application

main_response - main functions
present_response - present functions

All functions are defined in the *_functions.py

nohup.out is showed about log

app can start with code below to
`nohup flask run --host=0.0.0.0 &`

nohup can run this app on background

check app if is running on background,
`lsof -i :5000`

if stop this app or change code, you should stop this app and restart
`kill -9 pid_number`
"""

import threading
import json
import time
import datetime
import logging
from flask import Flask, request, render_template
import main_response
import present_response

app = Flask(__name__)


@app.route("/")
def home():
    """
    Flask homepage for testing

    Args:
        None

    Returns:
        rendering template
    """
    return render_template("index.html")


@app.route("/main_curation", methods=["GET", "POST"])
def main_curation():

    """
    Main curation
    Operation after survey.
    """

    def auto(content: dict) -> str:
        """
        auto functinos for main curation

        Args:
            content (str): chat_id : UserChat ID
        Returns:
            check this main_curation is operated on url
        """
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

    if request.method == "GET":
        content = request.args.to_dict()
    elif request.method == "POST":
        if request.is_json is True:
            content = request.get_json()
        else:
            content = request.form.to_dict()

    thread = threading.Thread(target=auto, kwargs={"content": content})
    thread.start()

    return "main_curation successfully operated"


@app.route("/curation_presents", methods=["GET", "POST"])
def curation_present():
    """
    Present curation
    Operation after say 'complete'
    """

    def auto(content):
        """
        auto functinos for present curation

        Args:
            content (str): chat_id : UserChat ID
        """

        chat_id = content["entity"]["chatId"]
        post_type = "user-chats"
        try:
            if content["refers"]["userChat"]["source"]["supportBot"]["id"] in [
                "51767",
                "43684",
                "47423",
            ]:
                if content["entity"]["plainText"] == "선물":
                    chat_id = content["entity"]["chatId"]
                    post_type = "user-chats"
                    response = present_response.get_message(chat_id, post_type)
                    content = json.loads(response.content)
                    try:
                        time.sleep(2)
                        present_response.quote_present(chat_id, content, post_type)
                        time.sleep(2)
                        present_response.quote_knowhow(chat_id, post_type)
                        time.sleep(2)
                        present_response.give_dining_schedule(
                            chat_id, content, post_type
                        )
                        time.sleep(2)
                        present_response.quote_goal_success(chat_id, content, post_type)
                        time.sleep(2)
                        present_response.cheering_quote(chat_id, content, post_type)
                        time.sleep(2)
                        present_response.marketing_quote(chat_id, post_type)
                        time.sleep(2)
                        present_response.last_quote(chat_id, post_type)
                        time.sleep(2)
                        present_response.give_link_event_salad(chat_id, post_type)
                        time.sleep(2)
                        present_response.final_quote(chat_id, post_type)
                    except TypeError as type_mid_error:
                        logging.warning(
                            "Exception Name: %s", type(type_mid_error).__name__
                        )
                        logging.warning("Exception Desc: %s", {type_mid_error})

        except TypeError as type_error:
            print(f"DATETIME : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            logging.warning("Exception Name: %s", type(type_error).__name__)
            logging.warning("Exception Desc: %s", {type_error})

        except KeyError as key_error:
            print(f"DATETIME : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            logging.warning("Exception Name: %s", type(key_error).__name__)
            logging.warning("Exception Desc: %s", {key_error})

    if request.method == "GET":
        content = request.args.to_dict()
    elif request.method == "POST":
        if request.is_json is True:
            content = request.get_json()
        else:
            content = request.form.to_dict()

    thread = threading.Thread(target=auto, kwargs={"content": content})
    thread.start()

    return "curation_presents successfully operated!"


if __name__ == "__main__":
    app.run(port=80, debug=True)
