import os
import telebot
import sys

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    print("TOKEN missing")
    sys.exit(1)

CHANNEL = "@Tech_coarses"

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
👤 Username: @{username}
🆔 ID: {user_id}

📝 Message:
{m.text}
"""

    bot.send_message(CHANNEL, text)


# Channel Reply → User
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
                    f"💬 Support Reply:\n\n{m.text}"
                )

            except:
                pass

            break


print("Bot Running...")

bot.polling(non_stop=True, interval=2, timeout=20)

