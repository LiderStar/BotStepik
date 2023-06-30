from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, filters, F
from aiogram.filters import Command, Filter
import os
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup




load_dotenv()

# Initialize bot and dispatcher
bot: Bot = Bot(token=os.environ.get('BOT_TOKEN'), parse_mode='HTML')
dp: Dispatcher = Dispatcher()

# Generate keyboard
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


# bot = Bot(token=os.environ.get('BOT_TOKEN'))
# dp = Dispatcher() 

@dp.message(Command('start'))

async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.", reply_markup=my_keyboard)



@dp.message(Command('help'))

async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message(filters.Text(text='Кнопка 2', ignore_case=True))
async def filter_button(message: types.Message):
    await message.answer('Была нажата кнопка 2')


# @dp.message(filters.IS_ADMIN())
# async def filter_button(message: types.Message):
#     await message.answer('Flvbybcnhfnjh')

@dp.message(F.contant_type=="photo")
async def send_photo(message: types.Message):
    await message.answer("Cool photo")






@dp.message()
async def send_all(message: types.Message):
    """
    This handler will be called when user sends somthing else
    """
    # await message.reply(f"{message.from_user.id} \n {message.from_user.full_name} \n {message.text}") 
    await message.answer(f"{message.from_user.id} \n {message.from_user.full_name} \n {message.text} {filters.IS_ADMIN}")


if __name__ == '__main__':
    dp.run_polling(bot)