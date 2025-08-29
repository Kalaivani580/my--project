from flask import Flask, request, jsonify
import pyautogui
import time
import os
import subprocess
from datetime import datetime

app = Flask(__name__)

filename = "saschicgiftsdemo.txt"
file_path = os.path.join(os.getcwd(), filename)

def open_notepad(new_file=False):
    if new_file:
        subprocess.Popen("notepad.exe")
    else:
        subprocess.Popen(["notepad.exe", file_path])
    time.sleep(1.5)

@app.route("/write", methods=["POST"])
def write_to_notepad():
    try:
        data = request.get_json(force=True, silent=True)
        if not data or "message" not in data:
            return jsonify({
                "error": "Missing or invalid JSON",
                "received_raw": request.data.decode()
            }), 400

        user_text = data["message"]
        timestamp = datetime.now().strftime("[%d-%m-%Y %H:%M:%S] ")
        full_message = timestamp + user_text

        if not os.path.exists(file_path):
            open_notepad(new_file=True)
            pyautogui.write(full_message, interval=0.05)
            pyautogui.hotkey("ctrl", "s")
            time.sleep(1)
            pyautogui.write(file_path)
            pyautogui.press("enter")
            return jsonify({"status": "created", "message": f"Created {filename}"}), 201
        else:
            open_notepad(new_file=False)
            pyautogui.hotkey("ctrl", "end")
            pyautogui.press("enter")
            pyautogui.write(full_message, interval=0.05)
            pyautogui.hotkey("ctrl", "s")
            return jsonify({"status": "updated", "message": f"Appended to {filename}"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
