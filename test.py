import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv



load_dotenv()

bot: Bot=Bot(token = os.environ.get('BOT_TOKEN'))
dp: Dispatcher=Dispatcher()


@dp.message(Command(commands=['start']))
async def start_message(message: Message):
    await message.answer("Hello")

@dp.message(Command(commands=['help']))
async def help_message(message: Message):
    await message.answer("Can I help you???")

@dp.message()
async def else_message(message: Message):
    await message.answer("Nice to meet you")


if __name__ == "__main__":
    dp.run_polling(bot)