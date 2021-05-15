import os
import telebot
from config import BOT_TOKEN
from text import WELCOME, VRTXT

worker = config.BOT_TOKEN
bot = telebot.TeleBot(worker)


@bot.message_handler(commands=["start"])
def start(message):
        welcomet = WELCOME,
        bot.reply_to(message, welcomet)  
        
 
  
@bot.message_handler(commands=["vrtx"])
def vrtx(message):
        vrtxt = VRTXT,
        bot.reply_to(message, vrtxt)  
       
         
bot.polling()
