import serial

ser = serial.Serial('COM4',9600)

try:
    while True:
        data = ser.readline().decode().strip()
        print("Data received: ",data)
except KeyboardInterrupt:
    print(" Keyboard interrupt detected. Stopping script")
finally:
    ser.close()
