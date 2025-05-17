import serial

#--Replace 'COMX' with your Arduino's serial port
ser = serial.Serial('COM4', 9600)

try:
    while True:
        pot_value = ser.readline().decode().strip()
        print("potentiometer Value:", pot_value)

except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed.")