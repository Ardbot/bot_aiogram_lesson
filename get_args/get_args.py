from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

import Keyboard


async def test(message: types.Message):
    """ Здесь прописываю комманды на тест """

    """ Видео тут:  
    Документация: https://docs.aiogram.dev/en/latest/telegram/types/message.html#aiogram.types.message.Message.get_args
    """
    like_default = 1  # Значение по умолчанию
    msg = message.text
    command = message.get_command()  # Забираем команду с сообщения
    arguments = message.get_args()  # Забираем аргумент (кол-во лайков) после команды /like 5

    like = arguments  # Просто меняю название
    if not like:  # Если аргумента нет
        await message.answer(f"Вы не указали кол-во лайков. Выставлено по умолчанию: {like_default}\n")
    else:  # Если аргумент есть
        if like.isdigit():  # Проверяем число ли это
            await message.answer(f"{like} лайков этому господину!\n")
        else:
            await message.answer(f"{like} - это не число. Укажите число\n")

    await message.answer(f"Тестовое сообщение:\n"
                         f"Сообщение: {msg}  |  Команда: {command}  |  Аргумент: {like}\n", reply_markup=Keyboard.test_key)
    print(f"Сообщение: {msg}  |  Аргумент: {like}")


def register_handlers_like(dp: Dispatcher):
    dp.register_message_handler(test, commands="like", state="*")
    dp.register_message_handler(test, Text(equals="Лайк", ignore_case=True), state="*")
