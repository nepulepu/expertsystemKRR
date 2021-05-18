import telebot
import os
import time
from dotenv import load_dotenv
from datetime import datetime
from telebot import types
from telebot.apihelper import edit_message_reply_markup

load_dotenv()
TOKEN=os.getenv("TOKEN")
print(TOKEN)
bot=telebot.TeleBot(TOKEN)

def getTime():
    now= datetime.now()
    currenttime=now.strftime("%H")
    if(int(currenttime)<6 or int(currenttime)>=15):
        return "Evening"
    elif(int(currenttime)>=6 and int(currenttime)<12):
        return "Morning"
    elif(int(currenttime)>=12 and int(currenttime)<15):
        return "Afternoon"

@bot.message_handler(commands=['HelloDr'])
def greet(message):
    name=message.from_user.first_name
    bot.send_message(message.chat.id, "Good "+getTime()+" " + name)
    def ready():
        reply_board= types.ReplyKeyboardMarkup()
        itemYes=types.KeyboardButton("/Yes")
        itemNo=types.KeyboardButton("/No")
        reply_board.add(itemYes,itemNo)
        bot.send_message(message.chat.id, "Are you ready to start the class?",reply_markup=reply_board)
        @bot.message_handler(commands=['Yes'])
        def letslearn(message):
            reply_board=types.ReplyKeyboardRemove(selective=False)
            bot.send_message(message.chat.id,"lesgoo",reply_markup=reply_board)
            print("lesgo")
        @bot.message_handler(commands=['No'])
        def notyet(message):
            bot.send_message(message.chat.id,"I will wait for you")
            ready()
    ready()

while True:
    try:
        bot.polling(none_stop=False)
    except Exception:
        print('crash')
        time.sleep(1)