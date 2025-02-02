# **Interactive Math Cube: 3D LED Fractal Visualizer**

A dynamic **8x8x8 LED cube** powered by a **Raspberry Pi Pico**, bringing **Julia and Mandelbrot fractals** to life with real-time sound-reactive lighting patterns. This project combines **mathematics, hardware design, and programming** to create a visually stunning and interactive experience.

---

## 🚀 **Features**
- 🔷 **Fractal Visualizations** – Displays **Julia and Mandelbrot sets** in 3D using Python-based algorithms.  
- 🎵 **Sound-Reactive Lighting** – Integrates a **sound sensor** to dynamically adjust lighting patterns based on audio input.  
- 🌟 **Brightness Modulation** – Uses **Taylor series** to enhance brightness control for smooth, dynamic visuals.  
- 🔧 **Custom Circuit Design** – Built with **KiCad**, featuring **transistor-based cathode control** and multiplexing for efficient power management.  
- 🔥 **Hand-Soldered Assembly** – Carefully soldered **512 LEDs** into an **8x8x8 cube**.  

---

## 🛠 **Components Used**

### 🔹 **Hardware**
- **Raspberry Pi Pico**
- **512 5mm LEDs**
- **Sound Sensor Module**
- **Transistors for cathode control**
- **Resistors and Capacitors for stability**
- **Custom PCB designed in KiCad**

### 🔹 **Software**
- **Python** – For fractal generation and lighting control
- **KiCad** – For circuit design
- **MicroPython** – For embedded programming

---

## ⚙️ **How It Works**
### **1️⃣ Fractal Generation**
- Implements **recursive algorithms** for **Julia and Mandelbrot sets** using complex numbers.  

### **2️⃣ Sound Integration**
- Captures **audio input** from the **sound sensor** and normalizes it to create **reactive light patterns**.  

### **3️⃣ Brightness Modulation**
- Uses a **Taylor series expansion** to achieve **smooth LED brightness transitions**.  

### **4️⃣ Control Circuitry**
- **Multiplexing enables efficient control of 128 connections** (64 anodes + 64 cathodes).  

---

## 📦 **Project Setup**

### 🔹 **Prerequisites**
- **Python 3.8+**
- **Raspberry Pi Pico** (flashed with **MicroPython firmware**)
- **KiCad** (for circuit design files)

### 🔹 **Installation**
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/interactive-math-cube.git
   cd interactive-math-cube

	2.	Install the required Python libraries:
   		pip install numpy micropython

## 🚀 **Upload Code to Raspberry Pi Pico**
1. **Flash the Raspberry Pi Pico** with MicroPython firmware.  
2. Upload the **`julia.py`**, **`mandelbrot.py`**, and **`main.py`** files to the Pico using a tool like **Thonny** or **ampy**.  

---

## 🎮 **Usage**
1. **Power on the LED cube** by connecting the Raspberry Pi Pico to a power source.  
2. Run **`main.py`** to initiate fractal visualizations or sound-reactive lighting.  

---

## 🛠 **Schematic and PCB**
The full **circuit schematic** and **PCB layout** are available in the **`kicad/`** directory. Open the files in **KiCad** to view or edit.  

---

## 📜 **License**
This project is licensed under the **MIT License**. See the `LICENSE` file for details.  
