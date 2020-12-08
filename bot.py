import sys
import telebot
from telebot import types
from config import Config

cfg = Config()
if cfg.bot_token == "null" or cfg.bot_token is None:
    print("Bot token is not found in config.yml")
    sys.exit()
bot = telebot.TeleBot(cfg.bot_token)

def isStringA(text):
    allowed_symbols = ['a', 'а', '!', '.', '?', ',']
    for letter in text:
        if letter not in allowed_symbols:
            return False
    return True

@bot.message_handler(func=lambda message: message.text is not None and isStringA(message.text.lower()))
def send_a_gif(message):
    a_gif = 'CgACAgIAAxkBAAMEX8-j-W7aYYu6cCROigHjTibvhW4AAiwKAAIsiClILv-rgL5Bb1oeBA'
    bot.send_animation(message.chat.id, a_gif, reply_to_message_id=message.message_id)

if __name__ == '__main__':
    print("Application has been started.")
    bot.polling(none_stop=True, interval=0)