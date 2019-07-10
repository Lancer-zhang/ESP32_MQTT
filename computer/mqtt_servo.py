import paho.mqtt.client as mqtt
import time

HOST_IP = 'broker.hivemq.com' # Server的IP地址
HOST_PORT = 1883    # mosquitto 默认打开端口
CLIENT_ID = 'test621'
TOPIC_ID = 'mrjiale' # TOPIC的ID

# 创建一个客户端
client = mqtt.Client(client_id=CLIENT_ID)
# 连接到服务器（本机）
client.connect(HOST_IP, HOST_PORT, 60)

startmsg = 'start'
stopmsg = 'stop'
while True:
    client.publish(TOPIC_ID, startmsg)
    time.sleep(10)
