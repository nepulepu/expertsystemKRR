from logging import currentframe
import telebot
import os
import time
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
TOKEN=os.getenv("TOKEN2")
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
    bot.send_message(message.chat.id, "Good "+getTime()+" "+name+",\nAre you ready to start the class?")

while True:
    try:
        bot.polling(none_stop=False)
    except Exception:
        print('crash')
        time.sleep(1)