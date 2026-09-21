<div align="center">
<img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="70" alt="Site icon">
<h1>Site-</h1>
<p><b>Simple Discord Bot • Python • discord.py</b></p>
<p>A clean Discord bot project focused on useful commands and a simple structure.</p>
</div>

---

## <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/commands.svg" width="28" align="absmiddle"> COMMANDS

| Command | Description |
|---|---|
| `/ping` | Checks the bot response |
| `/server` | Shows server information |
| `/user` | Shows user information |
| `/avatar` | Displays a user's avatar |
| `/help` | Shows the available commands |

---

## <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/python.svg" width="28" align="absmiddle"> TECHNOLOGY

- Python
- discord.py
- python-dotenv

---

## PROJECT STRUCTURE

```
Site-/
├── bot.py
├── .env
├── requirements.txt
└── README.md
```

### bot.py
The main bot file. It contains the Discord client and command logic.

### .env
Stores the Discord bot token locally.

Example:

```env
DISCORD_TOKEN=your_token_here
```

Do not publish your real token.

### requirements.txt
Contains the Python dependencies required by the project.

---

## HOW IT WORKS

```
Discord
   ↓
Bot
   ↓
Command
   ↓
Response
```

The bot receives a command from Discord, processes it through the command handler, and returns the requested information.

---

## RUN

Install the dependencies:

```bash
pip install -r requirements.txt
```

Then start the bot:

```bash
python bot.py
```

Make sure the bot token is configured in `.env`.

---

## PROJECT STYLE

**Simple. Clean. Practical.**

The project is intentionally structured so it is easy to understand, modify and expand.

<div align="center">
<img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="42">
<br><br>
<b>BUILD • TEST • EVOLVE</b>
<br>
2026
</div>