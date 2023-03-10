from dataclasses import dataclass
from dotenv import load_dotenv
import os

@dataclass
class DatabaseConfig:
    database: str
    db_host: str
    db_user: str
    db_password: str
    db_port: int

    
@dataclass
class TgBot:
    token: str
    admin_ids: list[int]

@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig

load_dotenv()


# Создаем экземпляр класса Config и наполняем его данными из переменных окружения
config = Config(tg_bot=TgBot(token=os.environ.get('BOT_TOKEN'),
                             admin_ids=list(map(int, os.environ.get('ADMIN_IDS').split(",")))),
                db=DatabaseConfig(database=os.environ.get('DATABASE'),
                                  db_host=os.environ.get('DB_HOST'),
                                  db_user=os.environ.get('DB_USER'),
                                  db_password=os.environ.get('DB_PASSWORD'),
                                  db_port=int(os.environ.get('DB_PORT'))))

# Выводим значения полей экземпляра класса Config на печать, 
# чтобы убедиться, что все данные, получаемые из переменных окружения, доступны
print('BOT_TOKEN:', config.tg_bot.token)
print('ADMIN_IDS:', config.tg_bot.admin_ids)
print()
print('DATABASE:', config.db.database)
print('DB_HOST:', config.db.db_host)
print('DB_USER:', config.db.db_user)
print('DB_PASSWORD:', config.db.db_password)
print('DB_PORT:', config.db.db_port)


# POSTGRES_URI= f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DATABASE}'