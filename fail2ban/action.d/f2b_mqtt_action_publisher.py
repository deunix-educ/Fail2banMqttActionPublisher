#!/usr/bin/python3
'''
Created on 20 mai 2020

@author: denis@miraceti.net
'''
import sys, json, uuid, datetime
import paho.mqtt.publish as publish

#HOST = 'broker.emqx.io'
#PORT = 1883
#AUTH = dict(username='emqx', password='public')

HOST = "127.0.0.1"
PORT = 1883
AUTH = dict(username='fail2ban', password='banishing')

LOG_FILE = '/var/log/fail2ban.log'

nodeid = uuid.getnode()
node_type = 'fail2ban'
base_topic = '%s/%s' % (node_type, nodeid, )
mqtt_publish_params = dict(
    qos=0,
    retain=False,
    hostname=HOST,
    port=PORT,
    keepalive=60,
    auth=AUTH,
    client_id='%s_%s'% (node_type, nodeid),
)


def print_message(message):
    try:
        with open(LOG_FILE, 'a') as f:
            f.write('{} [MQTT PUBLISHER] {}'.format(datetime.datetime.now(), message))
    except Exception as e:
        print("fai2ban mqtt error", e)


def publish_message(topic, **payload):
    try:
        message = json.dumps(payload)
        publish.single(base_topic + topic, message, **mqtt_publish_params)
    except Exception as e:
        print_message("publish_message error {}".format(e))


def main():
    try:
        payload = json.loads(sys.argv[1])
        publish_message('/jail', node=nodeid, **payload)
    except Exception as e:
        print_message("main error %s".format(e))

if __name__ == '__main__':
    main()

