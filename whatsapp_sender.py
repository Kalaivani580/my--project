# whatsapp_sender.py
import pywhatkit as kit
import datetime

# Your contact number in international format
phone_number = "+916382342240"  # Replace with the recipient's number

# Message to send
message = "Hello! This is an automated message sent via Python 😊"

# Send time (1 minute from now)
now = datetime.datetime.now()
hour = now.hour
minute = now.minute + 1  # sends the message in 1 minute

# Send the WhatsApp message
kit.sendwhatmsg("+919865138524", "hi amma this is automate msg", 0, 2)
