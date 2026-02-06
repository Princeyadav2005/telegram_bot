import telebot

TOKEN = "8298963673:AAFg-03lG5d3-7UUqm_qHzkjDFKi0PvxF-I"
CHANNEL_ID = "@Tech_coarses"   # ya -100xxxxxx

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def handle_msg(m):

    text = f"""
📩 New Message

👤 Name: {m.from_user.first_name}
📝 Msg: {m.text}
"""

    bot.send_message(CHANNEL_ID, text)

bot.polling()
