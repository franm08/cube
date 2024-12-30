from machine import ADC, Pin
import time
import julia  # Import your julia.py module

# Sound Sensor Setup
sound_sensor = ADC(Pin(26))  # Replace with the correct ADC pin for your sound sensor

# Function to read and normalize sound sensor input
def read_sound():
    raw_value = sound_sensor.read_u16()  # Range: 0 to 65535
    normalized_value = raw_value / 65535  # Normalize to [0, 1]
    return normalized_value

def main():
    # Julia set constants
    max_iterations = 50  # Maximum iterations for Julia set

    while True:
        # Read sound sensor input
        sound_input = read_sound()

        # Map sound input to Julia set parameters
        realC = -0.8 + sound_input * 0.3  # Real part of c adjusted by sound input
        imagC = 0.156 + sound_input * 0.2  # Imaginary part of c adjusted by sound input

        # Generate and display the Julia set on the 8x8x8 LED cube
        julia.julia_main(realC, imagC, max_iterations)

        # Small delay for responsiveness
        time.sleep(0.1)

if __name__ == "__main__":
    main()