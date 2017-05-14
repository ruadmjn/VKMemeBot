# -*- coding: utf-8 -*-
import time
from config import config
import telebot
from lib.core import vkMemes
bot = telebot.TeleBot(config.tg_token)

@bot.message_handler(commands=["meme", "start", "donat"])
def SendMeme(message):
    try:
        if "/start" in message.text:
            bot.reply_to(message, "Use /donat to support my future")
            bot.reply_to(message, "Use /meme to orat do gor")
        if "/donat" in message.text:
            bot.reply_to(message, "Here - 4817 7600 1285 8563")
        if "/meme" in message.text:
            time.sleep(1)
            bot.send_photo(message.chat.id, vkMemes.GetMeme())
    except:
        bot.reply_to(message, "Something went wrong. Repeat /meme ")
        time.sleep(2)
        SendMeme(message)

if __name__ == '__main__':
    bot.polling(none_stop=True)