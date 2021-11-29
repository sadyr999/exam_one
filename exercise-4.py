import telebot
from telebot import types

TOKEN = '2101170188:AAGMH-kNofkmKQVMg280Jz6an8I10DyoEVs'
bot = telebot.TeleBot(TOKEN)

# bot name is "@itacademy9999exam_bot"


@bot.message_handler(content_types=["text"])
def counter(message):
    chat_id = message.chat.id
    counter = 0
    for i in message.text:
        if i in ('a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'):
            counter += 1
    bot.send_message(chat_id, counter)

bot.polling()