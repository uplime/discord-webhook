class Logger:
  def emit(self, level, msg, **opts):
    print(f"::{level} ::{msg}", **opts)

  def debug(self, msg, **opts):
    self.emit("debug", msg, **opts)

  def error(self, msg, **opts):
    self.emit("error", msg, **opts)

  def notice(self, msg, **opts):
    self.emit("notice", msg, **opts)

  def warning(self, msg, **opts):
    self.emit("warning", msg, **opts)
