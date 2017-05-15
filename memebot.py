# -*- coding: utf-8 -*-
import time
from telebot import types
from config import config
import telebot
from lib.core import vkMemes
from lib.groups import groups

bot = telebot.TeleBot(config.tg_token)

class choose:
    category = "amoral"

@bot.message_handler(commands=["amoral", "podslusheno"])
def ChooseCategory(message):
    if "amoral" in message.text:
        choose.category = "amoral"
    if "podslusheno" in message.text:
        choose.category = "podslusheno"
    button_meme = types.KeyboardButton(text="/meme")
    button_category = types.KeyboardButton(text="/category")
    button_donat = types.KeyboardButton(text="/donat")
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(button_meme, button_category, button_donat)
    bot.reply_to(message, "Category "+choose.category, reply_markup=keyboard)


@bot.message_handler(commands=["meme", "start", "donat", "category"])
def SendMeme(message):
    try:
        categoryKeyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)

        button_meme = types.KeyboardButton(text="/meme")
        button_category = types.KeyboardButton(text="/category")
        button_donat = types.KeyboardButton(text="/donat")
        keyboard.add(button_meme, button_category, button_donat)

        button_category_amoral = types.KeyboardButton(text="/amoral")
        button_category_podslusheno = types.KeyboardButton(text="/podslusheno")
        categoryKeyboard.add(button_category_amoral, button_category_podslusheno)

        if "start" in message.text:
            bot.reply_to(message, "Use /donat to support my future", reply_markup=keyboard)
            bot.reply_to(message, "Use /meme to orat do gor", reply_markup=keyboard)
        if "donat" in message.text:
            bot.reply_to(message, "Here - 4817 7600 1285 8563", reply_markup=keyboard)
        if "meme" in message.text:
            randomPost = vkMemes.GetMeme(choose.category)
            if "photo" in randomPost:
                bot.send_photo(message.chat.id, randomPost["photo"], reply_markup=keyboard)
            if "text" in randomPost:
                bot.reply_to(message, str(randomPost["text"]).replace('<br>','\n'), reply_markup=keyboard)
        if "category" in message.text:
            bot.reply_to(message, "Choose", reply_markup=categoryKeyboard)
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