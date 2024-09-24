# Fail2banMqttActionublisher
Fail2ban action: publish all server banished

### Actions in action.d

### Configuration mqtt broker or local mosquitto
action.d/f2b_mqtt_action_publisher.py




### Usage
Add action as jail-example.local

        systemctl restart fail2ban.service
        
### Control
    
        tail -f /var/log/mosquitto/mosqitto.log
