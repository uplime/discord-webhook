import requests

class WebhookResponse:
  def __init__(self, code, msg):
    self.code = code
    self.msg = msg

  def ok(self):
    return self.code >= 200 and self.code < 300

class Webhook:
  def __init__(self, url, user=None, avatar=None):
    self.url = url
    self.user = user
    self.avatar = avatar
    self.session = requests.Session()

    self.session.headers.update({
      "User-Agent": "gh/uplime/discord-webhook"
    })

  def wire(self, msg):
    data = {
      "username": self.user,
      "content": msg
    }

    if self.avatar is None:
      data["avatar_url"] = self.avatar

    res = self.session.post(self.url, data=data)
    return WebhookResponse(res.status_code, res.content)

  def debug(self, msg):
    pass

  def error(self, msg):
    pass

  def notice(self, msg):
    pass

  def warning(self, msg):
    pass
