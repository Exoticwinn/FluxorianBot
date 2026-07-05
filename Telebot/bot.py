import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

class Book:
    def __init__(self, author, name, genre):
        self.author = author
        self.name = name
        self.genre = genre

    def read(self):
        return "Начинаем читать!"

    def stop(self):
        return "Закрываем книгу!"

    def info(self):
        return f"Автор: {self.author}, Название: {self.name}, Жанр: {self.genre}"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот. Напиши мне что-нибудь!")

@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, "Бот для личного использования.")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
    Доступные команды:
    /start - Начать общение
    /info - Информация о боте
    /help - Справка по командам
    /book - Информация о книгах
    """
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['book'])
def send_book_info(message):
    my_book = Book("Достоевский", "Преступление и наказание", "Роман")
    bot.send_message(message.chat.id, f"Книга:\n{my_book.info()}")
    bot.send_message(message.chat.id, my_book.read())
    bot.send_message(message.chat.id, my_book.stop())

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
