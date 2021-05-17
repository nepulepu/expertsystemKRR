import telebot
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN=os.getenv("TOKEN")
bot=telebot.Telebot(TOKEN)

@bot.message_handler(commands=['GoodDayDr'])
def greet(message):
    bot(message, "Good Day Student\nAre you ready to start the class?")

bot.polling()