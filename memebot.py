# -*- coding: utf-8 -*-
import time
from telebot import types
from config import config
import telebot
from lib.core import vkMemes
from lib.groups import groups

bot = telebot.AsyncTeleBot(config.tg_token)


@bot.message_handler(commands=["back"])
def ChooseCategory(message):
    if "back" in message.text:
        button_category = types.KeyboardButton(text="/category")
        button_donat = types.KeyboardButton(text="/donat")
        keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        keyboard.add(button_category, button_donat)
        bot.reply_to(message, "back", reply_markup=keyboard)


@bot.message_handler(commands=["start", "donat", "category", "amoral", "story", "gif"])
def SendMeme(message):
    category = "amoral"
    categoryKeyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)

    button_category = types.KeyboardButton(text="/category")
    button_donat = types.KeyboardButton(text="/donat")
    keyboard.add(button_category, button_donat)

    button_category_amoral = types.KeyboardButton(text="/amoral")
    button_category_story = types.KeyboardButton(text="/story")
    button_category_gif = types.KeyboardButton(text="/gif")
    button_category_back = types.KeyboardButton(text="/back")
    categoryKeyboard.add(button_category_amoral, button_category_story, button_category_gif, button_category_back)
    try:
        if "amoral" in message.text:
            category = "amoral"
        if "story" in message.text:
            category = "story"
        if "gif" in message.text:
            category = "gif"

        if "start" in message.text:
            bot.send_message(message.chat.id, "Use /donat to support my future", reply_markup=keyboard)
            bot.send_message(message.chat.id, "Select /category and ori do gor", reply_markup=keyboard)
        if "donat" in message.text:
            bot.reply_to(message, "Here - 4817 7600 1285 8563", reply_markup=keyboard)
        if "amoral" in message.text or "story" in message.text or "gif" in message.text:
            randomPost = vkMemes.GetMeme(category)
            if randomPost is None:
                time.sleep(2)
                SendMeme(message)
            if "photo" in randomPost:
                bot.send_photo(message.chat.id, randomPost["photo"], reply_markup=categoryKeyboard)
            if "text" in randomPost:
                bot.send_message(message.chat.id, str(randomPost["text"]).replace('<br>','\n'), reply_markup=categoryKeyboard)
            if "gif" in randomPost:
                bot.send_document(message.chat.id, randomPost["gif"]["doc"],
                                  caption=str(randomPost["gif"]["caption"]).replace('<br>','\n'),
                                  reply_markup=categoryKeyboard,
                                  )
        if "category" in message.text:
            bot.reply_to(message, "Choose", reply_markup=categoryKeyboard)
    except Exception as ex:
        if "Telegram" in ex.args[0]:
            bot.send_message(message.chat.id, "Too much peoples want memes. Telegram has limits. (We not) Just wait")
        config.tries -= 1
        if config.tries > 0:
            time.sleep(2)
        if "Telegram" not in ex.args[0]:
            bot.reply_to(message, "try later", reply_markup=categoryKeyboard)

if __name__ == '__main__':
    bot.polling(none_stop=True)