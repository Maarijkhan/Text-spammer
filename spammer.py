import pyautogui as auto
import keyboard
import time
import threading

# Flag to control the action
writing = False
spammer=input("Enter a thing to spam: ")

# Function to perform the writing and pressing action
def writer():
    while True:
        if writing:
            auto.write(spammer)
            auto.press('enter')
            time.sleep(0.1)  # Add a short delay to avoid too fast actions

# Function to toggle the action
def toggle_writing():
    global writing
    writing = not writing
    if writing:
        print("Writing started.")
    else:
        print("Writing stopped.")

# Register the hotkey
keyboard.add_hotkey('ctrl+shift+h', toggle_writing)

# Start the writer thread
write_thread = threading.Thread(target=writer)
write_thread.start()

print("\nPress Ctrl+Shift+h to toggle the writing action.")

# Keep the script running
keyboard.wait('esc')  # You can also use another hotkey to exit
