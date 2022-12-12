import discohook.util

class WebhookMessage:
  def __init__(self, msg, fmt=False):
    self.msg = msg
    self.fmt = fmt

  def color(self):
    return None # None

  def asGithub(self):
    actor = discohook.util.lookup("TRIGGERING_ACTOR", prefix="GITHUB")
    attempt = discohook.util.lookup("RUN_ATTEMPT", prefix="GITHUB")
    repo = discohook.util.lookup("REPOSITORY", prefix="GITHUB")
    run = discohook.util.lookup("RUN_NUMBER", prefix="GITHUB")
    run_id = discohook.util.lookup("RUN_ID", prefix="GITHUB")
    sha = discohook.util.lookup("SHA", prefix="GITHUB")
    url = discohook.util.lookup("SERVER_URL", prefix="GITHUB")

    repo_url = f"{url}/{repo}"
    commit_url = f"{repo_url}/commit"
    action_url = f"{repo_url}/actions/runs"

    payload = [
      f"[{repo}]({repo_url}) (commit [{sha[0:7]}]({commit_url}/{sha}))"
    ]

    if attempt > 1:
      payload.append(f"Re-run of [#{run}]({action_url}/{run_id}) triggered by [{actor}]({repo_url}/{actor})")
    else:
      payload.append(f"Run [#{run}]({action_url}/{run_id}) triggered by [{actor}]({repo_url}/{actor})")

    payload.append("\n")
    payload.append(f"{type(self).__name__.lower()}: {self.msg}")
    return "\n".join(payload)

  def __str__(self):
    if self.fmt:
      return self.asGithub()

    return self.msg

class WebhookDebug(WebhookMessage):
  def color(self):
    return 5793266 # Blurple

class WebhookError(WebhookMessage):
  def color(self):
    return 15548997 # Red

class WebhookNotice(WebhookMessage):
  def color(self):
    return 5763719 # Green

class WebhookWarning(WebhookMessage):
  def color(self):
    return 16705372 # Yellow

WEBHOOK_KINDS = {
  "plain": WebhookMessage,
  "debug": WebhookDebug,
  "error": WebhookError,
  "notice": WebhookNotice,
  "warning": WebhookWarning
}
