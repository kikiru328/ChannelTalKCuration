# ChannelTalk 1:1 Curation Service

채널톡의 서포트봇은 지정해둔 답변이 발송되기 때문에 개인에 맞는 답변이 어렵다.  
따라서 ChannelTalk(이하 채널톡)의 Webhook과 API를 사용하여 1:1 자동 응답 서비스를 개발하였다.

모든 답변의 내용은 채널톡 내 고객 설문조사를 기반으로 계산되어 제공된다.  
즉, 설문조사가 선행되어야 하며, channeltalk 내 database에서 어느 분야로 저장할지 지정할 수 있다.

저장된 database를 근거로 Flask를 활용하여 답변을 주는 서비스를 구현하였고  
24시간 작동을 위하여 AWS LIGHTSAIL background에 실행하였다.  
혹시 모를 에러나 문제에 대비하여 nohup에 logging을 출력하여 해결하였다.

<br/>
Channel Talk's support bot sends designated answers, so it is difficult to answer them individually.
Therefore, a 1:1 automatic response service was developed using ChannelTalk's Webhook and API.

The contents of all answers are calculated and provided based on customer surveys in Channel Talk.
In other words, a survey must be preceded, and it is possible to specify which field to store in the database in channeltalk.

Based on the stored database, we implemented a service that provides answers using Flask.
It was executed in AWS LIGHTSAIL background for 24-hour operation.
In preparation for any possible error or problem, logging was output to nohup to solve it.

</br>

### Modularization

해당 git 내용은 Curation 서비스를 `모듈화`하였다.  
따라서 git clone 이후 사용이 가능하다.
<br/>

This git content 'modularized' the Curation service.
Therefore, it can be used after git clone.

# Prepare

필요한 것은 두가지다.  
There are two things that are needed.

1. ChannelTalk API Key
2. ChannelTalk Webhook address
<details>
<summary><font size='2'>Webhook address</font></summary>
<div markdown='1'>
webhook 주소는 서버 URL + app.py 내 route 주소.
webhook 주소를 channeltalk webhook 주소에 입력한다.

```python
# server address = https://0.00.00.00

@app.route("/in_userchat", methods=["GET", "POST"])
# route address = "/in_userchat"

# webhook address = https://0.00.00.00/in_userchat
```

![webhook address](https://user-images.githubusercontent.com/60537388/210834393-0f9957e2-8bcd-402d-be0d-0dd28e79719d.png)

<details>
<summary><font size='2'>open_userchat_option</font></summary>
<div markdown='1'>

![image](https://user-images.githubusercontent.com/60537388/210835098-5f0ab058-db0e-4fd7-bfe9-31aa1351c165.png)

</div>
</details>

<details>
<summary><font size='2'>in_userchat_option</font></summary>
<div markdown='1'>

![image](https://user-images.githubusercontent.com/60537388/210834944-fa040cb8-3a90-4af8-a3b1-95e1cdee3bef.png)

</div>
</details>

</div>
</details>

<details>
<summary><font size='2'>Webhook?</font></summary>
<div markdown='1'>

![](https://user-images.githubusercontent.com/60537388/210836216-788a45c7-3105-47de-abdb-2c20b6c3f478.png)

</div>
</details>
<br/>

# Use

Flask operator > `app.py`  
MainCuration.main_curation.main_curation > operator main_curation  
same as InteractionCuration

<br/>

# Set Message

set message in #\_response.py

<br/>

```
📦distribution_git
 ┣ 📂InteractionCuration
 ┃ ┣ 📜interaction_curation.py
 ┃ ┣ 📜interaction_functions.py
 ┃ ┗ 📜interaction_response.py
 ┣ 📂MainCuration
 ┃ ┣ 📜main_curation.py
 ┃ ┣ 📜main_function.py
 ┃ ┗ 📜main_response.py
 ┣ 📂templates
 ┃ ┗ 📜index.html
 ┣ 📜API_key.json
 ┣ 📜app.py
 ┣ 📜nohup.out
 ┗ 📜requirements.txt
```
