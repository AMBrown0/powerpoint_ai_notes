import os
import requests

# Get the Bard API key from your Google Cloud Platform project
API_KEY = "AIzaSyBM1oSmZzdlSyKiUqVyIGpMiu-MT7iiTdE"

# Create a Bard client
client = requests.Session()
client.headers["Authorization"] = "Bearer " + API_KEY

# Send a request to the Bard API
request = {
    "text": "Write a Python function that checks if a number is prime.",
    "lang": "python",
}
response = client.post("https://bard.googleapis.com/v1/generate", json=request)

# Check the response status code
if response.status_code == 200:
    # Get the generated code
    code = response.json()["text"]

    # Print the generated code
    print(code)
else:
    print("Error:", response.status_code)
