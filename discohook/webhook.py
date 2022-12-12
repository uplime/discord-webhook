import requests

class ErrorWebhookTimeout(requests.exceptions.ConnectTimeout):
  pass

class ErrorRequestProblem(Exception):
  def __init__(self, code, msg):
    self.code = code
    self.msg = msg

class WebhookResponse:
  def __init__(self, code, msg):
    self.code = code
    self.msg = msg

  def ok(self):
    return self.code >= 200 and self.code < 300

class Webhook:
  def __init__(self, url, user=None, avatar=None):
    self.url = url
    self.username = user
    self.avatar = avatar

    self.payload = {
      "username": self.username,
      "avatar_url": self.avatar
    }

    self.session = requests.Session()

    self.session.headers.update({
      "User-Agent": "gh/uplime/discord-webhook"
    })

  def wire(self, msg, title=None):
    self.payload["embeds"] = [
      {"color": msg.color(), "title": title, "description": str(msg)}
    ]

    try:
      res = self.session.post(self.url, json=self.payload, timeout=5)

      if res.status_code >= 400 and res.status_code < 500:
        raise ErrorRequestProblem(res.status_code, res.content)

      return WebhookResponse(res.status_code, res.content)

    except requests.exceptions.ConnectTimeout:
      raise ErrorWebhookTimeout

  def debug(self, msg, title=None):
    return self.wire(msg, embed=True, title=title)

  def error(self, msg, title=None):
    return self.wire(msg, embed=True, title=title)

  def notice(self, msg, title=None):
    return self.wire(msg, embed=True, color=5763719, title=title)

  def warning(self, msg, title=None):
    return self.wire(msg, embed=True, title=title)
