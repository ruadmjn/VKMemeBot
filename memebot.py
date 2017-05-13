# -*- coding: utf-8 -*-
from config import config
import telebot
from lib.core import vkMemes
bot = telebot.TeleBot(config.tg_token)

@bot.message_handler(commands=["meme", "start"])
def SendMeme(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, "Use /meme to orat do gor")
    bot.send_photo(message.chat.id, vkMemes.GetMeme())

if __name__ == '__main__':
    bot.polling(none_stop=True)