""" Создаем клавиатуру """
from aiogram.types import ReplyKeyboardMarkup

cancel = "Отмена"

test_key = ReplyKeyboardMarkup(resize_keyboard=True).add('Лайк')
# test_key.add("...", "...")
test_key.add(cancel)