# /beta_tg_bot/handlers/base.py
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from aiogram.fsm.context import FSMContext
from states import SessionStates

from keyboards import pick_partner_kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    await message.answer(
        f'Привет, {message.from_user.full_name}! Выбери, с кем хочешь общаться 👇',
        reply_markup=pick_partner_kb,
    )
    await state.set_state(SessionStates.waiting_partner)
