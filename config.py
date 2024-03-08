TOKEN = "YOUR_TOKEN_HERE"

admin = ""





















# Other config part (don't touch it for correct bot work)
import json

if not TOKEN or TOKEN == "YOUR_TOKEN_HERE":
    raise ImportError("API key is empty!")

admin_id = None
admin_username = None

if not admin or admin.strip() == "":
    raise ImportError("Admin id or admin username are empty")
else:
    try:
        admin_id = int(admin)
    except:
        admin_username = admin

admin_link = (
    f"<b><i><a href='tg://user?id={admin_id}'>Click</a></i></b>" 
    if admin_id 
    else f"<b>@{admin_username}</b>"
)

help_message = f"""
<b>Contact admin</b>: {admin_link}
"""

default_start_message = f"""<b>Hi there!</b>
<i>I am your neighborhood anti-profanity bot, here to help you maintain a polite and clean chat! 😊</i>

<b>What I can do for you is as follows:</b>
- <i>Remove rude words from the text and substitute them with more appropriate ones.</i>
- <i>Recognize and mark anything in your conversations that can be considered inappropriate.</i>
- <i>Make the conversation space safer and more cozy for all parties.</i>

<i>Please don't hesitate to contact me at any time. Together, let's work to improve this community! 💬</i>

<b>Contact me</b>: {admin_link} 
"""

_custom_words_file = 'custom_words.json'

# Custom profanity words
with open(_custom_words_file, 'r', encoding='utf-8') as f:
    custom_words: list[str] = json.load(f)['words']

markup = 'html'

default_language = 'auto'

profanity_percent = 78#%