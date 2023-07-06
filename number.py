import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentType
from aiogram.filters import Command, Text
from dotenv import load_dotenv
from aiogram import F
from random import randint

load_dotenv()

bot: Bot = Bot(token=os.environ.get("BOT_TOKEN"))
dp: Dispatcher = Dispatcher()
ATTEMPTS: int = 5


user_status: dict = {}


def secret_num() -> int:
    return randint(1, 100)


@dp.message(Command(commands=["start"]))
async def start_message(message: Message):
    await message.answer(
        'Привет!\nДавай сыграем в игру "Угадай число"?\n\n'
        "Чтобы получить правила игры и список доступных "
        "команд - отправьте команду /help"
    )
    if message.from_user.id not in user_status:
        user_status[message.from_user.id] = {
            "ingame": False,
            "secret_number": None,
            "attemps": None,
            "total_games": 0,
            "wins": 0,
        }


@dp.message(Command(commands=["help"]))
async def help_message(message: Message):
    await message.answer(
        f"Правила игры:\n\nЯ загадываю число от 1 до 100, "
        f"а вам нужно его угадать\nУ вас есть {ATTEMPTS} "
        f"попыток\n\nДоступные команды:\n/help - правила "
        f"игры и список команд\n/cancel - выйти из игры\n"
        f"/stat - посмотреть статистику\n\nДавай сыграем?"
    )


@dp.message(Command(commands=["stat"]))
async def stat_message(message: Message):
    await message.answer(
        f'Всего игр сыграно: {user_status[message.from_user.id]["total_games"]}\n'
        f'Игр выиграно: {user_status[message.from_user.id]["wins"]}'
    )


@dp.message(Command(commands=["cancel"]))
async def cancell_command(message: Message):
    if user_status[message.from_user.id]["ingame"]:
        await message.answear("Очень жаль что Вы уходите")
        user_status[message.from_user.id]["ingame"] = False
    else:
        await message.answer("Мы и так не играли")


@dp.message(
    Text(text=["Да", "Дававй", "Еще", "Yes", "YES", "ДА", "ДАВАЙ"], ignore_case=True)
)
async def play_message(message: Message):
    if not user_status[message.from_user.id]["ingame"]:
        await message.answer(
            "Ура!\n\nЯ загадал число от 1 до 100, " "попробуй угадать!"
        )
        user_status[message.from_user.id]["ingame"] = True
        user_status[message.from_user.id]["secret_number"] = secret_num()
        user_status[message.from_user.id]["total_games"] += 1
        user_status[message.from_user.id]["attemps"] = ATTEMPTS
    else:
        await message.answer(
            "Пока мы играем в игру я могу "
            "реагировать только на числа от 1 до 100 "
            "и команды /cancel и /stat"
        )


@dp.message(Text(text=["Нет", "Не", "Не хочу", "Не буду"], ignore_case=True))
async def process_negative_answer(message: Message):
    if not user_status[message.from_user.id]["ingame"]:
        await message.answer(
            "Жаль :(\n\nЕсли захотите поиграть - просто " "напишите об этом"
        )
    else:
        await message.answer(
            "Мы же сейчас с вами играем. Присылайте, " "пожалуйста, числа от 1 до 100"
        )


@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def check_num(message: Message):
    if user_status[message.from_user.id]["ingame"]:
        if int(message.text) == user_status[message.from_user.id]["secret_number"]:
            await message.answer("Ура!!! Вы угадали число!\n\n" "Может, сыграем еще?")
            user_status[message.from_user.id]["ingame"] = False
            user_status[message.from_user.id]["total_games"] += 1
            user_status[message.from_user.id]["wins"] += 1
        elif int(message.text) > user_status[message.from_user.id]["secret_number"]:
            await message.answer("Мое число меньше")
            user_status[message.from_user.id]["attemps"] -= 1
        elif int(message.text) < user_status[message.from_user.id]["secret_number"]:
            await message.answer("Мое число больше")
            user_status[message.from_user.id]["attempts"] -= 1

        if user_status["attemps"] == 0:
            await message.answer(
                f"К сожалению, у вас больше не осталось "
                f"попыток. Вы проиграли :(\n\nМое число "
                f'было {user_status[message.from_user.id]["secret_number"]}\n\nДавайте '
                f"сыграем еще?"
            )
            user_status[message.from_user.id]["ingame"] = False
            user_status[message.from_user.id]["total_games"] += 1
    else:
        await message.answer("Мы еще не играем. Хотите сыграть?")


@dp.message()
async def else_message(message: Message):
    if user_status[message.from_user.id]["ingame"]:
        await message.answer(
            "Мы же сейчас с вами играем. " "Присылайте, пожалуйста, числа от 1 до 100"
        )
    else:
        await message.answer(
            "Я довольно ограниченный бот, давайте " "просто сыграем в игру?"
        )


if __name__ == "__main__":
    dp.run_polling(bot)
