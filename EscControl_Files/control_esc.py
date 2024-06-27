from adafruit_servokit import ServoKit
from time import sleep

# Initialize the ServoKit instance for a 16-channel PWM driver
my_kit = ServoKit(channels=16, frequency=50)

# Define throttle positions
min_throttle = -1.0  # Full reverse (ESC dependent)
neutral_throttle = 0.0  # Neutral (stop)
max_throttle = 1.0  # Full forward

# Set the number of repeats for the forward-backward loop
num_repeats = 5

# Function to set throttle (0 for stop, 1 for full forward, -1 for full reverse)
def set_throttle(throttle):
    my_kit.continuous_servo[0].throttle = throttle

# Loop to move forward and backward
for _ in range(num_repeats):
    # Move forward
    set_throttle(max_throttle) 
    sleep(1)  # Adjust the sleep time as needed for your application

    # Move backward (if applicable)
    set_throttle(min_throttle)
    sleep(1)  # Adjust the sleep time as needed for your application


# Set to neutral at the end to stop the motor
set_throttle(neutral_throttle)
