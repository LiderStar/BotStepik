from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


# Создаем экземпляр класса Config и наполняем его данными из переменных окружения
config = Config(tg_bot=TgBot(token=os.environ.get('BOT_TOKEN')))

# Выводим значения полей экземпляра класса Config на печать,
# # чтобы убедиться, что все данные, получаемые из переменных окружения, доступны
# print('BOT_TOKEN:', config.tg_bot.token)
#
# print()


