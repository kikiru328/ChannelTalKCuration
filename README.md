# ChannelTalk 1:1 Curation Service

ChannelTalk(이하 채널톡)의 Webhook과 API를 사용하여 1:1 자동 응답 서비스를 구축.  
채널톡의 서포트봇은 지정해둔 답변이 발송되기 때문에 개인에 맞는 답변이 어렵다.  
따라 Flask를 활용하여 답변을 주는 서비스를 구현하였고  
24시간 작동을 위하여 AWS LIGHTSAIL background에 실행하였다.  
혹시 모를 에러나 문제에 대비하여 nohup에 logging을 출력하여 해결하였다.

> 기본 Test는 Ngrok을 활용하였다.
