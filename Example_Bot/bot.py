from aiogram import Bot, Dispatcher, types
from Example_Bot.config_data import config

bot: Bot = Bot(token=config.BOT_TOKEN, parse_mode='HTML')
dp: Dispatcher = Dispatcher()

