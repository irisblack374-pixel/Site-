# Security

## Reporting a security issue

Please do not publish bot tokens, API keys, passwords, or other secrets in issues or pull requests.

If you find a security problem in this project, report it privately to the repository owner through GitHub rather than posting sensitive details publicly.

## Token safety

The Discord bot token belongs in a local `.env` file:

```env
DISCORD_TOKEN=YOUR_BOT_TOKEN
```

Never commit `.env` or paste a real token into GitHub.

If a token is exposed, immediately reset it in the Discord Developer Portal.

## Privacy-friendly analytics

Site- keeps command usage and error counters in memory while the bot is running. These counters are not uploaded to an external analytics service. Restarting the bot resets them. The `/stats` command shows aggregate bot statistics.
