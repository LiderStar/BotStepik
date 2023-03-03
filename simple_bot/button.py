from aiogram import F, Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from dotenv import load_dotenv
import random
import os


load_dotenv()
# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=os.environ.get('bot_token'))
dp: Dispatcher = Dispatcher()
# Количество попыток, доступных пользователю в игре


# Генерируем список с кнопками
buttons: list[KeyboardButton] = [
    KeyboardButton(text=f'Кнопка {i}') for i in range(1, 10)]

# Составляем список списков для будущей клавиатуры
keyboard: list[list[KeyboardButton]] = [[buttons[0]],
                                        buttons[1:3],
                                        buttons[3:6],
                                        buttons[6:8],
                                        [buttons[8]]]

# Создаем объект клавиатуры, добавляя в него список списков с кнопками
my_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                        keyboard=keyboard,
                                        resize_keyboard=True)


# button_1: KeyboardButton = KeyboardButton(text='start')
# button_2: KeyboardButton = KeyboardButton(text='help')
# button_3: KeyboardButton = KeyboardButton(text='cancel')
# button_4: KeyboardButton = KeyboardButton(text='Да')


# keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
#                                     keyboard=[[button_1, button_2],[button_3,button_4]],
#                                     resize_keyboard=True,
#                                     one_time_keyboard=True)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Привет!\nДля вызова справки набери /help ', reply_markup=my_keyboard)

# # Этот хэндлер будет срабатывать на команду "/help"
# @dp.message(Text(text=['help']))
# async def process_help_command(message: Message):
#     await message.answer(text='Правила игры')


# # Этот хэндлер будет срабатывать на команду "/cancel"
# @dp.message(Text(text=['cancel']))
# async def process_cancel_command(message: Message):
#         await message.answer(text='Вы вышли из игры. Если захотите сыграть снова - напишите об этом')
       

# # Этот хэндлер будет срабатывать на согласие пользователя сыграть в игру

# @dp.message(Text(text=['Да']))
# async def process_game_command(message: Message):
#     await message.answer(text='Ура!')

if __name__ == '__main__':
    dp.run_polling(bot)
