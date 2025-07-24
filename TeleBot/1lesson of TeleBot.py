import telebot


BOT_TOKEN = "your telebot token"#bot token бот токеніңіз
bot = telebot.TeleBot(BOT_TOKEN)#бот жасау интализация

@bot.message_handler(commands=["start"])#команда орында мысалы бот басталғанда start командасын басса hi деп жазады
def sent_hello(message):
    bot.reply_to(message,text="hi")#текст жазуга

bot.infinity_polling()
