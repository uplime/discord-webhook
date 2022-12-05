# Discord Webhook

GitHub Action for writing to a Discord Webhook.

## Inputs

  - `webhook-url`

**Required** The webhook endpoint to write to.

  - `username`

Username to identify as with Discord.

  - `message`

Message to write to the webhook.

## Example usage

```yaml
uses: actions/discord-webhook@v1
with:
  webhook-url: https://discord.com/api/webhooks/123457890/correct-horse-battery-staple
  username: Action Bot 900
  message: Hello, world!
```
