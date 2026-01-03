from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

session_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="❓ Задать вопрос")],
    ],
    resize_keyboard=True,
    input_field_placeholder="выбирай действие",
)
