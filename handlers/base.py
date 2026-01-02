from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButtonRequestUser, KeyboardButton

from aiogram.fsm.context import FSMContext
from states import SessionStates

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    kb = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text='Выбрать собеседника', request_user=KeyboardButtonRequestUser(request_id=1))
        ]],
        resize_keyboard=True
    )
    await message.answer(
        f'Привет, {message.from_user.full_name}! Выбери, с кем хочешь общаться 👇',
        reply_markup=kb,
    )
    await state.set_state(SessionStates.waiting_partner)
