import requests

class WebhookResponse:
  def __init__(self, code, msg):
    self.code = code
    self.msg = msg

  def ok(self):
    return self.code >= 200 and self.code < 300

class Webhook:
  def __init__(self, url, username=None, avatar=None):
    self.url = url
    self.username = username
    self.avatar = avatar

    self.payload = {
      "username": self.username,
      "avatar_url": self.avatar
    }

#    if self.avatar is not None:
#      self.payload["avatar_url"] = self.avatar

    self.session = requests.Session()

    self.session.headers.update({
      "User-Agent": "gh/uplime/discord-webhook"
    })

  def wire(self, msg, embed=False, color=None, title=None):
    if embed:
      self.payload["embeds"] = [
        {"color": color, "title": title, "description": msg}
      ]
    else:
      self.payload["content"] = msg

    import json
    print(self.payload)
    print(json.dumps(self.payload))

    res = self.session.post(self.url, data=self.payload)
    return WebhookResponse(res.status_code, res.content)

  def debug(self, msg, title=None):
    return self.wire(msg, embed=True, title=title)

  def error(self, msg, title=None):
    return self.wire(msg, embed=True, title=title)

  def notice(self, msg, title=None):
    return self.wire(msg, embed=True, color=5763719, title=title)

  def warning(self, msg, title=None):
    return self.wire(msg, embed=True, title=title)
