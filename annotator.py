import telebot

BOT_TOKEN = "6450255715:AAGfaBYjvKuLCFSyLlnYoS1Ptevcw1ZYr6U"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def hello_message(message):
    bot.reply_to(message, "How you doing:)")
    
@bot.message_handler(func= lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)
    
bot.infinity_polling()