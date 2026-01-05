# /beta_tg_bot/keyboards/questions.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

contact_pick_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Выбрать контакт', request_contact=True)]],
    resize_keyboard=True,
    input_field_placeholder='выбери контакт, с кем бот будет общаться',
)


questions_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Показать вопрос')],
        [KeyboardButton(text='Отправить вопрос контакту')],
        [KeyboardButton(text='Выбрать контакт')],
    ],
    resize_keyboard=True,
    input_field_placeholder='выбирай',
)
