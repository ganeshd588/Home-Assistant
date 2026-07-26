# 🏠 Home Assistant + MQTT + Python Integration

A Python-based IoT project that demonstrates real-time sensor data publishing using the MQTT protocol and visualization in Home Assistant.

---

## 📌 Project Overview

This project implements a simple IoT communication system where a Python application publishes sensor data to an MQTT broker. Home Assistant subscribes to the MQTT topic and displays the sensor values on a real-time dashboard.

The project demonstrates how MQTT enables lightweight communication between IoT devices and automation platforms.

---

## ✨ Features

- Real-time MQTT communication
- Python MQTT Publisher
- Home Assistant Dashboard Integration
- Live Sensor Monitoring
- Lightweight IoT Architecture
- Easy to Extend with Additional Sensors

---

## 📊 Sensor Data Published

The Python application publishes the following values:

- 🌡 Temperature
- 💧 Humidity
- 📳 Vibration Status

These values are received by Home Assistant and displayed on the dashboard in real time.

---

## 🛠 Technologies Used

- Python 3
- Home Assistant
- Mosquitto MQTT Broker
- paho-mqtt
- YAML Configuration
- MQTT Protocol

---

## 📂 Project Structure

```
Home-Assistant/
│
├── nak.py
├── README.md
```

---

## ⚙️ Workflow

Python Script
        ↓
MQTT Broker (Mosquitto)
        ↓
Home Assistant
        ↓
Dashboard Visualization

---

## 🚀 How to Run

1. Install Home Assistant.
2. Install the Mosquitto MQTT Broker.
3. Install the Python dependency:

```bash
pip install paho-mqtt
```

4. Run the Python publisher:

```bash
python nak.py
```

5. Configure MQTT sensors in Home Assistant.

6. Open the Home Assistant dashboard to view the live sensor values.

---

## 📸 Output

The Home Assistant dashboard displays:

- Temperature
- Humidity
- Vibration Status

The values update automatically whenever the Python publisher sends new MQTT messages.

---

## 📈 Future Improvements

- ESP32 Integration
- Raspberry Pi Deployment
- Additional IoT Sensors
- Cloud MQTT Broker
- Mobile Notifications
- Historical Data Storage

---

## 👨‍💻 Author

**Ganesh D**

---

## 📜 License

This project is intended for educational and learning purposes.
