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
import datetime
import logging
from flask import Flask, request, render_template
from MainCuration import main_curation
from PresentCuration import present_curation
from RefundCalculator import refund_calculator
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
def open_userchat():

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

    def refund_calculator_operator(content:dict) -> str:
        """
        operation refund calculator
        """
        try:
            refund_calculator.refund_calculator(content)
            
        except TypeError as type_error:
            print(f"DATETIME : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            logging.warning("Exception Name: %s", type(type_error).__name__)
            logging.warning("Exception Desc: %s", {type_error})            
        except NameError as name_error:
            logging.warning("Exception Name: %s", type(name_error).__name__)
            logging.warning("Exception Desc: %s", {name_error})
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
    
    refund_calculator_thread = threading.Thread(
        target=refund_calculator_operator, kwargs={"content": content}
    )
    refund_calculator_thread.start()

    return 'open_userchat successfully operated'


@app.route("/in_userchat", methods=["GET", "POST"])
def in_userchat():
    """
    Present curation
    Operation after say 'complete'
    """

    def present_curation_operator(content):
        """
        operation present_curation
        """
        try:
            present_curation.present_curation(content)

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

    present_curation_thread = threading.Thread(
        target=present_curation_operator, kwargs={"content": content}
    )
    present_curation_thread.start()

    return 'in_userchat successfully operated!'


if __name__ == "__main__":
    app.run(port=80, debug=True)
