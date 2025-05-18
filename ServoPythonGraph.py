import matplotlib.pyplot as plt
import serial
import time
import keyboard

# Open serial port
ser = serial.Serial('COM4', 9600)  # Update 'COM4' with your Arduino's port
time.sleep(2)  # Wait for serial connection to establish

# Initialize empty lists to store data
x_data = []
y_data_pot = []
y_data_servo = []

# Set up the plot
plt.ion()  # Turn on interactive mode
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
line_pot, = ax1.plot(x_data, y_data_pot, 'b-', label='Potentiometer Reading')
line_servo, = ax2.plot(x_data, y_data_servo, 'r-', label='Servo Position')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Potentiometer Reading', color='b')
ax2.set_ylabel('Servo Position', color='r')

# Main loop
try:
    while True:

        # Read potentiometer value and servo position from Arduino
        data = ser.readline().decode().strip()
        if data:
            values = data.split(',')
            pot_val = int(values[0])
            servo_pos = int(values[1])
            print("Potentiometer Reading:", pot_val, "Servo Position:", servo_pos)

            # Append data to lists
            x_data.append(time.time())  # Use time as x-axis
            y_data_pot.append(pot_val)
            y_data_servo.append(servo_pos)

            # Update plot
            line_pot.set_xdata(x_data)
            line_pot.set_ydata(y_data_pot)
            line_servo.set_xdata(x_data)
            line_servo.set_ydata(y_data_servo)
            ax1.relim()
            ax1.autoscale_view()
            ax2.relim()
            ax2.autoscale_view()
            fig.canvas.draw()
            fig.canvas.flush_events()

            # Check for keyboard input to halt
            if keyboard.is_pressed('q'):
                break

except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed")