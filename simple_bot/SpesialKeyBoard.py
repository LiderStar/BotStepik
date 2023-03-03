from aiogram import F, Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, KeyboardButtonPollType, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from dotenv import load_dotenv
import os

load_dotenv()

bot: Bot = Bot(token=os.environ.get('bot_token'))
dp: Dispatcher = Dispatcher()
# Инициализируем объект билдера
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

contact_btn: KeyboardButton = KeyboardButton(text='Отправить телефон',
                                             request_contact=True)
geo_btn: KeyboardButton = KeyboardButton(text='Отправить геопозицию',
                                         request_location=True)

poll_btn_2: KeyboardButton = KeyboardButton(
                                text='Создать опрос',
                                request_poll=KeyboardButtonPollType(
                                                        type='regular'))

quiz_btn: KeyboardButton = KeyboardButton(
                                text='Создать викторину',
                                request_poll=KeyboardButtonPollType(
                                                        type='quiz'))
web_app_btn: KeyboardButton = KeyboardButton(
                                text='Start Web App',
                                web_app=WebAppInfo(url="https://www.ukr.net/news/main.html"))

kb_builder.row(contact_btn, geo_btn, width=1)
kb_builder.row(poll_btn_2, quiz_btn, width=2)
kb_builder.row(web_app_btn, width=1)

keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
web_app_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                            text='Start Web App',
                                            keyboard=[[web_app_btn]],
                                            resize_keyboard=True)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Вот такая получается клавиатура',
                         reply_markup=keyboard)\



@dp.message(Command(commands='web_app'))
async def process_start_command(message: Message):
    await message.answer(text='Экспериментируем со специальными кнопками',
                         reply_markup=web_app_keyboard)


if __name__ == '__main__':
    dp.run_polling(bot)

"""
Несколько рядов с  разным расположением кнопак

# Создаем первый список с кнопками
buttons_1: list[KeyboardButton] = [KeyboardButton(
                text=f'Кнопка {i + 1}') for i in range(6)]

# Создаем второй список с кнопками
buttons_2: list[KeyboardButton] = [KeyboardButton(
                text=f'Кнопка {i + 7}') for i in range(4)]

# Распаковываем список с кнопками в билдер, указываем, что
# в одном ряду должно быть 4 кнопки
kb_builder.row(*buttons_1, width=4)

# Еще раз распаковываем список с кнопками в билдер, указываем, что
# теперь в одном ряду должно быть 3 кнопки
kb_builder.row(*buttons_2, width=3)
"""
