import telebot
from telebot import types
import os, signal, pickle, sys

bot = telebot.TeleBot('7423073356:AAFepO2Qx2lUhk9brXXXHkuLoDSWQvfJzyM')

@bot.message_handler(commands=['start'])
def user(message):
    sent = bot.send_message(message.chat.id, "Здравствуйте, поделитесь контактом, плиз")
    keyboard.add(reg_button)
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    reg_button = types.KeyboardButton(text="Поделиться контактом", request_contact=True)


if __name__ == '__main__':
     bot.infinity_polling(none_stop=True)
