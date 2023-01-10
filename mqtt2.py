import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)

def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))

def on_subscribe(client, userdata, mid, granted_qos):
    print("sybscrubed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    print("topic: "+msg.topic+"   msg: " +str(msg.payload.decode("UTF-8")))

# 새로운 클라이언트 생성
client = mqtt.Client()
# 콜백 함수 설정 
client.on_connect = on_connect # 브로커에 접속
client.on_disconnect = on_disconnect # 브로커에 접속 종료
client.on_subscribe = on_subscribe # topic 구독
client.on_message = on_message # 발행된 메세지가 들어왔을 때
# address 설정
client.connect('broker.hivemq.com', 1883)
# common topic 으로 메세지 발행
client.subscribe('bssmtopic/#', 0)
client.loop_forever()