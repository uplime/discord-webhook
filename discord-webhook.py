import discohook.logger
import discohook.webhook
import os
import sys

def make_pair(kind):
  msg = os.getenv(f"INPUT_{kind.upper()}")

  if msg == "":
    msg = None

  return [kind, msg]

webhook_url = os.getenv("INPUT_WEBHOOK-URL")
user = os.getenv("INPUT_USERNAME")
pfp = os.getenv("INPUT_AVATAR")

msg_kinds = [
  "message", "debug", "error",
  "notice", "warn"
]

msgs = dict(map(make_pair, msg_kinds))
used_msgs = list(filter(lambda msg: msg is not None, msgs.values()))
logger = discohook.logger.Logger()

if len(used_msgs) == 0:
  logger.error("No messages given.")
  sys.exit(1)

webhook = discohook.webhook.Webhook(webhook_url, username=user, avatar=pfp)

for kind in msgs:
  if msgs[kind] is None:
    next

  fn_name = kind

  if fn_name == "message":
    fn_name = "wire"

  fn = getattr(webhook, fn_name)

  if fn is None:
    logger.warn(f"Could not find suitable message kind for {kind}")
    next

  print(fn_name)
  print(fn)
  print(kind)
  print(msgs)
  print(webhook.wire)

  res = fn(msgs[kind])

  print(res)

  if res.ok():
    logger.notice("webhook payload successfully delivered.")
  else:
    logger.error(f"unexpected code {res.code} received.")
    sys.exit(1)
