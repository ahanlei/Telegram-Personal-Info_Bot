import os
import telebot

vrtx_token = '1765303617:AAGKA-wy3mCgz7k9GAYgXsl-IpR3y3fptvI'
vrtx = telebot.TeleBot(vrtx_token)


'''----------------------------------------------------------------------'''
@vrtx.message_handler(commands=["start"])
def start(message):
        welcomet = """
            ℍ𝕚 & \n
нєяє αяє αℓℓ тнє ℓιηкѕ тσ му ωσяк
        
𝓖𝖗𝖔𝖚𝖕 --:
        🎻ʍʊֆɨƈǟʟ ƈɦǟttɨռɢ🎻
         @vrtxmusic
         
𝕮𝖍𝖆𝖓𝖓𝖊𝖑 --:
        🌾|••Wǟʟʟɦʊɮ-ʋʀȶӼ••|🍁
         @vrtxwalls
         
        ••🔷| Vɾƚx--W๏гкร |🔶••
         @vrtxwork 

𝕭𝖔𝖙𝖘 ---:         
        🔴YouTube Downloader🎧📥
         @vrtxytbot
        
        🟢Spotify Downloader🎤📥
         @vrtxspotify_bot"""
        vrtx.reply_to(message, welcomet)  
        
 
'''----------------------------------------------------------------------'''     
@vrtx.message_handler(commands=["vrtx"])
def vrtx(message):
        welcomet = """
            ℍ𝕚 & \n
нєяє αяє αℓℓ тнє ℓιηкѕ тσ му ωσяк
        
𝓖𝖗𝖔𝖚𝖕 --:
        🎻ʍʊֆɨƈǟʟ ƈɦǟttɨռɢ🎻
         @vrtxmusic
         
𝕮𝖍𝖆𝖓𝖓𝖊𝖑 --:
        🌾|••Wǟʟʟɦʊɮ-ʋʀȶӼ••|🍁
         @vrtxwalls
         
        ••🔷| Vɾƚx--W๏гкร |🔶••
         @vrtxwork 

𝕭𝖔𝖙𝖘 ---:         
        🔴YouTube Downloader🎧📥
         @vrtxytbot
        
        🟢Spotify Downloader🎤📥
         @vrtxspotify_bot"""
        vrtx.reply_to(message, welcomet)  
        
        
'''----------------------------------------------------------------------'''  
@vrtx.message_handler(commands=["owner"])
def owner(message):
        met = "@mastermindvrtx A.K.A 🃏 ʍǟֆȶɛʀʍɨռɖ.ʋʀȶӼ™ "
        vrtx.reply_to(message, met)
        
        
'''----------------------------------------------------------------------'''

 
vrtx.polling()
