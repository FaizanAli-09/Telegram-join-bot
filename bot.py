import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.BOT_TOKEN)

REQUIRED_CHANNELS = config.REQUIRED_CHANNELS

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    not_joined = []

    for channel in REQUIRED_CHANNELS:
        try:
            member = bot.get_chat_member(channel, user_id)
            if member.status in ['left', 'kicked']:
                not_joined.append(channel)
        except:
            not_joined.append(channel)

    if not_joined:
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("📢 Join All Channels", url="https://t.me/Forex_Gold_Signals_PR")
        markup.add(btn)
        bot.send_message(
            user_id,
            "🚫 Pehlay sabhi channels join karo, phir /start dobara likho:",
            reply_markup=markup
        )
    else:
        bot.send_message(user_id, "✅ Aap ne sabhi channels join kar liye. Welcome!")

bot.infinity_polling()
