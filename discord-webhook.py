import discohook.kinds
import discohook.logger
import discohook.util
import discohook.webhook

logger = discohook.logger.Logger()

url = discohook.util.lookup("url")
usr = discohook.util.lookup("name")
pfp = discohook.util.lookup("avatar")
lvl = discohook.util.lookup("level")
fmt = discohook.util.lookup("format")
ttl = discohook.util.lookup("title")
msg = discohook.util.lookup("message")

logger.debug(f"Webhook endpoint is {url}")
logger.debug(f"Username for payload is {usr}")
logger.debug(f"Avatar profile for payload is {pfp}")
logger.debug(f"Webhook level is {lvl}")
logger.debug("Github notification format is ", end="")

if fmt:
  logger.debug("enabled.")
else:
  logger.debug("disabled.")

logger.debug(f"Title for payload is {ttl}")
logger.debug(f"Payload message is {msg}")

kind = discohook.kinds.WebhookMessage

if lvl not in discohook.kinds.WEBHOOK_KINDS:
  logger.warning(f"Unknown message kind {lvl}")
  logger.warning("Using a plain payload.")
else:
  kind = discohook.kinds.WEBHOOK_KINDS[lvl]

try:
  hook = discohook.webhook.Webhook(url, user=usr, avatar=pfp)
  res = hook.wire(kind(msg, fmt=fmt, ci=ci), title=ttl)

  if res.ok():
    logger.notice("Webhook payload was delivered successfully.")
  else:
    logger.error(f"Received unexpected error {res.code}: {res.msg}.")

except discohook.webhook.ErrorWebhookTimeout:
  logger.error("Connection timed out while trying to connect to Discord.")
except discohook.webhook.ErrorRequestProblem as err:
  logger.error(f"There is likely an issue with your settings for this Action.")
  logger.error(f"Received error code {err.code}: {err.msg}.")

if res.ok():
  logger.notice("webhook payload successfully delivered.")
else:
  logger.error(f"Payload for {kind} received unexpected code {res.code}.")
