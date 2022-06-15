from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

volm = KeyboardButton('Тише')
volp = KeyboardButton('Громче')
pause = KeyboardButton('Пауза')
close = KeyboardButton('Закрыть вкладку')
fullscr = KeyboardButton('Полноэкранный YT')


markup_vol = ReplyKeyboardMarkup(resize_keyboard=True).row(
    volm, volp).row(close).row(fullscr).row(pause)

