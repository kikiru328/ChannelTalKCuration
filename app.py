"""
Flask for curation application.
This is process modularization

start by

    nohup.out is showed about log

    app can start with code below to
    `nohup flask run --host=0.0.0.0 &`

    nohup can run this app on background

    check app if is running on background,
    `lsof -i :5000`

    if stop this app or change code, you should stop this app and restart
    `kill -9 pid_number`

    response > change response
    
"""

import threading
import datetime
import logging
from flask import Flask, request, render_template
from MainCuration import main_curation
from InteractionCuration import interaction_curation
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


@app.route("/open_userchat", methods=["GET", "POST"])
def open_userchat(): # when user-chat is available (open)

    """
    Main curation
    Operation after survey.
    """

    def main_curation_operator(content: dict) -> str:
        """
        operation main_curation
        """
        try:
            main_curation.main_curation(content)

        except ValueError as value_error:
            logging.warning("Exception Name: %s", type(value_error).__name__)
            logging.warning("Exception Desc: %s", {value_error})
        else:
            logging.warning("MAIN_EXCEPTION")


    if request.method == "GET":
        content = request.args.to_dict()
    elif request.method == "POST":
        if request.is_json is True:
            content = request.get_json()
        else:
            content = request.form.to_dict()

    main_curation_thread = threading.Thread(
        target=main_curation_operator, kwargs={"content": content}
    )
    main_curation_thread.start()
    
    return 'open_userchat successfully operated'


@app.route("/in_userchat", methods=["GET", "POST"])
def in_userchat(): # when user sends a message and chat in progress
    """
    Present curation
    Operation after say 'complete'
    """
    def Interaction_curation_operater(content):
        """
        operation Interaction_curation
        """
        try:
            interaction_curation.interaction_curation(content)

        except TypeError as type_error:
            print(f"DATETIME : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            logging.warning("Exception Name: %s", type(type_error).__name__)
            logging.warning("Exception Desc: %s", {type_error})

        except KeyError as key_error:
            print(f"DATETIME : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            logging.warning("Exception Name: %s", type(key_error).__name__)
            logging.warning("Exception Desc: %s", {key_error})

        else:
            logging.warning("MAIN_EXCEPTION")

    if request.method == "GET":
        content = request.args.to_dict()
    elif request.method == "POST":
        if request.is_json is True:
            content = request.get_json()
        else:
            content = request.form.to_dict()

    interaction_curation_thred = threading.Thread(
        target=Interaction_curation_operater, kwargs={"content": content}
    )
    interaction_curation_thred.start()

    return 'in_userchat successfully operated!'


if __name__ == "__main__":
    app.run(port=80, debug=True)
