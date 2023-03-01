from aiogram import F, Bot, Dispatcher
from aiogram.filters import Command, Text, CommandStart, ContentType, ContentTypeError
from aiogram.types import Message


from dotenv import load_dotenv
import random
import os

'''
ContentType.AUDIO == 'audio'                                # True
ContentType.TEXT == 'text'                                  # True
ContentType.PHOTO == 'photo'                                # True
ContentType.STICKER == 'sticker'                            # True
ContentType.CONTACT == 'contact'                            # True
ContentType.LOCATION == 'location'                          # True
ContentType.POLL == 'poll'                                  # True
ContentType.SUCCESSFUL_PAYMENT == 'successful_payment'      # True
ContentType.VOICE == 'voice'                                # True
ContentType.WEB_APP_DATA == 'web_app_data'                  # True

'''
bot: Bot = Bot(token="fdgfdg") 
dp: Dispatcher = Dispatcher(bot)

# Этот хэндлер будет срабатывать на тип контента "photo"
@dp.message(F.content_type == ContentTypeError.PHOTO)
async def process_send_photo(message: Message):
    await message.answer(text='Вы прислали фото')


# Этот хэндлер будет срабатывать на тип контента "photo"
@dp.message(F.content_type == 'photo')
async def process_send_photo(message: Message):
    await message.answer(text='Вы прислали фото')


# Этот хэндлер будет срабатывать на тип контента "voice", "video" или "text"
@dp.message(F.content_type.in_({'voice', 'video', 'text'}))
async def process_send_vovite(message: Message):
    await message.answer(text='Вы прислали войс, видео или текст')


# Этот хэндлер будет срабатывать на тип контента "voice", "video" или "text"
@dp.message(F.content_type.in_({ContentType.VOICE,
                                ContentType.VIDEO,
                                ContentType.TEXT}))
async def process_send_vovite(message: Message):
    await message.answer(text='Вы прислали войс, видео или текст')


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=['start']))
async def process_command_start(message: Message):
    await message.answer('Это команда /start')


# Этот хэндлер будет срабатывать на команду "|start"
@dp.message(Command(commands=['start'], prefix='|'))
async def process_command_start_2(message: Message):
    await message.answer('И это команда /start')



@dp.message(CommandStart())
async def process_command_start(message: Message):
    await message.answer('Это команда /start')



# полностью совпадает с каким-то текстом: Text(text='какой-то текст')
# начинается с какого-то конкретного текста: Text(startswith='начало какого-то текста')
# заканчивается каким-то текстом: Text(endswith='конец какого-то текста')
# содержит в себе какой-то текст: Text(contains='какой-то текст')

# Text(text=['какой-то текст 1', 'какой-то текст 2', 'какой-то текст 3'])
# Text(startswith=('начало 1', 'начало 2', 'начало 3'))
# Text(endswith={'конец 1', 'конец 2', 'конец 3'})
# Text(contains=['какой-то текст 1', 'какой-то текст 2', 'какой-то текст 3'])


# Этот хэндлер будет срабатывать на текст, заканчивающийся на "бот",
# причем регистр букв будет игнорироваться
@dp.message(Text(endswith=['бот'], ignore_case=True))
async def process_text_endswith_bot(message: Message):
    await message.answer(text='Ваше сообщение заканчивается на бот')


# F or lambda выбор 
F.photo                                    # Фильтр для фото
F.voice                                    # Фильтр для голосовых сообщений
F.content_type.in_({ContentType.PHOTO,
                    ContentType.VOICE,
                    ContentType.VIDEO})    # Фильтр на несколько типов контента
F.text == 'привет'                         # Фильтр на полное совпадение текста
F.text.startswith('привет')                # Фильтр на то, что текст сообщения начинается с 'привет'
~F.text.endswith('bot')                    # Инвертирование результата фильтра

lambda message: message.photo                        # Фильтр для фото
lambda message: message.voice                        # Фильтр для голосовых сообщений
lambda message: message.content_type in {ContentType.PHOTO,
                                         ContentType.VOICE,
                                         ContentType.VIDEO}   # Фильтр на несколько типов контента
lambda message: message.text == 'привет'             # Фильтр на полное совпадение текста
lambda message: message.text.startswith('привет')    # Фильтр на то, что текст сообщения начинается с 'привет'
lambda message: not message.text.startswith('bot')   # Инвертирование результата фильтра

lambda message: message.from_user.id == 173901673
F.from_user.id == 173901673

lambda message: message.from_user.id in {193905674, 173901673, 144941561}
F.from_user.id.in_({193905674, 173901673, 144941561})

lambda message: not message.text.startswith('Привет')
~F.text.startswith('Привет')

lambda message: not message.content_type in {ContentType.PHOTO,
                                             ContentType.VIDEO,
                                             ContentType.AUDIO,
                                             ContentType.DOCUMENT}

~F.content_type.in_({ContentType.PHOTO,
                     ContentType.VIDEO,
                     ContentType.AUDIO,
                     ContentType.DOCUMENT})
