from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message
from keyboards.keyboards import gm_kb, yes_no_kb
from lexicon.lexicon import LEXICON
from services.services import get_bot_choice, get_winner

router: Router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'], reply_markup=yes_no_kb)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON['/help'], reply_markup=yes_no_kb)


# Этот хэндлер срабатывает на согласие пользователя играть в игру
@router.message(Text(text=LEXICON['yes_button']))
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON['yes'], reply_markup=gm_kb)


# Этот хэндлер срабатывает на отказ пользователя играть в игру
@router.message(Text(text=LEXICON['no_button']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON['no'])


# Этот хэндлер срабатывает на любую из игровых кнопок
@router.message(Text(text=[LEXICON['stone'],
                           LEXICON['paper'],
                           LEXICON['scissors']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON["bot_choice"]} '
                              f'- {LEXICON[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON[winner], reply_markup=yes_no_kb)