import paho.mqtt.client as mqtt

# MQTT Callback function

def on_message(client, userdata, message):
    command = message.payload.decode("utf-8")
    if command == "ON":
        print("💡 Light is TURNED ON")
    elif command == "OFF":
        print("💡 Light is TURNED OFF")

# MQTT setup
client = mqtt.Client()
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 60)
client.subscribe("/student_group/light_control")

print("Listening for MQTT messages...")
client.loop_forever()
