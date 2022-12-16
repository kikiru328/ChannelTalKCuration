"""
No use for main response
"""
import requests
import main_functions_for_no_use

headers = main_functions_for_no_use.api_header()


def get_variables(content: dict) -> tuple:
    """
    get_variables for functions
    ***
    `user_hydrate not contains in main response`
    `user_dining not contains in main response`
    ***
    Args:
        content (dict): post dictionary

    Returns:
        list: functions variables
    """
    user_name = content.get("refers").get("user")["profile"]["name"]
    user_weight = content.get("refers").get("user")["profile"]["weight"]
    user_height = content.get("refers").get("user")["profile"]["height"]
    user_age = content.get("refers").get("user")["profile"]["age"]
    user_activation = content.get("refers")["user"]["profile"]["activation"]
    user_goal = content.get("refers").get("user")["profile"]["goal"]
    user_hydrate = content.get("refers")["user"]["profile"]["hydrate"]
    user_dining = content.get("refers")["user"]["profile"]["number_dining"]
    bmr = main_functions_for_no_use.get_bmr(user_weight, user_height, user_age)
    maintenance = main_functions_for_no_use.get_cal_by_activation(user_activation, bmr)
    goal_calories = main_functions_for_no_use.get_cal_for_goal(user_goal, maintenance)
    carbohydrate, protein, fat = main_functions_for_no_use.get_macro_cal(goal_calories)
    return (
        user_name,
        user_weight,
        user_height,
        user_age,
        user_activation,
        user_goal,
        user_hydrate,
        user_dining,
        bmr,
        maintenance,
        goal_calories,
        carbohydrate,
        protein,
        fat,
    )


def get_act_response(chat_id: str, content: dict, post_type: str) -> requests:
    """
    no use for response

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
        content : dict, content of post
    """
    user_activation: str = get_variables(content)[4]

    def get_activation_response(user_activation: str) -> str:
        if user_activation == "거의 없다 (주1회이하)":
            return "거의 없으세요.\n\n일주일에 한 번 운동 습관을" + "\n만들어 보는 것은 어떠실까요?"
        if user_activation == "보통 (주2회이상)":
            return "적당합니다.아주 좋습니다!"
        if user_activation == "꽤있다 (주4회)":
            return "꽤 있으시네요. 아주 좋습니다!"
        return "많으시군요. 아주 좋습니다!"

    reponse = get_activation_response(user_activation)
    json_data = {"blocks": [{"type": "text", "value": reponse}]}
    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def goal_response(chat_id: str, content: dict, post_type: str) -> requests:
    """
    no use for response

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
        content : dict, content of post
    """
    user_goal: str = get_variables(content)[5]

    def get_goal_response(user_goal: str) -> str:
        if user_goal == "5Kg 이상의 감량을 원하세요?":
            return (
                "<b>[5Kg 이상 감량]</b>을 원하신다고\n답변을 하셨어요!"
                + "\n\n<b>[5Kg 이상 감량]</b>을 위해서는"
                + "\n<b>하루 4번</b>의 식사를 권장 드리고 있어요!"
            )
        if user_goal == "5Kg 미만의 감량을 원하세요?":
            return (
                "<b>[5kg 미만 감량]</b>을 원한다고"
                + "\n답변을 하셨어요!\n\n<b>[5kg 미만 감량]</b>을 위해서는"
                + "\n<b>하루 4번</b>의 식사를 권장 드리고 있어요!"
            )
        if user_goal == "5Kg 이상의 증량을 원하세요?":
            return (
                "<b>[5Kg 이상 증량]</b>을 원한다고"
                + "\n답변을 하셨어요!\n\n<b>[5Kg 이상 증량]</b>을 위해서는"
                + "\n<b>하루 4번</b>의 식사를 권장 드리고 있어요!"
            )
        return (
            "<b>[유지]</b>를 원한다고"
            + "\n답변을 하셨어요!\n\n<b>[유지]</b>를 위해서는"
            + "\n<b>하루 4번</b>의 식사를 권장 드리고 있어요!"
        )

    response = get_goal_response(user_goal)

    json_data = {"blocks": [{"type": "text", "value": response}]}
    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def hydrate_response(chat_id: str, content: dict, post_type: str) -> requests:
    """
    no use for response

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
        content : dict, content of post
    """
    user_name: str = get_variables(content)[0]
    user_weight: str = get_variables(content)[1]
    user_hydrate: str = get_variables(content)[6]
    hydration = round(user_weight * 0.03, 1)

    def get_hydrate_response(user_hydrate: str) -> str:
        if user_hydrate == "500ml 이하":
            return (
                f":droplet:\n<b>[수분{hydration}L]</b>가"
                + f" <b>[{user_name}]</b>님의\n하루 수분 섭취량이에요."
                + "\n\n현재 심각한 수분 부족 상태로,\n충분한 수분 보충을 권장 드립니다!"
                + "\n\n처음부터 너무 많은 양의 물을 섭취하는 것이 부담스러우시다면"
                + '\n<b>하루 "1L"</b>섭취로 점진적으로\n시작해 보세요!\n\n'
            )
        if user_hydrate == "1L 이하":
            return (
                f":droplet:\n<b>[수분{hydration}L]</b>가"
                + f" <b>[{user_name}]</b>님의\n하루 수분 섭취량이에요."
                + "\n\n현재 심각한 수분 부족 상태로,\n충분한 수분 보충을 권장 드립니다!"
                + "\n\n처음부터 너무 많은 양의 물을 섭취하는 것이 부담스러우시다면"
                + '\n<b>하루 "1.5L"</b>섭취로 점진적으로\n시작해 보세요!\n\n'
            )
        if user_hydrate == "1.5L 이하":
            return (
                f":droplet:\n<b>[수분{hydration}L]</b>가"
                + f" <b>[{user_name}]</b>님의\n하루 수분 섭취량이에요."
                + "\n\n조금만 더 수분 보충에 신경 써주신다면\n더욱 좋은 몸의 상태를"
                + "\n유지할 수 있을 거예요!\n\n"
            )
        return (
            f":droplet:\n<b>[수분{hydration}L]</b>가"
            + f" <b>[{user_name}]</b>님의\n하루 수분 섭취량이에요."
            + "\n\n현재 수분 보충을\n열심히 하시는 것 같아요!"
            + "\n나에게 맞는 섭취량을 정확히 알아가며"
            + "\n더욱 좋은 몸의 컨디션을 만들어보세요!\n\n"
        )

    response: str = get_hydrate_response(user_hydrate)

    json_data = {"blocks": [{"type": "text", "value": response}]}

    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def dining_response(chat_id: str, content: dict, post_type: str) -> requests:
    """
    no use for response

    Args:
        chat_id : str, customer name
        post_type : str, post message to post
        content : dict, content of post
    """
    user_dining: str = get_variables(content)[7]

    def get_dining_response(user_dining: str) -> str:
        if user_dining == "1회":
            return (
                "<b>에너지 섭취 관리가 필요해요!</b>\n식사는 <b>3~5시간에 한 번씩</b>"
                + "\n섭취를 해주는 것이 가장 좋아요!"
                + "\n\n:alarm_clock: 07시 / 12시 / 16시 / 19시\n   이런 방식으로요!"
                + "\n\n1시간 동안 에너지로\n흡수할 수 있는 양은 정해져있어요"
                + "\n\n한 번에 많은 양을 섭취하면\n흡수되지 못한 양의 에너지가\n지방으로 전환돼요"
                + "\n\n또 한 대사율이 떨어져\n<b>살이 찌는 체질</b>로 변하게 돼요."
            )
        if user_dining == "2회":
            return (
                "<b>에너지 섭취 관리가 필요해요!</b>\n식사는 <b>3~5시간에 한 번씩</b>"
                + "\n섭취를 해주는 것이 가장 좋아요!"
                + "\n\n:alarm_clock: 07시 / 12시 / 16시 / 19시\n   이런 방식으로요!"
                + "\n\n1시간 동안 에너지로\n흡수할 수 있는 양은 정해져있어요"
                + "\n\n한 번에 많은 양을 섭취하면\n흡수되지 못한 양의 에너지가\n지방으로 전환돼요"
                + "\n\n또 한 대사율이 떨어져\n<b>살이 찌는 체질</b>로 변하게 돼요."
            )
        if user_dining == "3회":
            return (
                "<b>에너지 섭취 관리를\n 너무 잘하고 있습니다!</b>"
                + "\n식사는 <b>3~5시간에 한 번씩</b>\n섭취를 해주는 것이 가장 좋아요!"
                + "\n\n:alarm_clock: 07시 / 12시 / 16시 / 19시\n   이런 방식으로요!"
                + "\n\n1시간 동안 에너지로\n흡수할 수 있는 양은 정해져있어요"
                + "\n\n한 번에 많은 양을 섭취하면\n흡수되지 못한 양의 에너지가\n지방으로 전환돼요"
                + "\n\n또 한 대사율이 떨어져\n<b>살이 찌는 체질</b>로 변하게 돼요."
            )
        if user_dining == "4회":
            return (
                "<b>에너지 섭취 관리를\n 너무 잘하고 있습니다!</b>"
                + "\n식사는 <b>3~5시간에 한 번씩</b>\n섭취를 해주는 것이 가장 좋아요!"
                + "\n\n:alarm_clock: 07시 / 12시 / 16시 / 19시\n   이런 방식으로요!"
                + "\n\n1시간 동안 에너지로\n흡수할 수 있는 양은 정해져있어요"
                + "\n\n한 번에 많은 양을 섭취하면"
                + "\n흡수되지 못한 양의 에너지가\n지방으로 전환돼요"
                + "\n\n또 한 대사율이 떨어져\n<b>살이 찌는 체질</b>로 변하게 돼요."
            )
        return (
            "<b>에너지 섭취 관리를\n 너무 잘하고 있습니다!</b>"
            + "\n식사는 <b>3~5시간에 한 번씩</b>\n섭취를 해주는 것이 가장 좋아요!"
            + "\n\n:alarm_clock: 07시 / 12시 / 16시 / 19시\n이런 방식으로요!"
            + "\n\n1시간 동안 에너지로\n흡수할 수 있는 양은 정해져있어요"
            + "\n\n한 번에 많은 양을 섭취하면\n흡수되지 못한 양의 에너지가\n지방으로 전환돼요"
            + "\n\n또 한 대사율이 떨어져\n<b>살이 찌는 체질</b>로 변하게 돼요."
            + "\n\n<b>5회 이상의 식사</b>는 좋은 방법이지만"
            + "\n과식의 우려가 있어 하루 권장 섭취량을\n잘 분배해 섭취해 주세요!"
        )

    response: str = get_dining_response(user_dining)

    json_data = {"blocks": [{"type": "text", "value": response}]}

    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )


def recommend_product(chat_id: str, content: dict, post_type: str) -> requests:
    """
    Recommend products
    Args:
        chat_id : str, customer name
        post_type : str, post message to post
        content : dict, content of post
        11 12
    """
    carbohydrate: int = get_variables(content)[11]
    protein: int = get_variables(content)[12]

    def get_url(carbohydrate: int, protein: int) -> str:
        if (int(carbohydrate / 4) in range(0, 56)) and (
            int(protein / 4) in range(0, 36)
        ):
            return "https://yundiet.com/curation_program/?idx=23"
        if (int(carbohydrate / 4) in range(0, 56)) and (
            int(protein / 4) in range(36, 40)
        ):
            return "https://yundiet.com/curation_program/?idx=30"
        if (int(carbohydrate / 4) in range(0, 56)) and (
            int(protein / 4) in range(40, 101)
        ):
            return "https://yundiet.com/curation_program/?idx=33"

        if (int(carbohydrate / 4) in range(56, 69)) and (
            int(protein / 4) in range(0, 36)
        ):
            return "https://yundiet.com/curation_program/?idx=38"
        if (int(carbohydrate / 4) in range(56, 69)) and (
            int(protein / 4) in range(36, 40)
        ):
            return "https://yundiet.com/curation_program/?idx=39"
        if (int(carbohydrate / 4) in range(56, 69)) and (
            int(protein / 4) in range(40, 101)
        ):
            return "https://yundiet.com/curation_program/?idx=40"

        if (int(carbohydrate / 4) in range(69, 81)) and (
            int(protein / 4) in range(0, 36)
        ):
            return "https://yundiet.com/curation_program/?idx=41"
        if (int(carbohydrate / 4) in range(69, 81)) and (
            int(protein / 4) in range(36, 40)
        ):
            return "https://yundiet.com/curation_program/?idx=42"
        if (int(carbohydrate / 4) in range(69, 81)) and (
            int(protein / 4) in range(40, 101)
        ):
            return "https://yundiet.com/curation_program/?idx=45"
        return "https://yundiet.com/curation_program/?idx=45"

    url = get_url(carbohydrate, protein)

    json_data = {
        "blocks": [
            {
                "type": "text",
                "value": ":herb: 식단관리를 간편하게"
                + "\n   도와줄 <b>윤식단 맞춤 정기구독</b>을\n   추천해 드려요!",
            }
        ],
        "buttons": [
            {"title": "윤식단 샐러드 정기배송 프로그램", "colorVariant": "green", "url": url}
        ],
    }

    return requests.post(
        f"https://api.channel.io/open/v5/{post_type}/{chat_id}/messages",
        headers=headers,
        json=json_data,
        timeout=10,
    )
