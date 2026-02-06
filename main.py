import os
import telebot
import sys

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    print("❌ TOKEN missing")
    sys.exit(1)

CHANNEL_ID = "@Tech_coarses"
CHANNEL_USERNAME = "Tech_coarses"   # without @

bot = telebot.TeleBot(TOKEN)


# User → Channel
@bot.message_handler(func=lambda m: m.chat.type == "private")
def user_msg(m):

    name = m.from_user.first_name or "User"
    username = m.from_user.username or "NoUsername"
    user_id = m.from_user.id

    text = f"""
📩 New Message

👤 Name: {name}
🆔 Username: @{username}
🆔 ID: {user_id}

📝 Message:
{m.text}
"""

    bot.send_message(CHANNEL_ID, text)


# Channel → User (Reply Handler)
@bot.message_handler(func=lambda m: m.chat.type == "channel")
def channel_reply(m):

    if not m.reply_to_message:
        return

    old = m.reply_to_message.text

    for line in old.split("\n"):
        if "ID:" in line:
            try:
                user_id = int(line.split("ID:")[1].strip())

                bot.send_message(
                    user_id,
                    f"📩 Support Team:\n\n{m.text}"
                )
            except:
                pass

            break


print("✅ Bot Running...")

bot.polling(non_stop=True)
