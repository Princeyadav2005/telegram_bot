import os
import telebot

TOKEN = os.getenv("8298963673:AAGKdMgTz9OfLSOML7riP0JRiGikdw8TXlo")
CHANNEL_ID = "@Tech_coarses"   # your channel

bot = telebot.TeleBot(TOKEN)

# Store users (simple memory)
users = {}


# When user sends message to bot
@bot.message_handler(func=lambda m: m.chat.type == "private")
def user_msg(m):

    users[m.from_user.id] = True   # save user

    name = m.from_user.first_name or "User"
    username = m.from_user.username or "NoUsername"

    text = f"""
📩 New Message

👤 Name: {name}
🆔 Username: @{username}
🆔 ID: {m.from_user.id}

📝 Msg:
{m.text}
"""

    bot.send_message(CHANNEL_ID, text)


# When you reply in channel
@bot.message_handler(func=lambda m: m.chat.username == CHANNEL_ID.replace("@", ""))
def channel_reply(m):

    if m.reply_to_message:

        old = m.reply_to_message.text

        # find user id from old msg
        for line in old.split("\n"):
            if "ID:" in line:
                user_id = int(line.split("ID:")[1].strip())

                bot.send_message(
                    user_id,
                    f"📩 Reply from Admin:\n\n{m.text}"
                )
                break


print("Bot is running...")

bot.polling(non_stop=True)
