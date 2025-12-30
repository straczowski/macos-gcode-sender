from serial import Serial
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get configuration from environment variables
serial_port = os.getenv('SERIAL_PORT')

# Validate required environment variable
if not serial_port:
    raise ValueError("SERIAL_PORT environment variable is not set. Please check your .env file.")

# Open grbl serial port
s = Serial(serial_port, 115200)

# Wake up grbl
s.write(str.encode("\r\n\r\n"))
time.sleep(3)   # Wait for grbl to initialize 
s.flushInput()  # Flush startup text in serial input

print("GRBL Interactive Console")
print("Type GCODE commands and press Enter to send")
print("Type 'exit' or 'quit' to close the connection\n")

# Interactive loop for custom GCODE commands
while True:
    try:
        command = input("GCODE> ").strip()
        
        if command.lower() in ['exit', 'quit']:
            break
        
        if not command:
            continue
            
        print(f'Sending: {command}')
        s.write(str.encode(command + '\n'))  # Send g-code block to grbl
        grbl_out = s.readline()  # Wait for grbl response with carriage return
        print(f' : {grbl_out.strip().decode("utf-8")}')
        
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        break

# Close serial port
print("Closing connection...")
s.close()

