"""
Functions for refund calca
API header and included calculation functions

<content direction>
"""
import datetime
import math
import json


def api_header() -> dict:
    """
    Returns for API key and pwd

    Args: None
    Return:
        Dictionary headers for API request
    """
    with open("API_key.json", "r", encoding="utf-8") as api_json:
        api = json.load(api_json)
    key: str = api.get("x-access-key")
    pwd: str = api.get("x-access-secret")
    headers: dict = {
        "accept": "application/json",
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        "x-access-key": f"{key}",
        "x-access-secret": f"{pwd}",
    }
    return headers


def get_refund_variables(temp_refund_menu: str) -> tuple:
    """
    get_refund_variables for reseponse
    Args:
        temp_refund_menu (str): menu name

    Returns:
        tuple: variables
    """
    now: datetime = datetime.datetime.now()
    days: list = ["월요일", "화요ㅈ일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    now_day_name: str = days[now.weekday()]
    now_weekday: int = now.weekday()
    now_hour: int = now.hour
    delivery_cost: int = 2500
    salad_cost: int = 8900
    option_cost: int = 0
    product_cost: int = int(
        temp_refund_menu.split("(")[1].split("원)")[0].replace(",", "")
    )
    dining_count: int = int(temp_refund_menu.split("식")[0][-1])
    return (
        now,
        days,
        now_day_name,
        now_weekday,
        now_hour,
        delivery_cost,
        salad_cost,
        option_cost,
        product_cost,
        dining_count,
    )


def get_option_cost(temp_refund_option: list, option_cost: int) -> int:
    """
    get option cost by selecting options
    """
    for option in temp_refund_option:
        if option == "없음":
            option_cost = 0
            break
        if option == "단백질 추가 (50g)":
            option_cost += 700

        if option == "단백질 추가 (100g)":
            option_cost += 1400

        if option == "탄수화물 추가 (50g)":
            option_cost += 500

        if option == "탄수화물 추가 (100g)":
            option_cost += 1000

    return option_cost


def mon_wed(
    now_weekday: int, now_hour: int, temp_refund_count: int, dining_count: int
) -> tuple:
    """
    get quote and temp_refund_count from selecting delivery
    """
    if now_weekday == 0 and now_hour >= 16:
        cat: str = "수요일것까지"
        temp_refund_count += dining_count

    elif now_weekday == 1:
        cat: str = "수요일것까지"
        temp_refund_count += dining_count

    elif now_weekday == 5 and now_hour >= 16:
        cat: str = "다음주 월요일까지"
        temp_refund_count += dining_count

    elif now_weekday == 6:
        cat: str = "다음주 월요일까지"
        temp_refund_count += dining_count
    else:
        cat: str = ""
    return cat, temp_refund_count


def tue_thu(
    now_weekday: int, now_hour: int, temp_refund_count: int, dining_count: int
) -> tuple:
    """
    get quote and temp_refund_count from selecting delivery
    """
    if now_weekday == 0:
        cat: str = "화요일것까지"
        temp_refund_count += dining_count

    if now_weekday == 1 and now_hour >= 16:
        cat: str = "목요일것까지"
        temp_refund_count += dining_count

    if now_weekday == 2:
        cat: str = "목요일것까지"
        temp_refund_count += dining_count

    elif now_weekday == 6 and now_hour >= 16:
        cat: str = "다음주 화요일까지"
        temp_refund_count += dining_count

    else:
        cat: str = ""
    return cat, temp_refund_count


def add_temp_refund_count(
    now_weekday: int,
    now_hour: int,
    temp_refund_delivery: str,
    temp_refund_count: int,
    dining_count: int,
) -> tuple:
    """
    Total get quote and temp_refund_count from selecting delivery.
    """
    if temp_refund_delivery == "월요일 / 수요일":
        cat, temp_refund_count = mon_wed(
            now_weekday, now_hour, temp_refund_count, dining_count
        )
    if temp_refund_delivery == "화요일 / 목요일":
        cat, temp_refund_count = tue_thu(
            now_weekday, now_hour, temp_refund_count, dining_count
        )
    return cat, temp_refund_count


def calculate_refund(
    temp_refund_option: str,
    temp_refund_count: int,
    dining_count: int,
    option_cost: int,
    salad_cost: int,
    delivery_cost: int,
    product_cost: int,
):
    """
    Total functions for calculating refund
    """
    option_cost: int = get_option_cost(temp_refund_option, option_cost)
    total_salad_cost: int = int(salad_cost * temp_refund_count)
    total_option_cost: int = int(option_cost * temp_refund_count)
    recieve_delivery_count: int = math.ceil(temp_refund_count / (dining_count * 2))
    total_delivery_cost: int = int(recieve_delivery_count * delivery_cost)
    total_re_purchase_cost: int = (
        total_salad_cost + total_option_cost + total_delivery_cost
    )
    refund_cost: int = product_cost - total_re_purchase_cost
    return (
        total_salad_cost,
        total_option_cost,
        recieve_delivery_count,
        total_delivery_cost,
        total_re_purchase_cost,
        refund_cost,
    )
