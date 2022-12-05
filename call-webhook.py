import os
import requests

webhook_url = os.getenv("INPUT_WEBHOOK-URL")
username = os.getenv("INPUT_USERNAME")
message = os.getenv("INPUT_MESSAGE")

response = requests.post(webhook_url, data={
  "username": username,
  "content": message
})

print(response)
