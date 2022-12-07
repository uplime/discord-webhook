class Logger:
  def emit(self, level, msg):
    print(f"::{level} ::{msg}")

  def debug(self, msg):
    self.emit("debug", msg)

  def error(self, msg):
    self.emit("error", msg)

  def notice(self, msg):
    self.emit("notice", msg)

  def warn(self, msg):
    self.emit("warning", msg)
