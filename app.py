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

from flask import Flask, request, render_template
import main_response
import present_response
import threading
import json
import time

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

    Args:
        None
    """

    def auto(content: dict) -> str:
        """
        auto functinos for main curation

        Args:
            content (str): chat_ID : UserChat ID
            +) Tags : Only for curation
            +) thread : Webhook for flask

        Returns:
            check this main_curation is operated on url
        """
        try:
            if (
                content["entity"]["source"]["supportBot"]["id"] == "51767"
                or "43684"
                or "47423"
            ):
                if content["entity"]["tags"][0] == "식단큐레이션받기":
                    chat_ID: str = content.get("refers").get("message")["chatId"]
                    post_type: str = "user-chats"
                    thirdparty: str = content.get("refers").get("user")["profile"][
                        "thirdPartyAgree"
                    ]
                    if thirdparty != True:
                        pass
                    else:
                        time.sleep(2)
                        main_response.Introduction1(chat_ID, content, post_type)
                        time.sleep(2)
                        main_response.Introduction2(chat_ID, content, post_type)
                        time.sleep(2)
                        main_response.Introduction3(chat_ID, content, post_type)
                        time.sleep(2)
                        main_response.Introduction4(chat_ID, content, post_type)
                        time.sleep(2)
                        main_response.Introduction5(chat_ID, content, post_type)
                        time.sleep(2)
                        main_response.Introduction6(chat_ID, content, post_type)
                        time.sleep(2)
                        main_response.Introduction7(chat_ID, content, post_type)
                        time.sleep(2)
                        main_response.Activation_food_amount(
                            chat_ID, content, post_type
                        )
                        time.sleep(2)
                        main_response.Calories_per_dining(chat_ID, content, post_type)
                        time.sleep(2)
                        main_response.Before_form(chat_ID, content, post_type)
                        time.sleep(2)
                        main_response.RESET(chat_ID, content, post_type)
                else:
                    pass
        except Exception as e:
            print("RESPONSE MAIN ERROR OCCURED")
            print(f"DATETIME : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(e)
            print()

    if request.method == "GET":
        content = request.args.to_dict()
    elif request.method == "POST":
        if request.is_json is True:
            content = request.get_json()
        else:
            content = request.form.to_dict()

    """스레드 실행"""
    thread = threading.Thread(target=auto, kwargs={"content": content})
    thread.start()

    return "main_curation successfully operated"


@app.route("/curation_presents", methods=["GET", "POST"])
def curation_present():

    """자동화 작업 함수"""

    def auto(content):
        """_summary_

        Args:
            content (str): chat_ID : UserChat ID
            +) Tags : Only for curation
            +) thread : Webhook for flask
        """
        import time
        import second_response

        chat_ID = content["entity"]["chatId"]
        post_type = "user-chats"
        try:
            user_name = content["refers"]["user"]["profile"]["name"]
        except:
            pass
        print("PRESENT")
        print(content)
        try:
            if (
                content["refers"]["userChat"]["source"]["supportBot"]["id"] == "51767"
                or "43684"
                or "47423"
            ):
                if content["entity"]["plainText"] == "선물":
                    import time

                    chat_ID = content["entity"]["chatId"]
                    post_type = "user-chats"
                    import second_response

                    response = second_response.GET_MSG(chat_ID, post_type)
                    contents = json.loads(response.content)
                    try:
                        import time

                        time.sleep(2)
                        second_response.present(chat_ID, content, post_type)
                        time.sleep(2)
                        second_response.knowhow(chat_ID, content, post_type)
                        time.sleep(2)
                        second_response.Dining_Schedule(chat_ID, content, post_type)
                        time.sleep(2)
                        second_response.goal_success(chat_ID, content, post_type)
                        time.sleep(2)
                        second_response.yun_cheer(chat_ID, content, post_type)
                        time.sleep(2)
                        second_response.marketing(chat_ID, content, post_type)
                        time.sleep(2)
                        second_response.last_quote(chat_ID, content, post_type)
                        time.sleep(2)
                        second_response.event_salad(chat_ID, content, post_type)
                        time.sleep(2)
                        second_response.Final_Introduction(chat_ID, post_type)
                    except Exception as e:
                        time.sleep(2)
                        second_response.Final_Introduction(chat_ID, post_type)
                        time.sleep(1)
                        second_response.normal_salad(chat_ID, content, post_type)
                else:
                    time.sleep(2)
                    second_response.wrong_answer(chat_ID, post_type)
        except Exception as e:
            print("PRESENT ERROR OCCURED")
            print(f"DATETIME : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(e)
            print()

    if request.method == "GET":
        content = request.args.to_dict()
    elif request.method == "POST":
        if request.is_json is True:
            content = request.get_json()
        else:
            content = request.form.to_dict()

    """스레드 실행"""
    thread = threading.Thread(target=auto, kwargs={"content": content})
    thread.start()

    return "curation_presents successfully operated!"


@app.route("/delivery_curation", methods=["GET", "POST"])
def delivery_():
    def auto(content):
        print("####DELIVERY####", content)
        """_summary_

        Args:
            content (str): chat_ID : UserChat ID
            +) Tags : Only for curation
            +) thread : Webhook for flask
            
        """
        import time
        import present_response

        chat_ID = content["entity"]["chatId"]
        post_type = "user-chats"
        import delivery_date
        import datetime

        now = datetime.datetime.now()
        holiday_dataframe = delivery_date.holiday_dataframe
        print("######### NOW ##########", now)
        time.sleep(0.68)
        try:
            if content["refers"]["userChat"]["source"]["supportBot"]["id"] == "52853":
                if content["entity"]["plainText"] == "새벽배송":
                    delivery_date.get_delivery_start_date_each.get_deliv_start_date(
                        chat_ID, post_type, now, holiday_dataframe, "새벽배송"
                    )
                elif content["entity"]["plainText"] == "일반배송":
                    delivery_date.get_delivery_start_date_each.get_deliv_start_date(
                        chat_ID, post_type, now, holiday_dataframe, "일반배송"
                    )
                elif content["entity"]["plainText"] == "직접배송":
                    delivery_date.get_delivery_start_date_each.get_deliv_start_date(
                        chat_ID, post_type, now, holiday_dataframe, "직접배송"
                    )
        except:
            pass

    if request.method == "GET":
        content = request.args.to_dict()
    elif request.method == "POST":
        if request.is_json is True:
            content = request.get_json()
        else:
            content = request.form.to_dict()

    """스레드 실행"""
    thread = threading.Thread(target=auto, kwargs={"content": content})
    thread.start()

    return "delivery_curation successfully operated!"


if __name__ == "__main__":
    app.run(port=80, debug=True)
