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


if __name__ == "__main__":
    dp.run_polling(bot)