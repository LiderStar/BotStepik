from aiogram import F, Bot, Dispatcher
from aiogram.filters import Command, Text
from aiogram.types import Message

from dotenv import load_dotenv
import random
import os


load_dotenv()
# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=os.environ.get('bot_token'))
dp: Dispatcher = Dispatcher()
# Количество попыток, доступных пользователю в игре
ATTEMPTS: int = 5

user: dict = {

}


def get_random_number() -> int:
    return random.randint(1, 100)

# Этот хэндлер будет срабатывать на команду "/start"

def get_start(message: Message) -> bool:
    return message.text == '/start'



# @dp.message(Command(commands=["start"]))
@dp.message(get_start)
async def process_start_command(message: Message):
    await message.answer('Привет!\nДавай сыграем в\nУгадай число \nДля вызова справки набери /help ')
    if message.from_user.id not in user:
        user[message.from_user.id] = {
            'in_game': False,
            'secret_number': None,
            'attempts': None,
            'total_games': 0,
            'wins': 0}


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(f'Правила игры:\n\nЯ загадываю число от 1 до 100, '
                         f'а вам нужно его угадать\nУ вас есть {ATTEMPTS} '
                         f'попыток\n\nДоступные команды:\n/help - правила '
                         f'игры и список команд\n/cancel - выйти из игры\n'
                         f'/stat - посмотреть статистику\n\nДавай сыграем?')

# Этот хэндлер будет срабатывать на команду "/start"


# @dp.message(Command(commands=["start"]))
@dp.message(get_start)
async def process_start_command(message: Message):
    await message.answer(f"Всего игр сыграно: {user[message.from_user.id]['total_games']}\n"
                         f"Игр выиграно: {user[message.from_user.id]['wins']}")


# Этот хэндлер будет срабатывать на команду "/cancel"
@dp.message(Command(commands=['cancel']))
async def process_cancel_command(message: Message):
    if user[message.from_user.id]['in_game']:
        await message.answer('Вы вышли из игры. Если захотите сыграть снова - напишите об этом')
        user[message.from_user.id]['in_game'] = False
    else:
        await message.answer('А мы итак с вами не играем. '
                             'Может, сыграем разок?')

# Этот хэндлер будет срабатывать на согласие пользователя сыграть в игру


@dp.message(Text(text=['Да', 'Давай', 'Сыграем', 'Игра',
                       'Играть', 'Хочу играть'], ignore_case=True))
async def process_game_command(message: Message):
    if not user[message.from_user.id]['in_game']:
        await message.answer('Ура!\n\nЯ загадал число от 1 до 100, '
                             'попробуй угадать!')
        user[message.from_user.id]['in_game'] = True
        user[message.from_user.id]['secret_number'] = get_random_number()
        user[message.from_user.id]['attempts'] = ATTEMPTS
    else:
        await message.answer('Пока мы играем в игру я могу '
                             'реагировать только на числа от 1 до 100 '
                             'и команды /cancel и /stat')

# Этот хэндлер будет срабатывать на отказ пользователя сыграть в игру


@dp.message(Text(text=['Нет', 'Не', 'Не хочу', 'Не буду'], ignore_case=True))
async def process_negative_answer(message: Message):
    if not user[message.from_user.id]['in_game']:
        await message.answer('Жаль :(\n\nЕсли захотите поиграть - просто '
                             'напишите об этом')
    else:
        await message.answer('Мы же сейчас с вами играем. Присылайте, '
                             'пожалуйста, числа от 1 до 100')


@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_guess_ancwer(message: Message):
    if user[message.from_user.id]['in_game']:
        if int(message.text) == user[message.from_user.id]['secret_number']:
            await message.answer('Ура Вы выиграли')
            user[message.from_user.id]['in_game'] = False
            user[message.from_user.id]['total_game'] += 1
            user[message.from_user.id]['wins'] += 1
        elif int(message.text) > user[message.from_user.id]['secret_number']:
            await message.answer('Загаданное число меньше')
            user[message.from_user.id]['attempts'] -= 1
        elif int(message.text) < user[message.from_user.id]['secret_number']:
            await message.answer('Загаданное число больше')
            user[message.from_user.id]['attempts'] -= 1

        if user[message.from_user.id]['attempts'] == 0:
            await message.answer('У Вас закончились попытки. Вы проиграли. ' + f"Загаданное число {user[message.from_user.id]['secret_number']}" + f" Давайте еще сыграем???")
            user[message.from_user.id]['in_game'] = False
            user[message.from_user.id]['total_games'] += 1

    else:
        await message.answer("Мы еще не играли, хотите сыграть")

# Хэндлер для любого другого ввода


@dp.message()
async def process_other_text_answers(message: Message):
    if user[message.from_user.id]['in_game']:
        await message.answer('Мы же сейчас с вами играем. '
                             'Присылайте, пожалуйста, числа от 1 до 100')
    else:
        await message.answer('Я довольно ограниченный бот, давайте '
                             'просто сыграем в игру?')


if __name__ == '__main__':
    dp.run_polling(bot)
