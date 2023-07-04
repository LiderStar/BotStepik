import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentType
from aiogram.filters import Command
from dotenv import load_dotenv
from aiogram import F


load_dotenv()

bot: Bot=Bot(token = os.environ.get('BOT_TOKEN'))
dp: Dispatcher=Dispatcher()

async def start_message(message: Message):
    await message.answer("Hello")

async def help_message(message: Message):
    await message.answer("Can I help you???")

async def photo_message(message: Message):
    print(message)
    await message.reply_photo(message.photo[-1].file_id)

async def else_message(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text = "Данный тип не потдерживается")


dp.message.register(start_message, Command(commands=['start']))
dp.message.register(help_message, Command(commands=['help']))
dp.message.register(photo_message, F.photo)  # F.audio F.voice F.document
dp.message.register(else_message)

if __name__ == "__main__":
    dp.run_polling(bot)