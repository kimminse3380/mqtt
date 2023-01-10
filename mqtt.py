import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)

def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))

def on_publish(client, userdata, mid):
    print("In on_pub callback mid=", mid)

# 새로운 클라이언트 생성
client = mqtt.Client()
# 콜백 함수 설정 
client.on_connect = on_connect # 브로커에 접속
client.on_disconnect = on_disconnect # 브로커에 접속 종료
client.on_publish = on_publish # 메세지 발행``
# address 설정
client.connect('bssmtopic/1', 1883)
client.loop_start()
# common topic 으로 메세지 발행
client.publish('common', json.dumps({"sucess":"hi"}), 1)
client.loop_stop()
# 연결 종료
client.disconnect()