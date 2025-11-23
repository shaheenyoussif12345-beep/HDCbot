import os
import telebot

# بنجيب التوكن من Environment Variables
BOT_TOKEN = os.environ.get("BOT_TOKEN")

if not BOT_TOKEN:
    raise Exception("❌ مفيش BOT_TOKEN موجود في Environment Variables")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(
        message.chat.id,
        """✨ أهلاً بيك ✨

جميع التفاصيل اللي محتاجها موجودة داخل الجروب.

لا تنسى متابعة الجروب الرسمي ولا تتردد في التواصل مع الدعم لو عندك أي استفسار.

🔗 رابط الجروب:
https://t.me/+wnLokF1pLzs3ZmI0

نتمنى لكم التوفيق والنجاح الدائم 🌟
"""
    )

bot.polling(none_stop=True)
