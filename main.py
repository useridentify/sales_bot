# В данном примере используем pyTelegramBotAPI
import telebot

# Создаем бота с токеном
bot = telebot.TeleBot('7423073356:AAFepO2Qx2lUhk9brXXXHkuLoDSWQvfJzyM')

# Создаем обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    # создаем кнопку и клавиатуру для отправки контакта
    btn_phone = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_phone.add(telebot.types.KeyboardButton(text='Отправить свой контакт ☎️', request_contact=True))
    # Отправляем приветственное сообщение с кнопкой
    bot.send_message(message.chat.id, 'Привет! Отправь мне свой контакт, чтобы я записал твои данные и продал их на китайском  теневом рынке :D', reply_markup=btn_phone)

# Запускаем бота
bot.infinity_polling()
