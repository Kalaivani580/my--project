import requests

url = "http://127.0.0.1:5000/write"
payload = {"message": "Hello from the second file!"}

try:
    response = requests.post(url, json=payload)
    print("Response Status:", response.status_code)
    print("Response Data:", response.json())
except Exception as e:
    print("Error sending request:", str(e))
