from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

import Keyboard


async def test(message: types.Message):
    """ Здесь прописываю комманды на тест """




def register_handlers_test(dp: Dispatcher):
    dp.register_message_handler(test, commands="test", state="*")
    dp.register_message_handler(test, Text(equals="Тест", ignore_case=True), state="*")
