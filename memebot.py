# -*- coding: utf-8 -*-
from config import config
import telebot
from lib.core import vkMemes
bot = telebot.TeleBot(config.tg_token)

@bot.message_handler(commands=["meme", "start", "donat"])
def SendMeme(message):
    if message.text == "/start":
        bot.reply_to(message, "Use /donat to support my future")
        bot.reply_to(message, "Use /meme to orat do gor")
    if message.text == "/donat":
        bot.reply_to(message, "Here - 4817 7600 1285 8563")
    if message.text == "/meme":
        bot.send_photo(message.chat.id, vkMemes.GetMeme())

if __name__ == '__main__':
    bot.polling(none_stop=True)