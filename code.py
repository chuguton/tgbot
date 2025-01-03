from http.client import responses
import telebot

from telebot import types
import random
from telebot.apihelper import send_message

bot = telebot.TeleBot('...')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! Я бот, чья задача - развеселить тебя. Уверен, накопленный материал захлестнет юмором.')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id,
                     'Слегка запутался? Давай разберемся! Бот устроен достаточно примитивно, все доступные команды приведены ниже:\n\n /start - начальное приветствие\n /help - предоставляет названия всех встроенных команд\n /anecdote - командра для написания анекдота')

@bot.message_handler(commands=['anecdote'])
def send_random_anecdote(message):
    anecdote = [...]

anecdote = random.choice(anecdote)
    bot.send_message(message.chat.id, text=anecdote)

@bot.message_handler()
def info(message):
    bot.send_message(message.chat.id,
                     'Слегка запутался? Давай разберемся! Бот устроен достаточно примитивно, все доступные команды приведены ниже:\n\n /start - начальное приветствие\n /help - предоставляет названия всех встроенных команд\n /anecdote - командра для написания анекдота')

bot.polling(none_stop=True)
