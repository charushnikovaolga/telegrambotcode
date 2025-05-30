1) Импорт библиотек
import telebotfrom telebot import types
import logging
telebot - основная библиотека для работы с Telegram API
types - содержит типы данных для работы с Telegram
logging - для логирования событий и ошибок

2) Настройка логирования
logging.basicConfig(
 format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
Настраивает формат вывода логов
Устанавливает уровень логирования INFO

3) Инициализация бота
TOKEN = '7668466529:AAGg0O8Cnjwm4UmDoRHyYsd14GXXdD4XzXs'
bot = telebot.TeleBot(TOKEN)
Создает объект бота с указанным токеном
Токен - уникальный идентификатор вашего бота

4) Обработчики команд
/start
@bot.message_handler(commands='start')def send_welcome(message):
 bot.reply_to(message, 
 "Приветствую вас! Я - бот для изучения китайских слов и выражений для всех путешественников.")
Отвечает на команду /start
Отправляет приветственное сообщение

/allblocks
@bot.message_handler(commands='allblocks')
def send_allblocks(message):
 bot.reply_to(message, "На данный момент у меня есть следующие блоки слов и выражений:\n"
 "- Приветствие\n"
 "- Числа\n"
 "- Приветствие")
Показывает список доступных блоков слов
Использует переносы строк для форматирования

/block
@bot.message_handler(commands='block')
def send_block(message):
 bot.reply_to(message, "Приветствие:\n"
 "Здравствуй - 你好 (nǐ hǎo)\n"
 "Доброе утро - 早上好 (zǎo shang hǎo)\n"
 "Добрый день - 下午好 (xià wǔ hǎo)")
Показывает слова из блока “Приветствие”
Включает русский перевод и пиньинь

/about
@bot.message_handler(commands='about')
def send_about(message):
 bot.reply_to(message, "Этот бот - проект студентов Цифровых кафедр.\n"
 "Пока он не идеальный, но призванный немного помочь вам с изучением китайского языка!")
Показывает информацию о боте

Обработчик всех остальных сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message): bot.reply_to(message, "Неизвестная команда. Введите /help для списка доступных команд.")
Обрабатывает все сообщения, которые не соответствуют другим командам
Отвечает сообщением о неизвестной команде

5) Функция запуска бота
def main():
 try: bot.polling(none_stop=True)
 except Exception as e:
 logging.error(f"Ошибка при запуске бота: {e}")

if __name__ == '__main__':
 main()
Запускает бесконечный цикл обработки сообщений
Добавляет обработку исключений
none_stop=True - бот будет работать непрерывно
