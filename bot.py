import telebot

TOKEN = "7685749632:AAGBtpwSSSu-Dv-Frs1fkdbzClSg01Vob4A"  # Получи токен у @BotFather
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['привет'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я бот, запущенный в Pydroid 3.")

bot.polling()
