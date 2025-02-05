import telebot

TOKEN = "ISI_TOKEN_BOT_LO"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Hello, I'm Nier!")

print("Bot is running...")
bot.polling()
