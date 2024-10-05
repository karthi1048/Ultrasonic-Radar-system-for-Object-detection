# Ultrasonic-Radar-system-for-Object-detection


The **Ultrasonic Radar System** uses an ultrasonic sensor connected to an Arduino to measure the distance of objects in its path. The sensor's data is processed and visualized using the Processing IDE, while Python is used to automate the storage of acquired values in a text file.

### Features
- **Object Detection**: Detects objects within the sensor's range using an ultrasonic sensor.
- **Real-time Visualization**: Visualizes the detected objects on a radar-like display using Processing.
- **Modular Code**: Separate Arduino, Processing, and Python scripts to handle various parts of the system.

## Repository Structure

- `arduino/`: Contains the Arduino code for operating the ultrasonic sensor and handling communication with other parts of the system.
- `processing/`: Includes the Processing code to visualize the radar data in real-time.
- `python/`: Python code for storing distance values in a .txt file.

## How to Run

1. **Arduino Code**:
   - Upload the Arduino code (`Radar.ino`) to your Arduino board.
   - Connect the ultrasonic sensor as per the wiring instructions provided in the Arduino script.

2. **Processing Visualization**:
   - Run the Processing script (`RADAR__Project.pde`) in the Processing IDE to visualize the data from the sensor in real-time.

3. **Python Code**:
   - (Optional) Run the Python script (`Radar-Project.py`) for storing the distance values in a .txt file.
   - For redundancy case, create your own text file & use that.

## Requirements

- **Hardware**: Arduino board, Ultrasonic sensor (e.g., HC-SR04), Servo motor, Connecting wires.
- **Software**: Arduino IDE, Processing IDE, Python 3.x.

---
