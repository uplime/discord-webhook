# Discord Webhook

GitHub Action for writing to a Discord Webhook.

## Inputs

  - `webhook-url`

**Required** The webhook endpoint to write to.

  - `username`

Username to identify as with Discord.

  - `avatar`

URL of the avatar to use for the message.

  - `message`

Send a plain message to the webhook.

  - `debug`

Send a debug message to the webhook.

  - `error`

Send an error message to the webhook.

  - `notice`

Send an informational notice to the webhook.

  - `warn`

Send a warning message to the webhook.

> N.B. At least one of the following must be used: message, debug, error,
> notice, or warn.

## Example usage

```yaml
uses: actions/discord-webhook@v1
with:
  webhook-url: https://discord.com/api/webhooks/123457890/correct-horse-battery-staple
  username: Action Bot 900
  avatar: https://cabbages.com/my.png
  warn: "I'm Afraid I Can't Do That, Dave."
```
