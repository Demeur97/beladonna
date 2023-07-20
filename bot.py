import schedule
import telebot
import config
from telebot import types
import kz
import time


bot = telebot.TeleBot(config.TOKEN)

# приветствие при входе
@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    bot.reply_to(message, text='Приветствую в клане {0.first_name}!\nТребования клана: 600 камней в день и активное участие в жизни клана. Просьба об отсутствии в игре предупреждать заранее.', parse_mode="html")
    
# меню start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Список команд бота', url='https://telegra.ph/Spisok-komand-bota-klana-Beladonna-07-18')
 
    markup.add(btn1)
 
    bot.send_message(message.chat.id, 'Привет, {0.first_name}! Чтобы узнать команды кликни по кнопке ниже'.format(message.from_user), reply_markup = markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "!правила":
        bot.send_message(message.chat.id, '⚔Раздел находится в разработке')
        bot.delete_message(message.chat.id,message.message_id - 0)       

#полезные ссылки (нужно найти ссылки)
    elif message.text == "!ссылки1":
        bot.send_message(message.chat.id, '[Английская база знаний AoM](https://www.aomdb.com/)', parse_mode='Markdown')     
        bot.delete_message(message.chat.id,message.message_id - 0)
 
#команды (всё сделано, нужно только отредачить файл)
    elif message.text == "/commands" or message.text == "!команды":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Список команд бота', url='https://telegra.ph/Spisok-komand-bota-klana-Beladonna-07-18')
        markup.add(btn1)
        bot.send_message(message.chat.id, '{0.first_name}, чтобы узнать все команды нажми на кнопку ниже'.format(message.from_user), reply_markup = markup)  
        bot.delete_message(message.chat.id,message.message_id - 0) 
        

#рейды (заполнить кнопки картинками)
    elif message.text == "/raids" or message.text == "!рейды":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Обычные рейды', callback_data="raid")
        btn2 = types.InlineKeyboardButton(text='Огненные врата', callback_data="fire")
        btn3 = types.InlineKeyboardButton(text='Небесные врата', callback_data="sky")
        btn4 = types.InlineKeyboardButton(text='Врата рока', callback_data="rok")

        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Выберите вариант ниже'.format(message.from_user), reply_markup = markup)  
        bot.delete_message(message.chat.id,message.message_id - 0)    
        

# клановыезадания (сделать вывод текста в вылезающем окне)

    elif message.text == '/clantasks' or message.text == '!задания':
        markup = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton(text = 'Понедельник', callback_data="pn")
        item2 = types.InlineKeyboardButton(text = 'Вторник', callback_data="vt")
        item3 = types.InlineKeyboardButton(text = 'Среда', callback_data="sr")
        item4 = types.InlineKeyboardButton(text = 'Четверг', callback_data="cht")
        item5 = types.InlineKeyboardButton(text = 'Пятница', callback_data="pt")
        item6 = types.InlineKeyboardButton(text = 'Суббота', callback_data="sb")
        item7 = types.InlineKeyboardButton(text = 'Воскресение', callback_data="vs")

        markup.add(item1,item2,item3,item4,item5,item6,item7)
        bot.send_message(message.chat.id, 'Выберите день недели:', reply_markup = markup)
        bot.delete_message(message.chat.id,message.message_id - 0) 

#События
    elif message.text == "/events" or message.text == "!события":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Все события', url='https://telegra.ph/Vse-sobytiya-07-19')
        btn2 = types.InlineKeyboardButton(text='Бальтазар', url='https://telegra.ph/Baltazar-07-19-2')
        btn3 = types.InlineKeyboardButton(text='Сандариэль', url='https://telegra.ph/Sandariehl-07-19')
        btn4 = types.InlineKeyboardButton(text='Гоблушка', url='https://telegra.ph/Goblushka-07-19')

        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Выберите вариант ниже:'.format(message.from_user), reply_markup = markup)  
        bot.delete_message(message.chat.id,message.message_id - 0)    
  
#Полезные ссылки
    elif message.text == "/url" or message.text == "!ссылки":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Age of Magic Wiki(eng)', url='https://ageofmagicgame.fandom.com/wiki/Age_of_Magic_Wiki')
        btn2 = types.InlineKeyboardButton(text='Age of Magic Wiki(rus)', url='https://ageofmagic.ru/')

        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, '⚔Список ссылок⚔'.format(message.from_user), reply_markup = markup)  
        bot.delete_message(message.chat.id,message.message_id - 0) 
#Группы в telegram
    elif message.text == "/groups" or message.text == "!группы":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Группа с гайдами', url='https://t.me/AoM_Jr')
        btn2 = types.InlineKeyboardButton(text='Age Of Magic – Новости', url='https://t.me/age_of_magic_news')
        btn3 = types.InlineKeyboardButton(text='Фан-чат Age of Magic', url='https://t.me/aom_fan_ru')
        btn4 = types.InlineKeyboardButton(text='AomSOCIAL', url='https://t.me/aomSocial')
        btn5 = types.InlineKeyboardButton(text='Группа для помощи по игре', url='https://t.me/age_of_magic')
        btn6 = types.InlineKeyboardButton(text='Чат для новичков', url='https://t.me/aom697')

        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id, '⚔Список каналов и чатов⚔'.format(message.from_user), reply_markup = markup)  
        bot.delete_message(message.chat.id,message.message_id - 0) 

#Команды для офицеров
    elif message.text == "/admin" or message.text == "!админ":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Команды для офицеров/ветеранов', url='https://telegra.ph/Spisok-komand-bota-klana-Beladonna-07-19')
        markup.add(btn1)
        bot.send_message(message.chat.id, '{0.first_name}, чтобы узнать все команды нажми на кнопку ниже'.format(message.from_user), reply_markup = markup)  
        bot.delete_message(message.chat.id,message.message_id - 0) 
        
    elif message.text == '!рейд4':
        photo = open ('p.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption = "<strong>⚔ РЕЙД ОТКРЫТ ⚔</strong>\nВсе оперативно заходим в рейд и отбиваем энергию по максимуму!", parse_mode="html")
        bot.delete_message(message.chat.id,message.message_id - 0) 
        
            
#информация по клановым за пн-вс (В рейдах не заполнены 1-2 рейды)

@bot.callback_query_handler(func=lambda c:True)
def callback_inline(c):
    cid = c.message.chat.id
    keyboard = types.InlineKeyboardMarkup()
    if c.data == "pn":
        bot.send_message(cid, text = kz.pn, reply_markup=keyboard, parse_mode="html")
    elif c.data == "vt":
        bot.send_message(cid, text = kz.vt, reply_markup=keyboard, parse_mode="html")
    elif c.data == "sr":
        bot.send_message(cid, text = kz.sr, reply_markup=keyboard, parse_mode="html")
    elif c.data == "cht":
        bot.send_message(cid, text = kz.cht, reply_markup=keyboard, parse_mode="html")
    elif c.data == "pt":
        bot.send_message(cid, text = kz.pt, reply_markup=keyboard, parse_mode="html")
    elif c.data == "sb":
        bot.send_message(cid, text = kz.sb, reply_markup=keyboard, parse_mode="html")
    elif c.data == "vs":
        bot.send_message(cid, text = kz.vs, reply_markup=keyboard, parse_mode="html")    
    elif c.data == "raid":
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="Портал в неизведанное I", url='https://telegra.ph/Shema-rejda-I-Portal-v-neizvedannoe-07-19')
        but_2 = types.InlineKeyboardButton(text="Портал в неизведанное II", url='https://telegra.ph/Shema-rejda-II-Portal-v-neizvedannoe-07-19')
        but_3 = types.InlineKeyboardButton(text="Портал в неизведанное III", url='https://telegra.ph/Shema-rejda-III-Portal-v-neizvedannoe-07-19')
        but_4 = types.InlineKeyboardButton(text="Портал в неизведанное IV", url='https://telegra.ph/Shema-rejda-IV-Portal-v-neizvedannoe-07-19')
        but_5 = types.InlineKeyboardButton(text="Портал в неизведанное V", url='https://telegra.ph/Shema-rejda-V-Portal-v-neizvedannoe-07-19')
        but_6 = types.InlineKeyboardButton(text="Назад", callback_data="raids")
        key.add(but_1, but_2, but_3, but_4, but_5, but_6)
        bot.edit_message_text('Выберите схему для рейда', c.message.chat.id, c.message.message_id, reply_markup=key)

    elif c.data == "fire":
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="Огненные врата I", url='https://telegra.ph/Ognennye-vrata-I-07-19')
        but_2 = types.InlineKeyboardButton(text="Огненные врата II", url='https://telegra.ph/Ognennye-vrata-II-07-19')
        but_3 = types.InlineKeyboardButton(text="Огненные врата III", url='https://telegra.ph/Ognennye-vrata-III-07-19')
        but_4 = types.InlineKeyboardButton(text="Огненные врата IV", url='https://telegra.ph/Ognennye-vrata-IV-07-19')
        but_5 = types.InlineKeyboardButton(text="Назад", callback_data="raids")
        key.add(but_1, but_2, but_3, but_4, but_5)
        bot.edit_message_text('Выберите схему для рейда', c.message.chat.id, c.message.message_id, reply_markup=key)
    elif c.data == "sky":
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="Небесные врата I", url='https://telegra.ph/Nebesnye-vrata-I-07-19')
        but_2 = types.InlineKeyboardButton(text="Небесные врата II", url='https://telegra.ph/Nebesnye-vrata-II-07-19')
        but_3 = types.InlineKeyboardButton(text="Небесные врата III", url='https://telegra.ph/Nebesnye-vrata-III-07-19')
        but_4 = types.InlineKeyboardButton(text="Небесные врата IV", url='https://telegra.ph/Nebesnye-vrata-IV-07-19')
        but_5 = types.InlineKeyboardButton(text="Назад", callback_data="raids")
        key.add(but_1, but_2, but_3, but_4, but_5)
        bot.edit_message_text('Выберите схему для рейда', c.message.chat.id, c.message.message_id, reply_markup=key)
    elif c.data == "rok":
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="Врата рока I", url='https://telegra.ph/Vrata-roka-I-07-19')
        but_2 = types.InlineKeyboardButton(text="Врата рока II", url='https://telegra.ph/Vrata-roka-II-07-19')
        but_3 = types.InlineKeyboardButton(text="Врата рока III", url='https://telegra.ph/Vrata-roka-III-07-19')
        but_4 = types.InlineKeyboardButton(text="Врата рока IV", url='https://telegra.ph/Vrata-roka-IV-07-19')
        but_5 = types.InlineKeyboardButton(text="Назад", callback_data="raids")
        key.add(but_1, but_2, but_3, but_4, but_5)
        bot.edit_message_text('Выберите схему для рейда', c.message.chat.id, c.message.message_id, reply_markup=key)
        
    elif c.data == "raids": 
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Обычные рейды', callback_data="raid")
        btn2 = types.InlineKeyboardButton(text='Огненные врата', callback_data="fire")
        btn3 = types.InlineKeyboardButton(text='Небесные врата', callback_data="sky")
        btn4 = types.InlineKeyboardButton(text='Врата рока', callback_data="rok")

        markup.add(btn1, btn2, btn3, btn4)
        bot.edit_message_text('Выберите вариант ниже', c.message.chat.id, c.message.message_id, reply_markup = markup)  
     

#зазывалка (на будущее)
    elif message.text == "!зазывалка":
        nick = message.from_user.username
        bot.send_message(message.chat.id, f"@{nick}")
        
        
     
        
chat_id = '897173839'
def job():
    message = 'Сообщение, которое нужно отправить в 21:00'
    bot.send_message(chat_id=chat_id, text=message)
schedule.every().hour.at(":36").do(job)
        
while True:
    try:
        bot.polling(none_stop=True, interval=0) 
    except Exception as e:
        time.sleep(2)
