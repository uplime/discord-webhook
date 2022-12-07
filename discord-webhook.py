import discohook.logger
import os
import requests

webhook_url = os.getenv("INPUT_WEBHOOK-URL")
username = os.getenv("INPUT_USERNAME")
message = os.getenv("INPUT_MESSAGE")

response = requests.post(webhook_url, data={
  "username": username,
  "content": message
})

logger = discohook.logger.Logger()

if response.status_code >= 200 and response.status_code < 300:
  logger.notice("webhook payload successfully delivered.")
else:
  logger.error(f"unexpected code {response.status_code} received.")
  os.exit(1)
