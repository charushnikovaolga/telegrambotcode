import telebot
from telebot import types
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = '7668466529:AAGg0O8Cnjwm4UmDoRHyYsd14GXXdD4XzXs'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 
                 "Приветствую вас! Я - бот для изучения китайских слов и выражений для всех путешественников.")

@bot.message_handler(commands=['allblocks'])
def send_allblocks(message):
    bot.reply_to(message, "На данный момент у меня есть следующие блоки слов и выражений:\n"
                         "- Приветствие\n")

@bot.message_handler(commands=['block'])
def send_block(message):
    bot.reply_to(message, "Приветствие:\n"
                         "Здравствуй - 你好 (ни хао)\n"
                         "Доброе утро - 早上好 (дзао шанг хао)\n"
                         "Добрый день - 下午好 (ся ву хао)")

@bot.message_handler(commands=['about'])
def send_about(message):
    bot.reply_to(message, "Этот бот - проект студентов Цифровых кафедр.\n"
                         "Пока он не идеальный, но призван немного помочь вам с изучением китайского языка!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Неизвестная команда. Введите /start для списка доступных команд.")

def main():
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logging.error(f"Ошибка при запуске бота: {e}")

if __name__ == '__main__':
    main()
