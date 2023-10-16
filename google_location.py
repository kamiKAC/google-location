import time
import os

from paho.mqtt import client as mqtt_client
from locationsharinglib import Service

#Location Sharing Library config
cookies_file = "/files/" + os.environ.get("COOKIES_FILE",'googlemaps_cookie.txt')
google_email = os.environ.get("GOOGLE_EMAIL",'')

#MQTT Configuration
client_id = os.environ.get("MQTT_CLIENT_NAME", 'google_location_mqtt')
broker = os.environ.get("MQTT_HOST",'localhost')
port = int(os.environ.get("MQTT_PORT",'1883'))
topic = os.environ.get("MQTT_TOPIC",'googlelocation/')
username = os.environ.get("MQTT_USER",'')
password = os.environ.get("MQTT_PASS",'')

#Update Interval (in seconds)
update_interval = int(os.environ.get("INTERVAL",'60'))

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
            latitude = None
            longitude = None
            datetime = None
            for data in dir(person):
                if not data.startswith('_'):
                    if data == 'latitude':
                        latitude = str(getattr(person, data))
                    elif data == 'longitude':
                        longitude = str(getattr(person, data))
                    elif data == 'datetime':
                        datetime = str(getattr(person, data))
                    print(topic + person.nickname + "/" + data, str(getattr(person, data)))
                    client.publish(topic + person.nickname + "/" + data, str(getattr(person, data)))
            if latitude and longitude:
                print(topic + person.nickname + "/" + "coordinates", latitude + "," + longitude)
                client.publish(topic + person.nickname + "/" + "coordinates", latitude + "," + longitude)
            if datetime:
                print(topic + person.nickname + "/" + "datetime_iso8061", datetime[0:10] + 'T' + datetime[11:23] + datetime[26:29] + datetime [30:32])
                client.publish(topic + person.nickname + "/" + "datetime_iso8061", datetime[0:10] + 'T' + datetime[11:23] + datetime[26:29] + datetime [30:32])




def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
