# -*- coding: utf-8 -*-
import time
from telebot import types
from config import config
import telebot
from lib.core import vkMemes
bot = telebot.TeleBot(config.tg_token)

@bot.message_handler(commands=["meme", "start", "donat"])
def SendMeme(message):
    try:
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_meme = types.KeyboardButton(text="meme")
        button_donat = types.KeyboardButton(text="donat")
        keyboard.add(button_meme, button_donat)
        if "start" in message.text:
            bot.reply_to(message, "Use /donat to support my future", reply_markup=keyboard)
            bot.reply_to(message, "Use /meme to orat do gor", reply_markup=keyboard)
        if "donat" in message.text:
            bot.reply_to(message, "Here - 4817 7600 1285 8563", reply_markup=keyboard)
        if "meme" in message.text:
            bot.send_photo(message.chat.id, vkMemes.GetMeme(), reply_markup=keyboard)
    except Exception as ex:
        bot.reply_to(message, "Something went wrong. Repeat /meme ")
        config.tries -= 1
        if config.tries > 0:
            time.sleep(1)
        else:
            time.sleep(6)
        SendMeme(message)

if __name__ == '__main__':
    bot.polling(none_stop=True)