from aiogram import F, Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from dotenv import load_dotenv
import os


load_dotenv()

bot: Bot = Bot(token=os.environ.get('bot_token'))
dp: Dispatcher = Dispatcher()
# Инициализируем объект билдера
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
# Создаем список с кнопками (например, 10 кнопок)
buttons: list[KeyboardButton] = [KeyboardButton(
                text=f'Кнопка {i + 1}') for i in range(10)]
# Методами билдера добавляем в него кнопки
# (возьмем для примера метод row()),
# в одном ряду должно быть 4 кнопки
kb_builder.row(*buttons, width=4)

# kb_builder.add(*buttons_2) добавляет кнопки пока их не будет 8

# Распаковываем список с кнопками методом add
# kb_builder.add(*buttons_1)

# Явно сообщаем билдеру сколько хотим видеть кнопок в 1-м и 2-м рядах
# в 3 ряду будет столько же сколько и во втором и так пока не закончатся кнопки,
# если поставить 1 то будет 1 кнопка в ряду
# kb_builder.adjust(1, 3)


# Явно сообщаем билдеру сколько хотим видеть кнопок в 1-м и 2-м рядах,
# а также говорим методу повторять такое размещение для остальных рядов
# kb_builder.adjust(2, 1, repeat=True)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Вот такая получается клавиатура',
                         reply_markup=kb_builder.as_markup(resize_keyboard=True))


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