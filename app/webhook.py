class Webhook:
  def __init__(self, endpoint):
    self.endpoint = endpoint

  def wire(self, msg):
    pass

  def debug(self, msg):
    pass

  def error(self, msg):
    pass

  def notice(self, msg):
    pass

  def warning(self, msg):
    pass
