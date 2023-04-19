import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from handlers import other_handlers, user_handlers
from keyboards.set_menu import set_main_menu
from config_data.config import config

# инициализируем логгер
logger = logging.getLogger(__name__)

async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s'u'[%(asctime)s] - %(name)s - %(message)s')
    # Выводим в консоль информацию о начале запуска бота
    logger.info("Start bot")
    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()
    # Регистриуем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    # Настраиваем кнопку Menu
    await set_main_menu(bot)
    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)  # так делать плохо в продакшене
    await dp.start_polling(bot)


if __name__ == "__main__":
    # Регистрируем асинхронную функцию в диспетчере,
    # которая будет выполняться на старте бота,
    try:
        # Запускаем функцию main в асинхронном режиме
        asyncio.run(main())

    except (KeyboardInterrupt, SystemExit):
        # Выводим в консоль сообщение об ошибке,
        # если получены исключения KeyboardInterrupt или SystemExit
        logger.error('Bot stopped!')
