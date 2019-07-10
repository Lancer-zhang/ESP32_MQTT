from umqtt import MQTTClient
import time
import led

SERVER = 'broker.hivemq.com'
CLIENT_ID = 'test620'
TOPIC = b'mrjiale'


def serve_start():
	led.led2_on()


def serve_stop():
	led.led2_off()


def mqtt_callback(topic, msg):
  global TOPIC
  print('topic: {}'.format(topic))
  print('msg: {}'.format(msg))
  if msg == b"start":
		serve_start()
  if msg == b"stop":
		serve_stop()


def mqtt_connect():
  client = MQTTClient(CLIENT_ID, SERVER, port=1883)
  client.set_callback(mqtt_callback)
  client.connect()
  print("mqtt connect success")
  client.subscribe(TOPIC)
  while True:
    client.check_msg()
    time.sleep(1)
    print("wait ...")






