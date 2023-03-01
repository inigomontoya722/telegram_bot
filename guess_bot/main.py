import telebot
import os
from fuzzywuzzy import fuzz
import requests
from bs4 import BeautifulSoup


# Функция поиска названия аниме
def findAnime(file_path):

	url = f'https://yandex.ru/images/search?source=collections&rpt=imageview&url={file_path}'

	allNames = []

	while len(allNames) == 0:
		page = requests.get(url)

		soup = BeautifulSoup(page.text, 'html.parser')

		allNames = soup.findAll('div', class_='cbir-section cbir-section_name_tags')

	names = allNames[0].findAll('span', class_='Button2-Text')

	return(names[0].text)



# Создаем бота, пишем свой токен
bot = telebot.TeleBot('токен')

# Команда «Старт»
@bot.message_handler(commands=["start"])
def start(m, res=False):
        bot.send_message(m.chat.id, 'Привет, я Диас')
# Получение сообщений от юзера

@bot.message_handler(content_types=["text"])
def handle_text(message):
	bot.reply_to(message, findAnime(str(message.text)))    


# Запускаем бота
bot.polling(none_stop=True, interval=0)
