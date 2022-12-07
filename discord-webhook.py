import discohook.logger
import discohook.webhook
import os

webhook_url = os.getenv("INPUT_WEBHOOK-URL")
username = os.getenv("INPUT_USERNAME")
message = os.getenv("INPUT_MESSAGE")
avatar = os.getenv("INPUT_AVATAR")

webhook_opts = {
  "user": username, "avatar": avatar
}

logger = discohook.logger.Logger()
webhook = discohook.webhook.Webhook(webhook_url, **webhook_opts)
res = webhook.wire(message)

if res.ok():
  logger.notice("webhook payload successfully delivered.")
else:
  logger.error(f"unexpected code {res.code} received.")
  os.exit(1)
