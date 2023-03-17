import telebot
from telebot import types

bot = telebot.TeleBot('5883186105:AAF2AKT-UnBptrJ5fx4IzNPoaXmt_HKlxB4')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Как стать модератором на канале создателя?')
        btn2 = types.KeyboardButton('Telegram канал создателя')
        btn3 = types.KeyboardButton('Кто создатель бота?')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) #ответ бота


    elif message.text == 'Как стать модератором на канале создателя?':
        bot.send_message(message.from_user.id, 'Решили стать модератором всё здесь \n \nПолный текст можно прочитать по ' + '[ссылке](https://telegra.ph/Kak-podat-zayavku-na-poluchenie-moderatora-ili-drugoj-dolzhnosti-03-15)', parse_mode='Markdown')

    elif message.text == 'Telegram канал создателя':
        bot.send_message(message.from_user.id, 'Перейти на телеграм канал можно по ' + '[ссылке](https://t.me/HigWag)', parse_mode='Markdown')

    elif message.text == 'Кто создатель бота?':
        bot.send_message(message.from_user.id, 'Создателем является MalahitRumRus ' + '[ссылке](https://t.me/MalahitRumRus)', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть