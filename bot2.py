import telebot

TOKEN = '8788945893:AAF_tazl6e2kNQlHmpRDghhQb6VDbxpnTUE'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def get_id(message):
    print(f"Твой ID: {message.from_user.id}")
    bot.reply_to(message, f"Ваш ID: {message.from_user.id} сохранен!")

print("Бот запущен. Напиши ему что угодно в Telegram...")
bot.polling()
