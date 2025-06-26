import requests

url = 'http://127.0.0.1:5000/predict'

payload = {
    "text": "I'm feeling really anxious about exams"
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
