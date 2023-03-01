''' Рассматриваем метод send_copy он заменяет кучу хендлеров для текста, фото, видео
и ....  '''
from aiogram import F, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from dotenv import load_dotenv
import os


load_dotenv()
# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=os.environ.get('bot_token'))
dp: Dispatcher = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="Данный тип не потдерживается")



if __name__ == '__main__':
    dp.run_polling(bot)