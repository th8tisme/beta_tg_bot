# /beta_tg_bot/handlers/base.py
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards import pick_partner_kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(
        f'Привет, {message.from_user.full_name}! Выбери, с кем хочешь общаться 👇',
        reply_markup=pick_partner_kb,
    )
