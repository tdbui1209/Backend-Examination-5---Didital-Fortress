import ssl
import json
import paho.mqtt.client as mqtt
from app import db
from app.models import Light
import yaml


# MQTT broker information
with open('mqtt_config.yaml', 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    host = cfg['mqtt']['host']
    port = cfg['mqtt']['port']
    root_ca = cfg['mqtt']['root_ca']
    certificate = cfg['mqtt']['certificate']
    private_key = cfg['mqtt']['private_key']
    topic = cfg['mqtt']['topic']

# MQTT message callback
def on_message(client, userdata, message):
    payload = json.loads(message.payload.decode('utf-8'))
    # Extract information from payload and save to database
    light_id = payload.get('light_id')
    brightness = payload.get('brightness')
    status = payload.get('status')
    # Update database
    light = Light.query.get(light_id)
    if light:
        light.brightness = brightness
        light.status = status
        db.session.commit()

# Create MQTT client
client = mqtt.Client()
client.on_message = on_message

# Set TLS configuration
client.tls_set(
    ca_certs=root_ca,
    certfile=certificate,
    keyfile=private_key,
    cert_reqs=ssl.CERT_REQUIRED,
    tls_version=ssl.PROTOCOL_TLS,
    ciphers=None,
)

# Connect to MQTT broker
client.connect(host, port)

# Subscribe to topic
client.subscribe(topic)

# Start the MQTT loop
client.loop_forever()
