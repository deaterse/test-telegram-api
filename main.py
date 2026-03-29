from bot import *
from config import TOKEN

bot = Bot(TOKEN)

@bot.message('Hello')
def hello(message):
    bot.send_message(message['chat']['id'], 'Hello World.')

@bot.message('/start')
def start_command(message):
    bot.send_message(message['chat']['id'], 'U wrote start command.')

bot.start()