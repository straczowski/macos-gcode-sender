# macos-gcode-sender
A lightweight Python G-code sender for macOS, running in a Conda environment.

This project includes two scripts:
- `file_stream.py` - sends a G-code file to your controller
- `interactive_stream.py` - interactive mode to manually send G-code commands. Useful to bring your machine into position.

Set up the `.env` file before starting the scripts.

## Installation

### Create Conda Environment

```sh
conda env create -f environment.yml
```

### Activate Environment

```sh
conda activate gcode-sender
```

## Configuration

1. Copy the example environment file:

```sh
cp .env.example .env
```

2. Edit `.env` and set your configuration:
   - `SERIAL_PORT`: Your GRBL controller's serial port (find it with `ls /dev/tty.*`) after it was connected
   - `GCODE_FILEPATH`: Path to the G-code file (only needed for `file_stream.py`)

## Usage

1. Connect your GRBL controller via USB

2. Find the connected device in terminal:

```sh
ls /dev/tty.*
```

3. Update the `SERIAL_PORT` in your `.env` file with the device path

4. Run a script:

**File streaming:**
```sh
python file_stream.py
```

**Interactive mode:**
```sh
python interactive_stream.py
```

