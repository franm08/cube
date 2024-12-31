from machine import ADC, Pin
import time
import julia  # Import julia.py for Julia set logic
import mandelbrot  # Import mandelbrot.py for Mandelbrot set logic

# Sound Sensor Setup
sound_sensor = ADC(Pin(26))  # Replace with the correct ADC pin for your sound sensor

# Function to read and normalize sound sensor input
def read_sound():
    raw_value = sound_sensor.read_u16()  # Range: 0 to 65535
    normalized_value = raw_value / 65535  # Normalize to [0, 1]
    return normalized_value

def main():
    # Default settings
    fractal_type = "julia"  # Start with Julia set ("julia" or "mandelbrot")
    max_iterations = 50  # Maximum iterations for both fractals

    while True:
        # Read sound sensor input
        sound_input = read_sound()

        if fractal_type == "julia":
            # Map sound to Julia set parameters
            realC = -0.8 + sound_input * 0.3  # Adjust real part
            imagC = 0.156 + sound_input * 0.2  # Adjust imaginary part

            # Generate and display Julia set
            julia.julia_main(realC, imagC, max_iterations)

        elif fractal_type == "mandelbrot":
            # Map sound to Mandelbrot set parameters
            centerX = -0.5 + sound_input * 0.2  # Adjust center X
            centerY = 0 + sound_input * 0.2  # Adjust center Y
            zoom = 1 + sound_input * 10  # Adjust zoom

            # Generate and display Mandelbrot set
            mandelbrot.mandelbrot_main(centerX, centerY, zoom, max_iterations)

        # Optionally, toggle between fractal types based on time or input
        if int(time.time()) % 30 == 0:  # Toggle every 30 seconds
            fractal_type = "mandelbrot" if fractal_type == "julia" else "julia"

        # Small delay for responsiveness
        time.sleep(0.1)

if __name__ == "__main__":
    main()