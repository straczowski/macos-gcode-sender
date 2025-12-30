from serial import Serial
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get configuration from environment variables
serial_port = os.getenv('SERIAL_PORT')
gcode_filepath = os.getenv('GCODE_FILEPATH')

# Validate required environment variables
if not serial_port:
    raise ValueError("SERIAL_PORT environment variable is not set. Please check your .env file.")
if not gcode_filepath:
    raise ValueError("GCODE_FILEPATH environment variable is not set. Please check your .env file.")

# Open grbl serial port
s = Serial(serial_port, 115200)

# Open g-code file
f = open(gcode_filepath, 'r');

# Count total lines for progress tracking
total_lines = sum(1 for _ in f)
f.seek(0)  # Reset file pointer to beginning

# Wake up grbl
s.write(str.encode("\r\n\r\n"))
time.sleep(3)   # Wait for grbl to initialize 
s.flushInput()  # Flush startup text in serial input

# Stream g-code to grbl
current_line = 0
for line in f:
    current_line += 1
    progress_pct = (current_line / total_lines) * 100
    l = line.strip() # Strip all EOL characters for consistency
    print(f'[{progress_pct:6.2f}%] [{current_line}/{total_lines}] Sending: ' + l,)
    s.write(str.encode(l + '\n')) # Send g-code block to grbl
    grbl_out = s.readline() # Wait for grbl response with carriage return
    print(grbl_out.strip().decode('utf-8'))

# Wait here until grbl is finished to close serial port and file.
input("  Press <Enter> to exit and disable grbl.") 

# Close file and serial port
f.close()
s.close()