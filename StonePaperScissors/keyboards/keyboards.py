from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import LEXICON

# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

# Создаем кнопки с ответами согласия и отказа
button_yes: KeyboardButton = KeyboardButton(text=LEXICON['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON['no_button'])
button_stone: KeyboardButton = KeyboardButton(text=LEXICON['stone'])
button_scissors: KeyboardButton = KeyboardButton(text=LEXICON['scissors'])
button_paper: KeyboardButton = KeyboardButton(text=LEXICON['paper'])

# Инициализируем билдер для клавиатуры с кнопками "Давай" и "Не хочу!"
yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с параметром width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)
kb_builder.row(button_stone, button_paper, button_scissors, width=3)
# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
yes_no_kb = yes_no_kb_builder.as_markup(
                                one_time_keyboard=True,
                                resize_keyboard=True)
gm_kb = kb_builder.as_markup(resize_keyboard=True)

# # ------- Создаем игровую клавиатуру без использования билдера -------
#
# # Создаем кнопки игровой клавиатуры
# button_1: KeyboardButton = KeyboardButton(text=LEXICON['stone'])
# button_2: KeyboardButton = KeyboardButton(text=LEXICON['scissors'])
# button_3: KeyboardButton = KeyboardButton(text=LEXICON['paper'])
#
# # Создаем игровую клавиатуру с кнопками "Камень 🗿",
# # "Ножницы ✂" и "Бумага 📜" как список списков
# game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
#                                     keyboard=[[button_1],
#                                               [button_2],
#                                               [button_3]],
#                                     resize_keyboard=True)