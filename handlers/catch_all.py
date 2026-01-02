# bot_tg/handlers/catch_all.py
import logging

from aiogram import Router
# from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards import questions_kb

router = Router()
logger = logging.getLogger('beta_tg_bot.handlers.catch_all')


@router.message()
# async def catch_all(message: Message, state: FSMContext) -> None:
async def catch_all(message: Message) -> None:
    user = message.from_user
    # current_state = await state.get_state()

    logger.info(
        "UNHANDLED_MESSAGE",
        extra={
            "user_id": user.id if user else None,
            "username": user.username if user else None,
            "chat_id": message.chat.id,
            "message_id": message.message_id,
            "content_type": message.content_type,
            "text": message.text,
        }
    )

    await message.answer(
        'Ну и хера ли ты написал? 🤔\n'
        'Давай по новой!',
        reply_markup=questions_kb,
    )
