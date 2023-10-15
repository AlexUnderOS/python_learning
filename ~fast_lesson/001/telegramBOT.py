import telebot

bot = telebot.TeleBot("6462503957:AAFZfbBlb4dQrYrlNqKUaUCk6I64aqbnAF0", parse_mode=None)


@bot.message_handler(content_types=['text'])
def send_echo(message):
    a = message.text
    c = int(a) + int(a)
    bot.send_message(message.chat.id, c)
 
bot.polling(none_stop=True)