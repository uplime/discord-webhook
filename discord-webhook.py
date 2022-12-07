import discohook.logger
import discohook.webhook
import os

def make_pair(msg):
  return [msg, os.getenv(f"INPUT_{msg.upper()}")]

webhook_url = os.getenv("INPUT_WEBHOOK-URL")
user = os.getenv("INPUT_USERNAME")
pfp = os.getenv("INPUT_AVATAR")

msg_types = [
  "message", "debug", "error",
  "notice", "warn"
]

msgs = dict(map(make_pair, msg_types))
used_msgs = list(filter(lambda msg: msg is not None, msgs.values()))
logger = discohook.logger.Logger()

if len(used_msgs) == 0:
  logger.error("No messages given.")
  os.exit(1)

webhook = discohook.webhook.Webhook(webhook_url, username=user, avatar=pfp)
res = webhook.wire(msgs["message"])

if res.ok():
  logger.notice("webhook payload successfully delivered.")
else:
  logger.error(f"unexpected code {res.code} received.")
  os.exit(1)
