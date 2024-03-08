import asyncio
import logging
import threading

from profanityfilter import ProfanityFilter
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

import config
from modules.strdistance import StrDistance
from modules.translator import TranslateText

log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
config_file = 'debug.log'
logging.basicConfig(
    filename=config_file,
    level=logging.DEBUG, 
    force=True, 
    encoding='utf-8',
    format=log_format
)


class Filter:
    def __init__(self) -> None:
        self.pf = ProfanityFilter()
        
    @staticmethod
    def check_dist_bad(text):
        dist = StrDistance(text)
        result: float = dist.compute()
        print("[DEBUG]", result)
        return result >= config.profanity_percent
        
    def bad_text(self, text) -> bool:
        translated_text = TranslateText(text).translate()
        custom_words_check = self.check_dist_bad(text)
               
        # For custom words
        if custom_words_check: return custom_words_check
        
        # For english translation
        return self.pf.has_bad_word(text=translated_text)
         
                
bot = AsyncTeleBot(config.TOKEN, parse_mode=config.markup)
filter = Filter()

@bot.message_handler(commands=['start'])  # /start command
async def start(msg: Message):
    await bot.reply_to(msg, config.default_start_message)

@bot.message_handler(commands=['help', 'support', 'admin'])
async def support(msg: Message):
    await bot.reply_to(msg, config.help_message)

@bot.message_handler(func=lambda message: not message.text.startswith('/'))
async def check_message(msg: Message):
    if not msg.text: 
        return
    
    msg_id = msg.message_id
    group_name = msg.chat.first_name
        
    result = filter.bad_text(msg.text.lower())
    if result:
        try:
            #await bot.reply_to(msg, 'Found profinity word!')  # Use this if you want to warn users
            await bot.delete_message(msg.chat.id, msg_id)
            
        except:
            print(f'Cannot delete message ({msg_id}) in group {group_name}')


if __name__ == "__main__":
    t = threading.Thread(target=
        asyncio.run, args=(bot.polling(restart_on_change=True),)           
    )
    print("Starting bot polling...")
    logging.info("Starting bot polling...")
    t.start()
    print("Bot polling started")
    logging.info("Bot polling started")
    t.join()