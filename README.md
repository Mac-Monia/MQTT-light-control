# MQTT Light Control System

A simple web-based light control system that demonstrates MQTT communication between a web interface and a Python-based light simulation.

## Features

- Real-time light control through MQTT protocol
- Web-based user interface with visual feedback
- Python-based light simulation
- Responsive design using Tailwind CSS
- Visual light status indicator

## Prerequisites

- Python 3.x
- MQTT broker (using test.mosquitto.org for demonstration)
- Web browser with JavaScript enabled

## Dependencies

### Python Dependencies
```
paho-mqtt
```

### Web Dependencies
- MQTT.js (loaded via CDN)
- Tailwind CSS (loaded via CDN)

## Project Structure

```
light_control/
├── index.html          # Web interface
└── light_simulation.py # Python MQTT subscriber
```

## Setup and Running

1. Install the required Python package:
   ```bash
   pip install paho-mqtt
   ```

2. Start the light simulation:
   ```bash
   python light_simulation.py
   ```

3. Open `index.html` in a web browser

## How It Works

1. The web interface (`index.html`) connects to the MQTT broker and provides controls to turn the light ON/OFF
2. When a button is clicked, it publishes an MQTT message to the topic `/student_group/light_control`
3. The Python script (`light_simulation.py`) subscribes to the same topic and simulates the light state
4. The web interface updates its visual representation based on the current light state

## MQTT Configuration

- Broker: test.mosquitto.org
- Port: 1883 (Python client) / 8081 (WebSocket)
- Topic: /student_group/light_control
- Commands: "ON" / "OFF"

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License. 