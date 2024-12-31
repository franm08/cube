from machine import Pin
from neopixel import NeoPixel
import math
import time

# LED Cube Setup
led_pin = Pin(0, Pin.OUT)  # Replace with the correct pin for your LED cube
led_cube = NeoPixel(led_pin, 512)  # 8x8x8 cube = 512 LEDs

# Function to approximate sin(x) using Taylor series
def taylor_sine(x, terms=10):
    result = 0
    for n in range(terms):
        coefficient = (-1)**n  # Alternating sign
        result += coefficient * (x**(2*n + 1)) / math.factorial(2*n + 1)
    return result

# Function to map Taylor series results to brightness
def map_brightness(x, terms=10):
    # Get sine value using Taylor series
    sine_value = taylor_sine(x, terms)
    # Normalize sine value from [-1, 1] to [0, 255]
    return int((sine_value + 1) / 2 * 255)

# Function to apply brightness to the entire LED cube
def update_led_cube(brightness):
    for i in range(512):  # Update all 512 LEDs
        led_cube[i] = (brightness, brightness, brightness)  # Grayscale brightness
    led_cube.write()

# Main loop for brightness modulation
def main():
    x = 0  # Starting angle
    increment = 0.1  # Angle increment for smooth animation
    while True:
        brightness = map_brightness(x, terms=10)  # Calculate brightness
        update_led_cube(brightness)  # Update the LED cube
        x += increment  # Increment angle
        time.sleep(0.05)  # Small delay for smooth animation

if __name__ == "__main__":
    main()