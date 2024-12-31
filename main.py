from machine import ADC, Pin
import time
from neopixel import NeoPixel
from math import factorial

# LED Cube Setup
led_pin = Pin(0, Pin.OUT)  # Replace with the correct pin for your LED cube
led_cube = NeoPixel(led_pin, 512)  # 8x8x8 cube = 512 LEDs

# Sound Sensor Setup
sound_sensor = ADC(Pin(26))  # Replace with the correct ADC pin for your sound sensor

# Function to approximate sin(x) using Taylor series
def taylor_sine(x, terms=10):
    result = 0
    for n in range(terms):
        coefficient = (-1)**n  # Alternating sign
        result += coefficient * (x**(2*n + 1)) / factorial(2*n + 1)
    return result

# Function to map brightness based on sine and sound input
def calculate_brightness(x, sound_input, terms=10):
    # Get sine value using Taylor series
    sine_value = taylor_sine(x, terms)
    # Combine sine and sound for dynamic brightness
    combined_value = sine_value * sound_input
    # Normalize to [0, 255]
    return int((combined_value + 1) / 2 * 255)

# Function to update LED cube brightness
def update_led_cube(brightness):
    for i in range(512):  # Update all 512 LEDs
        led_cube[i] = (brightness, brightness, brightness)  # Grayscale brightness
    led_cube.write()

# Function to read sound input and normalize to [0, 1]
def read_sound():
    raw_value = sound_sensor.read_u16()  # Range: 0 to 65535
    return raw_value / 65535  # Normalize

# Main loop
def main():
    x = 0  # Starting angle for sine
    increment = 0.1  # Increment for smooth sine wave animation
    while True:
        # Read sound sensor input
        sound_input = read_sound()
        
        # Calculate brightness based on sine wave and sound input
        brightness = calculate_brightness(x, sound_input, terms=10)
        
        # Update the LED cube with the calculated brightness
        update_led_cube(brightness)
        
        # Increment angle for sine wave
        x += increment
        time.sleep(0.05)  # Delay for smooth animation

if __name__ == "__main__":
    main()