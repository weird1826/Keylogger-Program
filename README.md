# PRODIGY_CS_04
## Keylogger Program in Python
- Thee project contains three files:
    1. `keylogger.py`
    2. `keylogger_server.py`
    3. `keylogs.txt`
- This keylogger program can be used 
    - To detect keylogs on a single computer
    - And can also log the keypresses of other computer on the same network
    - (you have to comment out some code in order to switch between these two functionalities)
### To detect keylogs on a single computer
- In the `keylogger.py` file, uncomment the `on_press_single(key)` function and comment out the `on_press(key)` function. Start the program.
- Do not interact with the `keylogger_server.py` file
- The keypresses will be saved in the `keylogs.txt` file.
- NOTE: You cannot stop the program with Ctrl+C. You have to forcefully terminate the execution of it.
### To detect keylogs on a computer on the same network
- In the `keylogger.py` file, uncomment the `on_press(key)` function and comment out the `on_press_single(key)` function
- Send this file to the other computer and start this python script on it
- Start the Apache HTTP Server on Port 80 on your computer
- Start the `keylogger_server.py` script on your computer
- The keypresses will be saved in the `keylogs.txt` file
