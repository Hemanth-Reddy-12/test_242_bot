import os
import telebot
from dotenv import load_dotenv


load_dotenv()
api_token = os.getenv('API_TOKEN')

bot = telebot.TeleBot(api_token)



@bot.message_handler(commands=['start'])
def start_welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Hello")


bot.infinity_polling()
