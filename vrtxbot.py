import telebot
from text import WELCOME, VRTXT

BOT_TOKEN = "1765303617:AAFURgnhnxaVOhdMxiN41rCFG4gVO38q5XE"
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
        welcomet = WELCOME,
        bot.reply_to(message, welcomet)  
        
 
  
@bot.message_handler(commands=["vrtx"])
def vrtx(message):
        vrtxt = VRTXT,
        bot.reply_to(message, vrtxt)  
       
         
bot.polling()
