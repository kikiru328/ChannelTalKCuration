"""
refund calculator Responses
<content direction>
chat_id (str): content.get('refers').get('message')['chatId']
post_type (str) : groups : post message to groups
"""

import requests
from RefundCuration import refund_function


def refund_response_introduction1(chat_id, post_type):
    """
    refund_calculator Reseponse by step

    Args:
        chat_id (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """

    headers = refund_function.api_header()
    json_data = {
        "blocks": [
            {"type": "text", "value": "<b>고객님, 안녕하세요</b>\n이용에 만족을 드리지 못해\n진심으로 죄송합니다."}
        ]
    }

    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )



def refund_response_introduction2(chat_id, post_type):
    """
    refund_calculator Reseponse by step

    Args:
        chat_id (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """

    headers = refund_function.api_header()
    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": "윤식단 정기배송 중단시,"
                + "\n남은기간 100% 위약금 없이"
                + "\n환불이 가능합니다."
                + "\n\n단, 처음 결제하신 <b>기존 주문건은 전체 환불 처리</b>되며"
                + "\n환불 요청 시점을 기준으로"
                + "\n<b>진행기간에 비례한</b>"
                + "\n<b>단품 원가 재결재</b>가 진행됩니다."
                + "\n\n"
                + "또한 <b>정기배송 중단 요청으로 환불시</b>"
                + "\n<b>재결재는 샐러드 단품 원가가"
                + "\n적용되어 계산됩니다.</b>"
                + "\n(1팩당 8,900원, \n배송회수 당 2,500원 적용)"
                + "\n\n<b>단, 환불 재결재 금액이 기존 결제 금액을 초과할 경우 환불 진행이 어렵습니다.</b>",
            }
        ]
    }

    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )



def refund_response1(chat_id, content, post_type):
    """
    refund_calculator Reseponse by step

    Args:
        chat_id (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """

    headers = refund_function.api_header()
    temp_refund_menu = content.get("refers").get("user")["profile"]["temp_refund_menu"]
    temp_refund_count = content.get("refers").get("user")["profile"][
        "temp_refund_count"
    ]
    temp_refund_option = content.get("refers").get("user")["profile"][
        "temp_refund_option"
    ]
    temp_refund_delivery = content.get("refers").get("user")["profile"][
        "temp_refund_delivery"
    ]

    now = refund_function.get_refund_variables(temp_refund_menu)[0]
    now_weekday = refund_function.get_refund_variables(temp_refund_menu)[3]
    now_hour = refund_function.get_refund_variables(temp_refund_menu)[4]
    product_cost = refund_function.get_refund_variables(temp_refund_menu)[8]
    dining_count = refund_function.get_refund_variables(temp_refund_menu)[9]

    _, temp_refund_count = refund_function.add_temp_refund_count(
        now_weekday, now_hour, temp_refund_delivery, temp_refund_count, dining_count
    )

    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": "현재 고객님의 환불 내역 정보를"
                + "\n바탕으로 계산을 진행하겠습니다."
                + "\n\n"
                + "고객님께서 구매하신 상품은"
                + f"\n<b>[{temp_refund_menu.split('(')[0]}]</b> 이며"
                + "\n\n"
                + f"가격은 <b>[{product_cost}원]</b> 입니다."
                + "\n\n"
                + "추가하신 옵션사항은"
                + f"\n<b>{temp_refund_option}</b> 입니다."
                + "\n\n"
                + f"배송주기는 <b>[{temp_refund_delivery}]</b> 입니다."
                + "\n\n"
                + "환불금액 조회시각은 현재"
                + f"\n<b>[{now.strftime('%Y-%m-%d %H:%M')}]</b>입니다.",
            }
        ]
    }

    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )



def refund_response2(chat_id, content, post_type):
    """
    refund_calculator Reseponse by step

    Args:
        chat_id (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """

    headers = refund_function.api_header()
    temp_refund_menu = content.get("refers").get("user")["profile"]["temp_refund_menu"]
    temp_refund_count = content.get("refers").get("user")["profile"][
        "temp_refund_count"
    ]
    temp_refund_delivery = content.get("refers").get("user")["profile"][
        "temp_refund_delivery"
    ]

    now_weekday = refund_function.get_refund_variables(temp_refund_menu)[3]
    now_hour = refund_function.get_refund_variables(temp_refund_menu)[4]
    dining_count = refund_function.get_refund_variables(temp_refund_menu)[9]

    cat, temp_refund_count = refund_function.add_temp_refund_count(
        now_weekday, now_hour, temp_refund_delivery, temp_refund_count, dining_count
    )
    if cat != "":
        cat_response = f"다음 제조가 진행중에 있어\n<b>[{cat}</b> {dining_count} 개]의 수량이 추가됩니다."

    else:
        cat_response = "다음 제조 예정이 없기 때문에\n수량이 추가되지 않습니다."
    json_data = {
        "blocks": [{"type": "text", "value": "현재 환불금액 조회시간에 따라" + f"\n{cat_response}"}]
    }

    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )



def refund_response3(chat_id, content, post_type):
    """
    refund_calculator Reseponse by step

    Args:
        chat_id (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """

    headers = refund_function.api_header()
    temp_refund_menu = content.get("refers").get("user")["profile"]["temp_refund_menu"]
    temp_refund_count = content.get("refers").get("user")["profile"][
        "temp_refund_count"
    ]
    temp_refund_option = content.get("refers").get("user")["profile"][
        "temp_refund_option"
    ]
    temp_refund_delivery = content.get("refers").get("user")["profile"][
        "temp_refund_delivery"
    ]

    now_weekday = refund_function.get_refund_variables(temp_refund_menu)[3]
    now_hour = refund_function.get_refund_variables(temp_refund_menu)[4]
    delivery_cost = refund_function.get_refund_variables(temp_refund_menu)[5]
    salad_cost = refund_function.get_refund_variables(temp_refund_menu)[6]
    option_cost = refund_function.get_refund_variables(temp_refund_menu)[7]
    product_cost = refund_function.get_refund_variables(temp_refund_menu)[8]
    dining_count = refund_function.get_refund_variables(temp_refund_menu)[9]

    _, temp_refund_count = refund_function.add_temp_refund_count(
        now_weekday, now_hour, temp_refund_delivery, temp_refund_count, dining_count
    )
    recieve_delivery_count = refund_function.calculate_refund(
        temp_refund_option,
        temp_refund_count,
        dining_count,
        option_cost,
        salad_cost,
        delivery_cost,
        product_cost,
    )[2]

    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": "환불금액 조회시간에 따른 샐러드는\n 다음과 같습니다."
                + "\n\n"
                + f"\n1회 배송당 수령 샐러드 개수 : <b>[{dining_count} 개]</b>"
                + f"\n총 수령 샐러드 개수 : <b>[{temp_refund_count} 개]</b> "
                + f"\n총 배송회수 : <b>[{recieve_delivery_count} 회]</b>",
            }
        ]
    }

    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )



def refund_response4(chat_id, content, post_type):
    """
    refund_calculator Reseponse by step

    Args:
        chat_id (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """

    headers = refund_function.api_header()
    temp_refund_menu = content.get("refers").get("user")["profile"]["temp_refund_menu"]
    temp_refund_count = content.get("refers").get("user")["profile"][
        "temp_refund_count"
    ]
    temp_refund_option = content.get("refers").get("user")["profile"][
        "temp_refund_option"
    ]
    temp_refund_delivery = content.get("refers").get("user")["profile"][
        "temp_refund_delivery"
    ]

    now_weekday = refund_function.get_refund_variables(temp_refund_menu)[3]
    now_hour = refund_function.get_refund_variables(temp_refund_menu)[4]
    delivery_cost = refund_function.get_refund_variables(temp_refund_menu)[5]
    salad_cost = refund_function.get_refund_variables(temp_refund_menu)[6]
    option_cost = refund_function.get_refund_variables(temp_refund_menu)[7]
    product_cost = refund_function.get_refund_variables(temp_refund_menu)[8]
    dining_count = refund_function.get_refund_variables(temp_refund_menu)[9]

    _, temp_refund_count = refund_function.add_temp_refund_count(
        now_weekday, now_hour, temp_refund_delivery, temp_refund_count, dining_count
    )

    total_re_purchase_cost = refund_function.calculate_refund(
        temp_refund_option,
        temp_refund_count,
        dining_count,
        option_cost,
        salad_cost,
        delivery_cost,
        product_cost,
    )[4]
    refund_cost = refund_function.calculate_refund(
        temp_refund_option,
        temp_refund_count,
        dining_count,
        option_cost,
        salad_cost,
        delivery_cost,
        product_cost,
    )[5]

    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": "환불 규정에 따른 재결재액과 환불액은\n다음과 같습니다."
                + "\n\n"
                + f"재결재 총액 : <b>[{total_re_purchase_cost} 원]</b>"
                + f"\n환불액 : <b>[{refund_cost} 원]</b>",
            }
        ]
    }

    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )



def refund_response5(chat_id, content, post_type):
    """
    refund_calculator Reseponse by step

    Args:
        chat_id (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """

    headers = refund_function.api_header()
    temp_refund_menu = content.get("refers").get("user")["profile"]["temp_refund_menu"]
    temp_refund_count = content.get("refers").get("user")["profile"][
        "temp_refund_count"
    ]
    temp_refund_option = content.get("refers").get("user")["profile"][
        "temp_refund_option"
    ]
    temp_refund_delivery = content.get("refers").get("user")["profile"][
        "temp_refund_delivery"
    ]
    now_weekday = refund_function.get_refund_variables(temp_refund_menu)[3]
    now_hour = refund_function.get_refund_variables(temp_refund_menu)[4]
    delivery_cost = refund_function.get_refund_variables(temp_refund_menu)[5]
    salad_cost = refund_function.get_refund_variables(temp_refund_menu)[6]
    option_cost = refund_function.get_refund_variables(temp_refund_menu)[7]
    product_cost = refund_function.get_refund_variables(temp_refund_menu)[8]
    dining_count = refund_function.get_refund_variables(temp_refund_menu)[9]

    _, temp_refund_count = refund_function.add_temp_refund_count(
        now_weekday, now_hour, temp_refund_delivery, temp_refund_count, dining_count
    )
    total_salad_cost = refund_function.calculate_refund(
        temp_refund_option,
        temp_refund_count,
        dining_count,
        option_cost,
        salad_cost,
        delivery_cost,
        product_cost,
    )[0]
    total_option_cost = refund_function.calculate_refund(
        temp_refund_option,
        temp_refund_count,
        dining_count,
        option_cost,
        salad_cost,
        delivery_cost,
        product_cost,
    )[1]

    total_delivery_cost = refund_function.calculate_refund(
        temp_refund_option,
        temp_refund_count,
        dining_count,
        option_cost,
        salad_cost,
        delivery_cost,
        product_cost,
    )[3]
    total_re_purchase_cost = refund_function.calculate_refund(
        temp_refund_option,
        temp_refund_count,
        dining_count,
        option_cost,
        salad_cost,
        delivery_cost,
        product_cost,
    )[4]
    refund_cost = refund_function.calculate_refund(
        temp_refund_option,
        temp_refund_count,
        dining_count,
        option_cost,
        salad_cost,
        delivery_cost,
        product_cost,
    )[5]

    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": "<b>[상세내역]</b>"
                + "\n\n"
                + f"상품명 :\n<b>[{temp_refund_menu.split('(')[0]}]</b> "
                + f"\n상품 가격 :\n<b>[{product_cost} 원]</b> "
                + "\n\n"
                + f"총 수령 샐러드 금액 :\n<b>[{total_salad_cost} 원]</b> "
                + f"\n총 수령 추가 옵션 금액 :\n<b>[{total_option_cost} 원]</b>"
                + f"\n총 수령 배송금액 :\n<b>[{total_delivery_cost} 원]</b>"
                + f"\n<b>재결재 총액</b> :\n<b>[{total_re_purchase_cost} 원]</b>"
                + "\n\n"
                + f"<b>최종 환불액</b> :\n<b>[{refund_cost} 원]</b>",
            }
        ]
    }

    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def refund_response6(chat_id, post_type):
    """
    refund_calculator Reseponse by step

    Args:
        chat_id (str): content.get('refers').get('message')['chatId'] >> 20220719 : group name
        post_type (str) : groups : post message to groups
    """

    headers = refund_function.api_header()
    json_data = {
        'blocks': [
            {
                'type': 'text',
                "value": "환불 예정 금액 확인 후"
                        + "\n환불 진행 희망시"
                        + "\n카카오톡 채널 윤식단을 통한"
                        + "\n상담원 연결 부탁드립니다."
                        + '\n\n'
                        + ":pushpin:<b>윤식단 고객센터</b> (평일08시 - 16시)"
                        + "\n<link type=\"http://pf.kakao.com/_Lxexcxkj/chat\">윤식단 고객센터</link>"
                        
            }
            ],
        } 

    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )

    