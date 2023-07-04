import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentType
from aiogram.filters import Command
from dotenv import load_dotenv
from aiogram import F



load_dotenv()

bot: Bot=Bot(token = os.environ.get('BOT_TOKEN'))
dp: Dispatcher=Dispatcher()


@dp.message(Command(commands=['start']))
async def start_message(message: Message):
    await message.answer("Hello")

@dp.message(Command(commands=['help']))
async def help_message(message: Message):
    await message.answer("Can I help you???")

@dp.message(F.photo)   # F.audio F.voice F.document
async def photo_message(message: Message):
    print(message)
    await message.reply_photo(message.photo[-1].file_id)


@dp.message()
async def else_message(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text = "Данный тип не потдерживается")


if __name__ == "__main__":
    dp.run_polling(bot)