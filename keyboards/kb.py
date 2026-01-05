# /beta_tg_bot/keyboards/kb.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButtonRequestUser, KeyboardButton


session_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="❓ Задать вопрос")],
    ],
    resize_keyboard=True,
    input_field_placeholder="выбирай действие",
)

pick_partner_kb = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text='Выбрать собеседника', request_user=KeyboardButtonRequestUser(request_id=1))
        ]],
        resize_keyboard=True
    )
