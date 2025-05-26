# ♻️ Revenge of the Recycling System

A logic-driven autonomous system designed to identify recyclable bottles and guide a robot to sort them into appropriate bins based on weight and color sensor data.

## 🚀 Project Overview

This project simulates a smart recycling system where a robot autonomously detects, classifies, and sorts recyclable bottles into corresponding bins. Given limited low-level functions for motor control, I developed all the high-level logic, decision-making, and troubleshooting required for robust real-time operation.

## 🧠 Key Features

- **Sensor-Based Detection**: Classifies bottles using color and weight sensors.
- **Automated Arm Movement**: Coordinates robotic arm movement to pick up and drop off bottles.
- **Bin Navigation**: Guides the robot to the correct bin based on object classification.
- **Error Handling**: Designed to address unreliable sensor readings by adding redundancy and fallbacks.

## 🛠️ Technologies Used

- **Language**: Python
- **Platform**: Custom educational robotics simulator
- **Sensors**: Simulated color and weight sensors
- **Actuators**: Pre-defined motor functions for movement and pickup/dropoff

## 🧩 My Role

- Designed and implemented the **entire logic and decision-making layer**, using predefined movement functions.
- Handled **sensor integration**, including interpreting raw values and compensating for inconsistencies in input.
- Implemented a reliable classification system based on conditional logic and thresholds.
- Optimized navigation paths and action sequencing for minimal time and error.

## 📊 Results

- Successfully tested with **50+ sample bottles**, achieving over **90% classification accuracy**.
- Robust handling of corner cases such as:
  - Inconsistent lighting
  - Ambiguous color values
  - Unusual weight distributions

## 🔍 Sample Logic (Pseudocode)

```python
if color == RED and weight < 25:
    category = "Can"
elif color == GREEN and weight >= 25:
    category = "Bottle"
# Navigate to bin and drop
