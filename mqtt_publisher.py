import paho.mqtt.client as mqtt
import random
import time
import json

DEVICE_ID = "Sensor_1"  # Unique device ID

# MQTT Configurations
BROKER_ADDRESS = "192.168.2.10"  # MQTT broker address
PORT = 1883  # MQTT port
SENSOR_TOPIC = f"sensor/{DEVICE_ID}"  # Topic for sensor data

def main():
    # Initialize MQTT client
    client = mqtt.Client()

    try:
        # Connect to the MQTT broker
        client.connect(BROKER_ADDRESS, PORT, keepalive=60)
        print(f"Connected to MQTT broker at {BROKER_ADDRESS}:{PORT}")

        # Publish data in a loop
        while True:
            # Generate random measurements
            temperature = round(random.uniform(20.0, 30.0), 2)  # Temperature in °C
            humidity = round(random.uniform(30.0, 60.0), 2)     # Humidity in %

            # Create a combined message for temperature and humidity
            sensor_message = json.dumps({
                "temperature": {
                    "value": temperature,
                    "unit": "°C"
                },
                "humidity": {
                    "value": humidity,
                    "unit": "%"
                }
            })

            # Publish the message to the single topic
            client.publish(SENSOR_TOPIC, sensor_message)
            print(f"Published to {SENSOR_TOPIC}: {sensor_message}")

            time.sleep(1)  # Delay between measurements

    except KeyboardInterrupt:
        print("Disconnecting...")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.disconnect()
        print("Disconnected from MQTT broker")

if __name__ == "__main__":
    main()


















