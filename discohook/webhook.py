import requests

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

    self.session.post(self.url, data=data)

  def debug(self, msg):
    pass

  def error(self, msg):
    pass

  def notice(self, msg):
    pass

  def warning(self, msg):
    pass



response = requests.post(webhook_url, data={
  "username": username,
  "content": message
})




message = os.getenv("INPUT_MESSAGE")
avatar_url



s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})