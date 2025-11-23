
import telebot

BOT_TOKEN = "8267938733:AAGhhKLDNx12UCNyGL6cn0I0eSQr_AINCs0"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        """  
جميع التفاصيل اللي محتاجها داخل الجروب  
لا تنسي متابعة الجروب الرسمي  
ولا تتردد في التواصل مع الدعم عند وجود استفسار  

https://t.me/+wnLokF1pLzs3ZmI0

نتمني لكم التوفيق والنجاح الدائم 🌟
        """
    )

bot.polling(none_stop=True)
