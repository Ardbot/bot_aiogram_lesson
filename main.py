""" Тестовый раздел для уроков """
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand

import config
from get_args.get_args import register_handlers_like
from test import register_handlers_test


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/like", description="Тест get_args"),
        BotCommand(command="/start", description="Старт и регистрация"),
        BotCommand(command="/cancel", description="Отменить текущее действие")
    ]
    await bot.set_my_commands(commands)


async def main():
    bot = Bot(token=config.TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage())

    """ Регистрация хэндлеров """
    register_handlers_test(dp)
    register_handlers_like(dp)


    """ Установка команд бота """
    await set_commands(bot)

    """ Запуск поллинга """
    # await dp.skip_updates()  # пропуск накопившихся апдейтов (необязательно)
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())

