import random

from lexicon.lexicon import LEXICON


# Функция, возвращающая случайный выбор бота в игре
def get_bot_choice() -> str:
    return random.choice(['stone', 'paper', 'scissors'])


# Функция, возвращающая ключ из словаря, по которому
# хранится значение, передаваемое как аргумент - выбор пользователя
def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON:
        if LEXICON[key] == user_answer:
            return key
    raise Exception


# Функция, определяющая победителя
def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules: dict[str, str] = {'stone': 'scissors',
                             'scissors': 'paper',
                             'paper': 'stone'}
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    else:
        return 'bot_won'

