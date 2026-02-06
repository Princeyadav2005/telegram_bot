import os
import telebot

# Get token from Railway variable
TOKEN = os.getenv("8298963673:AAGKdMgTz9OfLSOML7riP0JRiGikdw8TXlo")

CHANNEL_ID = "@Tech_coarses"   # ya -100xxxxxxxxx

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda m: True)
def handle_msg(m):

    name = m.from_user.first_name or "User"
    username = m.from_user.username or "NoUsername"

    text = f"""
📩 New Message

👤 Name: {name}
🆔 Username: @{username}
📝 Msg: {m.text}
"""

    bot.send_message(CHANNEL_ID, text)


print("Bot is running...")

bot.polling(non_stop=True)



