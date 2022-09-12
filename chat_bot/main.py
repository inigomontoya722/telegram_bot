import telebot
import os
from fuzzywuzzy import fuzz
import requests
from bs4 import BeautifulSoup



# Создаем бота, пишем свой токен
bot = telebot.TeleBot('5415338680:AAFlS_4HKhq5P5XxlWvcgvMmOtoJ6nYIrI0')
# Загружаем список фраз и ответов в массив
mas=[]
if os.path.exists('data/boltun.txt'):
    f=open('data/boltun.txt', 'r', encoding='UTF-8')
    for x in f:
        if(len(x.strip()) > 2):
            mas.append(x.strip().lower())
    f.close()
# С помощью fuzzywuzzy вычисляем наиболее похожую фразу и выдаем в качестве ответа следующий элемент списка
def answer(text):
    try:
        text=text.lower().strip()
        if os.path.exists('data/boltun.txt'):
            a = 0
            n = 0
            nn = 0
            for q in mas:
                if('u: ' in q):
                    # С помощью fuzzywuzzy получаем, насколько похожи две строки
                    aa=(fuzz.token_sort_ratio(q.replace('u: ',''), text))
                    if(aa > a and aa!= a):
                        a = aa
                        nn = n
                n = n + 1
            s = mas[nn + 1]
            return s
        else:
            return 'Ошибка'
    except:
        return 'Ошибка'
# Команда «Старт»
@bot.message_handler(commands=["start"])
def start(m, res=False):
        bot.send_message(m.chat.id, 'Привет, я Диас')
# Получение сообщений от юзера

@bot.message_handler(content_types=["text"])
def handle_text(message):
	bot.reply_to(message, answer(str(message.text)))    


# Запускаем бота
bot.polling(none_stop=True, interval=0)
