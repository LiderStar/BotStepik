import os

from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN: str = os.environ.get('BOT_TOKEN')

print(BOT_TOKEN)