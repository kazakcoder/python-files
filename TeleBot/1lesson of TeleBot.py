import telebot


BOT_TOKEN = "your telebot token"#bot token
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def sent_hello(message):
    bot.reply_to(message,text="hi")

bot.infinity_polling()
