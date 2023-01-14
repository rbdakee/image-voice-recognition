import telebot
from photo import photo_text
from audio import audio_text
import requests


token='5308911565:AAGHFO5zAWZJMh5XdOGR5zvTXx5kgrbLQDQ'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):

    bot.send_message(message.chat.id, '''Привет! Этот бот умеет конвертировать фото и аудио в тексты
Выбери, что хочешь конвертировать:
/audio - аудио
/photo - фото''')

@bot.message_handler(content_types='text')
def bot_body(message):
    if message.text == '/audio':
        bot.send_message(message.chat.id, "Отправьте аудиосообщение")
    elif message.text == '/photo':
        bot.send_message(message.chat.id, "Отправьте фотографию")

@bot.message_handler(content_types=['photo'])
def photo(message):   
    fileID = message.photo[-1].file_id   
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("photo/image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)  
    bot.send_message(message.chat.id, f"{photo_text()}")

@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    file_info = bot.get_file(message.voice.file_id)
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))

    with open('telega.ogg','wb') as f:
        f.write(file.content)

    bot.send_message(message.chat.id, audio_text())


bot.polling(none_stop=True, interval=0)

