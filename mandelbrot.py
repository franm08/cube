from neopixel import NeoPixel
from machine import Pin

# LED Cube Setup
led_pin = Pin(0, Pin.OUT)  # Pin for controlling the LED cube
led_cube = NeoPixel(led_pin, 512)  # 8x8x8 cube = 512 LEDs

# Mandelbrot Set Parameters
grid_size = 8  # 8x8x8 cube dimensions
max_iterations = 50  # Default max iterations

# Function to calculate the magnitude squared of a complex number
def get_magnitude_squared(ReZ, ImZ):
    return ReZ * ReZ + ImZ * ImZ

# Recursive function for Mandelbrot set calculations
def recursive_mandelbrot(ReC, ImC, ReZ, ImZ, depth, max_iterations):
    magnitude = get_magnitude_squared(ReZ, ImZ)

    # Case 1: Diverges
    if magnitude > 4.0:
        return depth

    # Case 2: Converges
    if depth >= max_iterations:
        return max_iterations

    # Recursive step: z_(n+1) = z_n^2 + c
    new_ReZ = (ReZ * ReZ) - (ImZ * ImZ) + ReC
    new_ImZ = 2 * ReZ * ImZ + ImC

    return recursive_mandelbrot(ReC, ImC, new_ReZ, new_ImZ, depth + 1, max_iterations)

# Generate 3D Mandelbrot set for the LED cube
def generate_mandelbrot_8x8x8(centerX, centerY, zoom, max_iterations):
    x_min, x_max = centerX - 2.0 / zoom, centerX + 2.0 / zoom
    y_min, y_max = centerY - 2.0 / zoom, centerY + 2.0 / zoom
    z_min, z_max = -1.0, 1.0  # Arbitrary depth mapping

    # Initialize 8x8x8 grid
    grid = [[[0 for _ in range(grid_size)] for _ in range(grid_size)] for _ in range(grid_size)]

    for z in range(grid_size):  # Z-layer (depth)
        for y in range(grid_size):  # Y-row
            for x in range(grid_size):  # X-column
                # Map (x, y, z) to the complex plane
                ReC = x_min + (x / grid_size) * (x_max - x_min)
                ImC = y_min + (y / grid_size) * (y_max - y_min)

                # Z-axis affects the imaginary part slightly
                depth_effect = z_min + (z / grid_size) * (z_max - z_min)
                adjusted_ImC = ImC + depth_effect

                # Calculate iterations
                iterations = recursive_mandelbrot(ReC, adjusted_ImC, 0, 0, 0, max_iterations)
                grid[z][y][x] = iterations

    return grid

# Map Mandelbrot set values to LED brightness
def map_to_led_cube(grid, max_iterations):
    led_brightness = [[[0 for _ in range(grid_size)] for _ in range(grid_size)] for _ in range(grid_size)]

    for z in range(grid_size):
        for y in range(grid_size):
            for x in range(grid_size):
                # Normalize iterations to brightness (0 to 255)
                brightness = int((grid[z][y][x] / max_iterations) * 255)
                led_brightness[z][y][x] = brightness

    return led_brightness

# Display brightness values on the LED cube
def display_on_cube(led_brightness):
    for z in range(grid_size):  # Iterate through Z-layers
        for y in range(grid_size):  # Iterate through rows
            for x in range(grid_size):  # Iterate through columns
                index = z * 64 + y * 8 + x  # Map 3D grid to 1D LED array
                brightness = led_brightness[z][y][x]
                led_cube[index] = (brightness, brightness, brightness)  # Set grayscale color
    led_cube.write()

# Wrapper function for Mandelbrot set
def mandelbrot_main(centerX, centerY, zoom, max_iterations):
    mandelbrot_grid = generate_mandelbrot_8x8x8(centerX, centerY, zoom, max_iterations)
    led_brightness = map_to_led_cube(mandelbrot_grid, max_iterations)
    display_on_cube(led_brightness)