# 24시간 큐레이션 자동화 서비스

**ChannelTalk API와 Webhook을 활용한 실시간 개인화 큐레이션 자동 응답 시스템**입니다.  
Flask 기반의 백엔드 서버를 AWS Lightsail에 배포하여 24시간 상담 전환과 자동화를 구현하였습니다.  
기존 수동 응답 시스템 대비 개인 상담 전환율이 **2% → 19%**, 약 **850% 향상**되었습니다.

## 개요

- 기간: 2022.07 ~ 2022.10
- 역할: 기획 / API 서버 개발 / 자동화 설계 / 배포 운영
- 기술 스택: Python, Flask, AWS Lightsail, ChannelTalk API, Webhook


## 프로젝트 배경

- 기존 ChannelTalk 서포트봇은 단순 고정형 답변만 제공 → 실시간 맞춤형 큐레이션 제공 불가
- 고객 응답 결과를 매번 사람이 분석하고 응답 → 운영 부담과 응답 지연 발생
- 상담 연결까지의 **전환율이 낮고 실시간성 부족**

## 문제 정의

| 문제 상황 | 설명 |
|-----------|------|
| 개인화 응답 부족 | 설문 결과에 따른 자동 추천 불가능 |
| 운영 부담 증가 | 매 상담마다 수작업으로 큐레이션 제공 |
| 24시간 응답 불가 | 근무 외 시간에는 상담이 끊김 |

## 해결 방안

- Flask 백엔드 서버 구축 → ChannelTalk Webhook 실시간 수신
- 고객 설문 데이터 기반 응답 자동 생성
- REST API로 ChannelTalk에 응답 전송 → 실시간 큐레이션 제공
- AWS Lightsail에 서버 배포 → 24시간 무중단 운영

## 시스템 구조

![image](https://github.com/user-attachments/assets/96ffcaa1-f842-438d-ada1-ff63dda1c44a)

- **ChannelTalk Webhook**: 고객 입력 수신
- **Flask 서버**: 설문 응답 기반 큐레이션 자동 생성
- **ChannelTalk API**: 응답 전송
- **AWS Lightsail**: 서버 배포 및 운영


## 성과 및 지표

| 항목 | 개선 전 | 개선 후 |
|------|---------|----------|
| 개인 상담 전환율 | 2% | **19%** |
| 상담 연결까지 평균 시간 | 수분 소요 | **즉시 응답** |
| 운영 필요 인력 | 실시간 대응 필요 | **자동화 운영** |

![image](https://github.com/user-attachments/assets/7240181f-dccb-44a4-8f1e-e4352f57f5e9)

## 구현 상세

### 사용방법
1. ChannelTalk에서 Webhook 등록
2. .env 또는 API_key.json 설정
3. app.py 실행 후 Webhook 경로 /in_userchat에 연결
4. 설문 응답이 오면 자동 응답 전송됨

### Webhook 흐름

- `POST /in_userchat` 엔드포인트에서 Webhook 요청 수신
- 설문 응답값 파싱 → 응답 유형 분류 → 템플릿 응답 생성
- ChannelTalk API를 통해 자동 응답 전송

### 운영 환경
- AWS Lightsail에서 Flask 앱 실행
- nohup 로그 기록 및 에러 대응
- RESTful 구조로 유지보수 및 기능 추가 용이
- 하루 24시간 운영 가능하도록 설정

# 참고 자료
- [Channel Talk API Docs](https://developers.channel.io/)
