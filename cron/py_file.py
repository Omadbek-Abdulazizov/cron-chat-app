import telebot
from main_app.models import Habarlar
from datetime import datetime
from main_app.utils import send_message


bot = telebot.TeleBot(token='6858387672:AAHIm8VGQ2hGt-DGkFk9vXCRJAbwfLjbJV8')

def p():
    now = datetime.now()
    try:
        habarlar = Habarlar.objects.filter(vaqt__year=now.year, vaqt__month=now.month, vaqt__day=now.day, vaqt__hour=now.hour, vaqt__minute=now.minute)
        if habarlar:
            for habar in habarlar:
                for hodim in habar.hodim.all():
                    send_message(chat_id=hodim.telegram_id, text=habar.text)
    except Habarlar.DoesNotExist:
        pass