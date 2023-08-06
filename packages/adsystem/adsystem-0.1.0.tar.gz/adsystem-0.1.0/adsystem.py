from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json 
from aiogram import types
from copy import deepcopy 

interests_keyboard = InlineKeyboardMarkup(row_width=4)
ik1 = InlineKeyboardButton("Юмор & Отдых", callback_data="adsystemparameters_2_1")
ik2 = InlineKeyboardButton("Новости", callback_data="adsystemparameters_2_2")
ik3 = InlineKeyboardButton("IT-сфера", callback_data="adsystemparameters_2_3")
ik4 = InlineKeyboardButton("Мода & Красота", callback_data="adsystemparameters_2_4")
ik5 = InlineKeyboardButton("Еда & Кулинария", callback_data="adsystemparameters_2_5")
ik6 = InlineKeyboardButton("Бизнес & Финансы", callback_data="adsystemparameters_2_6")
ik7 = InlineKeyboardButton("Политика", callback_data="adsystemparameters_2_7")
ik8 = InlineKeyboardButton("Образование", callback_data="adsystemparameters_2_8")
ik9 = InlineKeyboardButton("Криптовалюты", callback_data="adsystemparameters_2_9")
ik10 = InlineKeyboardButton("Арт & Дизайн", callback_data="adsystemparameters_2_10")
ik11 = InlineKeyboardButton("Спорт", callback_data="adsystemparameters_2_11")
ik12 = InlineKeyboardButton("Путешествия", callback_data="adsystemparameters_2_12")
ik13 = InlineKeyboardButton("Видеоигры", callback_data="adsystemparameters_2_13")
ik14 = InlineKeyboardButton("Ставки & Азарт", callback_data="adsystemparameters_2_14")

nx = InlineKeyboardButton("Далее >", callback_data="adsystemparameters_2_next")
interests_keyboard.add(ik1, ik2)
interests_keyboard.add(ik3, ik4)
interests_keyboard.add(ik5, ik6)
interests_keyboard.add(ik7, ik8)
interests_keyboard.add(ik9, ik10)
interests_keyboard.add(ik11, ik12)
interests_keyboard.add(ik13, ik14)
interests_keyboard.add(nx)

genders_keyboard = InlineKeyboardMarkup()
genders_keyboard.add(InlineKeyboardButton("Мужчина", callback_data="adsystemparameters_0_-1"))
genders_keyboard.add(InlineKeyboardButton("Женщина", callback_data="adsystemparameters_0_1"))

ages_keyboard = InlineKeyboardMarkup()
ages_keyboard.add(InlineKeyboardButton(" <12 ", callback_data="adsystemparameters_1_1"), \
            InlineKeyboardButton(" 12-18 ", callback_data="adsystemparameters_1_2"), \
                InlineKeyboardButton(" 18-21 ", callback_data="adsystemparameters_1_3") )
ages_keyboard.add(InlineKeyboardButton(" 21-25 ", callback_data="adsystemparameters_1_4"), \
            InlineKeyboardButton(" 25-30 ", callback_data="adsystemparameters_1_5"), \
                InlineKeyboardButton(" 30-36 ", callback_data="adsystemparameters_1_6"))
ages_keyboard.add(InlineKeyboardButton(" 36-42 ", callback_data="adsystemparameters_1_7"), \
            InlineKeyboardButton(" 42-50 ", callback_data="adsystemparameters_1_8"), \
                InlineKeyboardButton(" 50-60 ", callback_data="adsystemparameters_1_9"))
ages_keyboard.add(InlineKeyboardButton(" >60 ", callback_data="adsystemparameters_1_10"))

try_again_keyboard = InlineKeyboardMarkup()
try_again_keyboard.add(InlineKeyboardButton("Попробовать ещё раз", callback_data="adsystemparameters_5"))

# temporary data storage 
class Storage():
    print("[ OK ] AdSystem connected successfully.")
    adsystem_host = 1089311758      # AdSystem id in Telegram
    interests = {}
    buttons = {}
    state = {}
    bot = None 
    me = None 

# обработка сообщений пользователя 
class MessageToAdSystem(BoundFilter):
    async def check(self, message: types.Message):    
        bot = Storage.bot 
            
        survey = {
            0: "🆕 Теперь контент будет подбираться специально для Вас! \nДля этого, пожалуйста, ответьте на несколько вопросов.\n\nВы: ",
            1: "Ваш возраст:",
            2: "Чем Вы увлекаетесь?"
        }    
        keyboards = {
            0: genders_keyboard,
            1: ages_keyboard,
            2: interests_keyboard
        }   
        user = int(message.from_user.id)  # The user
        
        if user!=Storage.adsystem_host and user not in Storage.state:
            await bot.send_message(chat_id=Storage.adsystem_host, text=f"v1.message:{user}")       # request an ad for the user
            return False
        
        else:   
            if "survey" in message.text:
                data = message.text.replace("survey:", "").split(":")
                user = int(data[0])
                stage = int(data[1])

                if stage < 3:
                    await bot.send_message(chat_id=user, text=survey[stage], reply_markup=keyboards[stage])       # send question to the user
                return True 
                
            elif "ad" in message.text:
                data = json.loads(message.text.replace("ad:", "").replace("'", '"'))
                ad_text = data['ad_text']
                link = data['link']
                user = data['user']
                
                text = ad_text
                ad_keyboard = InlineKeyboardMarkup()
                ad_keyboard.add(InlineKeyboardButton("Перейти", url=link))
                
                await bot.send_message(chat_id=user, text=text, reply_markup=ad_keyboard)       # send question to the user
                
                return True 

# обработка нажатий           
class CallbackToAdSystem(BoundFilter):
    async def check(self, callback_query: types.CallbackQuery):
        bot = Storage.bot
        if callback_query.data.startswith("adsystemparameters") and int(callback_query.data.split("_")[1]) != 2 and int(callback_query.data.split("_")[1]) != 5:
            data = callback_query.data.split("_")
            
            user_id = callback_query.from_user.id
            parameter = data[1]
            value = data[2]
            
            await bot.send_message(chat_id=Storage.adsystem_host, text=f"v1.survey:{user_id}:{parameter}:{value}")
            await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            
            return True
        
        elif callback_query.data.startswith("adsystemparameters") and int(callback_query.data.split("_")[1]) == 5:  # request captcha again
            await bot.send_message(chat_id=Storage.adsystem_host, text=f"v1.survey:{callback_query.from_user.id}:3:0")
            return True 
        
        else:
            return False 
        
# подтверждение подключения бота   
class IsFromAdSystem(BoundFilter):
    async def check(self, message: types.Message ):
        if message.from_user.id == Storage.adsystem_host:
            return True 
        else:
            return False     

class AdSystemBot(BoundFilter):
    def __init__(self, state=None):
        self.state = state 
        
    async def check(self, message):
        user = message.from_user.id
        if self.state == None: return True
        elif user in Storage.state and self.state == Storage.state[user]: return True
        else: return False  
    
class IAmTheOwner(BoundFilter):
    def __init__(self, me, bot):
        Storage.me = me 
        Storage.bot = bot 
        
    async def check(self, message):
        if message.from_user.id == Storage.adsystem_host and message.text == "/adsystem": return True 
        elif message.from_user.username == Storage.me and message.text == "/adsystem": return True 
        else: return False 

async def AdSystemConnectBot(message: types.Message):
    if message.from_user.id == Storage.adsystem_host:
        await message.reply(Storage.me)
    else:
        await message.reply("✅ Бот успешно подключен к AdSystem!")

async def AdSystemMessage(message): pass

async def AdSystemCallback(callback_query: types.CallbackQuery):  
    user = callback_query.from_user.id
    if int(callback_query.data.split("_")[1]) == 1: 
        Storage.state[user] = False     # interests state
        Storage.interests[user] = {}
        buttons = [ik1, ik2, ik3, ik4, ik5, ik6, ik7, ik8, ik9, ik10, ik11, ik12, ik13, ik14, nx]
        Storage.buttons[user]=deepcopy(buttons)
        
    elif int(callback_query.data.split("_")[1]) == 5:       # get captcha again
        Storage.state[user] = True      # capcha state 
        
async def AdSystemGetInterests(callback_query: types.CallbackQuery):   
    data = callback_query.data.split("_")   # get data
    user = callback_query.from_user.id
    
    bot = Storage.bot 
    
    user_id = callback_query.from_user.id
    parameter = data[1]
    value = data[2]
                    
    # получаем данные
    interests = Storage.interests[user]
    buttons = Storage.buttons[user]
        
    if value == "next" and interests.keys():
        await bot.send_message(chat_id=Storage.adsystem_host, text=f"v1.survey:{user_id}:{parameter}:0:{list(interests.keys())}")
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        Storage.state[user] = True 
        del Storage.interests[user]
        del Storage.buttons[user]
    elif value == "next" and not interests.keys():
        await bot.answer_callback_query(callback_query_id=callback_query.id, show_alert=True, text='Выберете Ваши интересы, потом нажмите кнопку "Далее"')
    else:
        value = int(value)
        # обновляем кнопки
        if value not in interests:
            buttons[value-1].text += " ✅" 
            interests[value] = None
        else:
            buttons[value-1].text = buttons[value-1].text[:-2]
            del interests[value]
            
        # сохраняем кнопки 
        Storage.buttons[user] = buttons 
        Storage.interests[user] = interests
        
        # пересобираем клавиатуру
        new_keyboard = InlineKeyboardMarkup(row_width=4)
        new_keyboard.add(buttons[0], buttons[1])
        new_keyboard.add(buttons[2], buttons[3])
        new_keyboard.add(buttons[4], buttons[5])
        new_keyboard.add(buttons[6], buttons[7])
        new_keyboard.add(buttons[8], buttons[9])
        new_keyboard.add(buttons[10], buttons[11])
        new_keyboard.add(buttons[12], buttons[13])
        new_keyboard.add(buttons[14])
        
        await callback_query.message.edit_reply_markup(reply_markup=new_keyboard)

async def AdSystemCaptcha(message: types.Message):
    bot = Storage.bot 
    user = message.from_user.id
    
    await bot.send_message(chat_id=Storage.adsystem_host, text=f"v1.survey:{message.from_user.id}:4:{message.text}")
    
    try: del Storage.state[user]
    except KeyError: pass 
        
# отправка рекламного объявления
async def AdSystemPhoto(message: types.Message, *args):
    bot = Storage.bot 
    if "caption" in message:
        if "ad:" in message.caption:    # send ad
            image = message['photo'][0]['file_id']
            data = json.loads(message.caption.replace("ad:", "").replace("'", '"'))
            title = data['title']
            ad_text = data['ad_text']
            link = data['link']
            user = data['user']
            
            text = f"{title}\n{ad_text}"
            ad_keyboard = InlineKeyboardMarkup()
            ad_keyboard.add(InlineKeyboardButton("Перейти", url=link))
                    
            await bot.send_photo(chat_id=user, photo=image, caption=text, reply_markup=ad_keyboard)
            
        else:   # send captcha
            image = message['photo'][0]['file_id']
            data = message.caption.split("=")
            user_id = data[0]
            caption = data[1]
                
            await bot.send_photo(chat_id=user_id, photo=image, caption=caption)
            
    elif "text" in message:
        data = message.text.split(":")
        if data[1] == "end":      # success
            await bot.send_message(chat_id=data[0], text="✅ Успешно! Можете продолжать пользоваться ботом!")
        else:
            await bot.send_message(chat_id=data[0], text=data[1], reply_markup=try_again_keyboard)
            
            
### Функции для библиотеки Telebot        
            
import telebot
            
# pyTelegramBotApi
interests_keyboard_telebot = telebot.types.InlineKeyboardMarkup(row_width=4)
ik1t = telebot.types.InlineKeyboardButton("Юмор & Отдых", callback_data="adsystemparameters_2_1")
ik2t = telebot.types.InlineKeyboardButton("Новости", callback_data="adsystemparameters_2_2")
ik3t = telebot.types.InlineKeyboardButton("IT-сфера", callback_data="adsystemparameters_2_3")
ik4t = telebot.types.InlineKeyboardButton("Мода & Красота", callback_data="adsystemparameters_2_4")
ik5t = telebot.types.InlineKeyboardButton("Еда & Кулинария", callback_data="adsystemparameters_2_5")
ik6t = telebot.types.InlineKeyboardButton("Бизнес & Финансы", callback_data="adsystemparameters_2_6")
ik7t = telebot.types.InlineKeyboardButton("Политика", callback_data="adsystemparameters_2_7")
ik8t = telebot.types.InlineKeyboardButton("Образование", callback_data="adsystemparameters_2_8")
ik9t = telebot.types.InlineKeyboardButton("Криптовалюты", callback_data="adsystemparameters_2_9")
ik10t = telebot.types.InlineKeyboardButton("Арт & Дизайн", callback_data="adsystemparameters_2_10")
ik11t = telebot.types.InlineKeyboardButton("Спорт", callback_data="adsystemparameters_2_11")
ik12t = telebot.types.InlineKeyboardButton("Путешествия", callback_data="adsystemparameters_2_12")
ik13t = telebot.types.InlineKeyboardButton("Видеоигры", callback_data="adsystemparameters_2_13")
ik14t = telebot.types.InlineKeyboardButton("Ставки & Азарт", callback_data="adsystemparameters_2_14")

nxt = telebot.types.InlineKeyboardButton("Далее >", callback_data="adsystemparameters_2_next")
interests_keyboard_telebot.add(ik1t, ik2t)
interests_keyboard_telebot.add(ik3t, ik4t)
interests_keyboard_telebot.add(ik5t, ik6t)
interests_keyboard_telebot.add(ik7t, ik8t)
interests_keyboard_telebot.add(ik9t, ik10t)
interests_keyboard_telebot.add(ik11t, ik12t)
interests_keyboard_telebot.add(ik13t, ik14t)
interests_keyboard_telebot.add(nxt)

genders_keyboard_telebot = telebot.types.InlineKeyboardMarkup()
genders_keyboard_telebot.add(telebot.types.InlineKeyboardButton("Мужчина", callback_data="adsystemparameters_0_-1"))
genders_keyboard_telebot.add(telebot.types.InlineKeyboardButton("Женщина", callback_data="adsystemparameters_0_1"))

ages_keyboard_telebot = telebot.types.InlineKeyboardMarkup()
ages_keyboard_telebot.add(telebot.types.InlineKeyboardButton(" <12 ", callback_data="adsystemparameters_1_1"), \
            telebot.types.InlineKeyboardButton(" 12-18 ", callback_data="adsystemparameters_1_2"), \
                telebot.types.InlineKeyboardButton(" 18-21 ", callback_data="adsystemparameters_1_3") )
ages_keyboard_telebot.add(telebot.types.InlineKeyboardButton(" 21-25 ", callback_data="adsystemparameters_1_4"), \
            telebot.types.InlineKeyboardButton(" 25-30 ", callback_data="adsystemparameters_1_5"), \
                telebot.types.InlineKeyboardButton(" 30-36 ", callback_data="adsystemparameters_1_6"))
ages_keyboard_telebot.add(telebot.types.InlineKeyboardButton(" 36-42 ", callback_data="adsystemparameters_1_7"), \
            telebot.types.InlineKeyboardButton(" 42-50 ", callback_data="adsystemparameters_1_8"), \
                telebot.types.InlineKeyboardButton(" 50-60 ", callback_data="adsystemparameters_1_9"))
ages_keyboard_telebot.add(telebot.types.InlineKeyboardButton(" >60 ", callback_data="adsystemparameters_1_10"))

try_again_keyboard_telebot = telebot.types.InlineKeyboardMarkup()
try_again_keyboard_telebot.add(telebot.types.InlineKeyboardButton("Попробовать ещё раз", callback_data="adsystemparameters_5"))

# обработка сообщений пользователя          
def MessageToAdSystemTelebot(message: telebot.types.Message):               
    bot = Storage.bot 
    survey = {
            0: "🆕 Теперь контент будет подбираться специально для Вас! \nДля этого, пожалуйста, ответьте на несколько вопросов.\n\nВы: ",
            1: "Ваш возраст:",
            2: "Чем Вы увлекаетесь?"
    }    
    keyboards = {
        0: genders_keyboard_telebot,
        1: ages_keyboard_telebot,
        2: interests_keyboard_telebot
    }   
    
    user = int(message.from_user.id)  # The user
        
    if user!=Storage.adsystem_host and user not in Storage.state:
        bot.send_message(chat_id=Storage.adsystem_host, text=f"v1.message:{user}")       # request an ad for the user
        return False
        
    else:   
        if "survey" in message.text:
            data = message.text.replace("survey:", "").split(":")
            user = int(data[0])
            stage = int(data[1])

            if stage < 3:
                bot.send_message(chat_id=user, text=survey[stage], reply_markup=keyboards[stage])       # send question to the user
            return True 
                
        elif "ad" in message.text:
            data = json.loads(message.text.replace("ad:", "").replace("'", '"'))
            ad_text = data['ad_text']
            link = data['link']
            user = data['user']
                
            text = ad_text
            ad_keyboard = telebot.types.InlineKeyboardMarkup()
            ad_keyboard.add(telebot.types.InlineKeyboardButton("Перейти", url=link))
                
            bot.send_message(chat_id=user, text=text, reply_markup=ad_keyboard)       # send question to the user
                
            return True 

# обработка нажатий        
def CallbackToAdSystemTelebot(callback_query: telebot.types.CallbackQuery):
    bot = Storage.bot 
    
    if callback_query.data.startswith("adsystemparameters") and int(callback_query.data.split("_")[1]) != 2 and int(callback_query.data.split("_")[1]) != 5:
        data = callback_query.data.split("_")
            
        user_id = callback_query.from_user.id
        parameter = data[1]
        value = data[2]
            
        bot.send_message(chat_id=Storage.adsystem_host, text=f"v1.survey:{user_id}:{parameter}:{value}")
        bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            
        return True
        
    elif callback_query.data.startswith("adsystemparameters") and int(callback_query.data.split("_")[1]) == 5:  # request captcha again
        bot.send_message(chat_id=Storage.adsystem_host, text=f"v1.survey:{callback_query.from_user.id}:3:0")
        return True 
        
    else:
        return False 

# подтверждение подключения бота   
def IsFromAdSystemTelebot(message: telebot.types.Message ):
    if message.from_user.id == Storage.adsystem_host: return True 
    else: return False     

def AdSystemBotTelebot(message, state):
    user = message.from_user.id
    if state == None: return True
    elif user in Storage.state and state == Storage.state[user]: return True
    else: return False  


def IAmTheOwnerTelebot(message, me, bot):
    Storage.me = me 
    Storage.bot = bot 
    if message.from_user.id == Storage.adsystem_host and message.text == "/adsystem": return True 
    elif message.from_user.username == Storage.me and message.text == "/adsystem": return True 
    else: False 

def AdSystemConnectBotTelebot(message: telebot.types.Message): 
    bot = Storage.bot 
    bot.reply_to(message, Storage.me)
    
    if message.from_user.id == Storage.adsystem_host:
        bot.reply_to(message, Storage.me)
    else:
        bot.reply_to(message, "✅ Бот успешно подключен к AdSystem!")


def AdSystemCallbackTelebot(callback_query: telebot.types.CallbackQuery):  
    user = callback_query.from_user.id
    if int(callback_query.data.split("_")[1]) == 1: 
        Storage.state[user] = False     # interests state
        Storage.interests[user] = {}
        buttons = [ik1t, ik2t, ik3t, ik4t, ik5t, ik6t, ik7t, ik8t, ik9t, ik10t, ik11t, ik12t, ik13t, ik14t, nxt]
        Storage.buttons[user]=deepcopy(buttons)
        
    elif int(callback_query.data.split("_")[1]) == 5:       # get captcha again
        Storage.state[user] = True      # capcha state 
        

def AdSystemGetInterestsTelebot(callback_query: telebot.types.CallbackQuery):   
    data = callback_query.data.split("_")   # get data
    user = callback_query.from_user.id
    
    bot = Storage.bot 
    
    user_id = callback_query.from_user.id
    parameter = data[1]
    value = data[2]
                    
    # получаем данные
    interests = Storage.interests[user]
    buttons = Storage.buttons[user]
        
    if value == "next" and interests.keys():
        bot.send_message(chat_id=Storage.adsystem_host, text=f"v1.survey:{user_id}:{parameter}:0:{list(interests.keys())}")
        bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        Storage.state[user] = True 
        del Storage.interests[user]
        del Storage.buttons[user]
    elif value == "next" and not interests.keys():
        bot.answer_callback_query(callback_query_id=callback_query.id, show_alert=True, text='Выберете Ваши интересы, потом нажмите кнопку "Далее"')
    else:
        value = int(value)
        # обновляем кнопки
        if value not in interests:
            buttons[value-1].text += " ✅"
            interests[value] = None
        else:
            buttons[value-1].text = buttons[value-1].text[:-2]
            del interests[value]
            
        # сохраняем кнопки 
        Storage.buttons[user] = buttons 
        Storage.interests[user] = interests
        
        # пересобираем клавиатуру
        new_keyboard = telebot.types.InlineKeyboardMarkup(row_width=4)
        new_keyboard.add(buttons[0], buttons[1])
        new_keyboard.add(buttons[2], buttons[3])
        new_keyboard.add(buttons[4], buttons[5])
        new_keyboard.add(buttons[6], buttons[7])
        new_keyboard.add(buttons[8], buttons[9])
        new_keyboard.add(buttons[10], buttons[11])
        new_keyboard.add(buttons[12], buttons[13])
        new_keyboard.add(buttons[14])
        
        bot.edit_message_reply_markup(chat_id=callback_query.from_user.id, message_id=callback_query.message.id, reply_markup=new_keyboard)

def AdSystemCaptchaTelebot(message: types.Message):
    bot = Storage.bot 
    user = message.from_user.id
    
    bot.send_message(chat_id=Storage.adsystem_host, text=f"v1.survey:{message.from_user.id}:4:{message.text}")
    
    try: del Storage.state[user]
    except KeyError: pass 
        
# отправка рекламного объявления
def AdSystemPhotoTelebot(message: types.Message, *args):
    bot = Storage.bot     
    if message.caption != None:
        if "ad:" in message.caption:    # send ad
            image = message.photo[0].file_id
            data = json.loads(message.caption.replace("ad:", "").replace("'", '"'))
            title = data['title']
            ad_text = data['ad_text']
            link = data['link']
            user = data['user']
            
            text = f"{title}\n{ad_text}"
            ad_keyboard = telebot.types.InlineKeyboardMarkup()
            ad_keyboard.add(telebot.types.InlineKeyboardButton("Перейти", url=link))
                    
            bot.send_photo(chat_id=user, photo=image, caption=text, reply_markup=ad_keyboard)
            
        else:   # send captcha
            image = message.photo[0].file_id
            data = message.caption.split("=")
            user_id = data[0]
            caption = data[1]
                
            bot.send_photo(chat_id=user_id, photo=image, caption=caption)
            
    elif message.text != None :
        data = message.text.split(":")
        if data[1] == "end":      # success
            bot.send_message(chat_id=data[0], text="✅ Успешно! Можете продолжать пользоваться ботом!")
        else:
            bot.send_message(chat_id=data[0], text=data[1], reply_markup=try_again_keyboard_telebot)

