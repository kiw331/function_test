import requests
import json

# FCM 서버 키 (Firebase 콘솔에서 확인 가능)
server_key = 'YOUR_SERVER_KEY'

# 알림을 보낼 디바이스의 등록 토큰
registration_token = 'YOUR_DEVICE_REGISTRATION_TOKEN'

# 알림 메시지 내용
message_title = 'Test Notification'
message_body = 'This is a test message from FCM'

# FCM 엔드포인트 URL
url = 'https://fcm.googleapis.com/fcm/send'

# 헤더 설정
headers = {
    'Authorization': f'key={server_key}',
    'Content-Type': 'application/json',
}

# 메시지 데이터
payload = {
    'to': registration_token,
    'notification': {
        'title': message_title,
        'body': message_body
    }
}

# FCM에 POST 요청
response = requests.post(url, headers=headers, data=json.dumps(payload))

# 응답 출력
print(f'Status Code: {response.status_code}')
print(f'Response: {response.json()}')
