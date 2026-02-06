import os
import telebot
import sys

# Token Railway env se lega
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    print("❌ TOKEN not found")
    sys.exit(1)

CHANNEL_ID = "@Tech_coarses"   # apna channel username

bot = telebot.TeleBot(TOKEN)


# Jab bhi user message bheje
@bot.message_handler(func=lambda m: m.chat.type == "private")
def user_message(m):

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


# Admin reply → User
@bot.message_handler(func=lambda m: m.chat.username == CHANNEL_ID.replace("@", ""))
def admin_reply(m):

    if m.reply_to_message:

        old_msg = m.reply_to_message.text

        for line in old_msg.split("\n"):
            if "ID:" in line:
                user_id = int(line.split("ID:")[1].strip())

                bot.send_message(
                    user_id,
                    f"📩 Support:\n\n{m.text}"
                )
                break


print("✅ Bot Running...")

bot.polling(non_stop=True)
