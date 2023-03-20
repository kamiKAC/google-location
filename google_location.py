import random
import time

from paho.mqtt import client as mqtt_client
from locationsharinglib import Service

#Location Sharing Library config
cookies_file = 'COOKIE_FILE_PATH.txt'
google_email = 'GOOGLE_USER@gmail.com'

#MQTT Configuration
broker = '192.168.1.114'
port = 1883
topic = "googlelocation/"
client_id = 'python-mqtt-{random.randint(0, 1000)}'
username = ''
password = ''

#Update Interval (in seconds)
update_interval = 60

service = Service(cookies_file=cookies_file, authenticating_account=google_email)

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    while True:
        time.sleep(update_interval)
        for person in service.get_all_people():
            for data in dir(person):
                if not data.startswith('_'):
                    print(topic + person.nickname + "/" + data, str(getattr(person, data)))
                    client.publish(topic + person.nickname + "/" + data, str(getattr(person, data)))


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
