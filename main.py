import telebot
import openai


openai.api_key = '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' #ключ OpenAi


bot = telebot.TeleBot('6893084576:AAEdVNS6m86KczspJxPWsWOwNDKHMft6TmA') #ключ телеграм бота 



@bot.message_handler(commands=['start']) #если на вход подается /start, то выполнить функцию 
def handle_start(message): #фунция обработки /start 
    bot.send_message(message.chat.id, "Привет! Я твой телеграм-бот. Отправь мне сообщение, и я постараюсь ответить.")#приветствие пользователя 


@bot.message_handler(func=lambda message: True)
def handle_message(message):#главная функция, которая принимает сообещния пользователья 
   
    user_input = message.text

    
    response = openai.Completion.create(
        engine="text-davinci-003",  #версия ии 
        prompt=user_input, 
        max_tokens=500 #макс символов в ответе бота 
    )

    
    bot_response = response.choices[0].text.strip()#перевот ответа в текст 

    
    bot.send_message(message.chat.id, bot_response)#ответ на вопрос пользователя 


bot.polling(none_stop=True)#команда, которая не дает боту остановится 

