from aiogram import Router, F
from aiogram.types import Message

import storage

router = Router()


@router.message(F.text.lower() == 'вопрос')
async def send_question(message: Message):
    user_id = message.from_user.id
    active_sessions = storage.get_user_sessions(user_id)

    if not active_sessions:
        await message.answer('Нет активных сессий 😕 Сначала выбери собеседника.')
        return

    # для простоты — берём первую
    session_id = active_sessions[0]
    partner_id = storage.get_partner(session_id, user_id)
    q = storage.pick_question(session_id)

    if not q:
        await message.answer('Вопросы в этой сессии закончились.')
        return

    await message.bot.send_message(partner_id, f'🤔 Вопрос от собеседника:\n\n{q}')
    await message.answer('Отправил ✅')
