def activation_calculation(user_activation,기초대사량):
    if user_activation == '거의 없다 (주1회이하)' : return 기초대사량 * 1.2
    elif user_activation == '보통 (주2회이상)' : return 기초대사량 * 1.375
    elif user_activation == '꽤있다 (주4회)' : return 기초대사량 * 1.55
    else : return 기초대사량 * 1.725