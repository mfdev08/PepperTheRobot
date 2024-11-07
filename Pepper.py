import RPi.GPIO as GPIO
import time

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)

# Motor 1 pins (connected to GPIO17 and GPIO18)
IN1 = 17
IN2 = 18

# Motor 2 pins (connected to GPIO22 and GPIO23)
IN3 = 22
IN4 = 23

# Set GPIO pins as output
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Function to move forward
def forward():
    print("Moving forward")
    GPIO.output(IN1, GPIO.HIGH)  # Motor 1 forward
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)  # Motor 2 forward
    GPIO.output(IN4, GPIO.LOW)

# Function to move backward
def backward():
    print("Moving backward")
    GPIO.output(IN1, GPIO.LOW)   # Motor 1 backward
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)   # Motor 2 backward
    GPIO.output(IN4, GPIO.HIGH)

# Function to stop the robot
def stop():
    print("Stopping")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

# Main program loop
try:
    while True:
        command = input("Enter command (forward/backward/stop): ").lower()
        if command == 'forward':
            forward()
        elif command == 'backward':
            backward()
        elif command == 'stop':
            stop()
        else:
            print("Invalid command.")
        time.sleep(1)  # Delay for 1 second

except KeyboardInterrupt:
    print("\nProgram stopped by user")
finally:
    GPIO.cleanup()  # Clean up GPIO settings
