# /beta_tg_bot/handlers/questions.py
from aiogram import Router, F
from aiogram.types import Message

import storage

router = Router()


@router.message(F.text == "❓ Задать вопрос")
async def ask_question(message: Message):
    user_id = message.from_user.id

    sessions = storage.get_user_sessions(user_id)
    if not sessions:
        await message.answer("У тебя нет активных сессий 😕")
        return

    session_id = sessions[0]
    partner_id = storage.get_partner(session_id, user_id)

    question = storage.pick_question(session_id)
    if not question:
        await message.answer("Вопросы для этой сессии закончились 🫠")
        return

    await message.bot.send_message(
        partner_id,
        f"❓ Вопрос от собеседника:\n\n{question}"
    )

    await message.answer("Отправил вопрос ✅")
