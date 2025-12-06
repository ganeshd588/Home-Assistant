import time
import paho.mqtt.client as mqtt

student_name = "Ganesh D"
unique_id = "42732014"
topic = "home/ganeshd-2025/sensor"

broker = "192.168.0.11"    
port = 1883
username = "ganesh"           
password = "ganesh@123" 

client = mqtt.Client()
client.username_pw_set(username, password)
client.connect(broker, port, 60)

print("Connected to MQTT broker. Publishing sensor data...")

while True:
    temperature = 25
    humidity = 60
    vibration = 1

    payload = f"{student_name},{unique_id},{temperature},{humidity},{vibration}"
    client.publish(topic, payload)
    print("Published:", payload)
    time.sleep(5)
