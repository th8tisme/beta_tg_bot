from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

import storage
from keyboards import session_kb

router = Router()


@router.message(F.user_shared)
async def handle_user_shared(message: Message):
    partner_id = message.user_shared.user_id
    initiator_id = message.from_user.id

    if partner_id == initiator_id:
        await message.answer('Ты не можешь выбрать сам себя 🤪')
        return

    session_id = storage.create_session(initiator_id, partner_id)

    # отправим партнёру подтверждение
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='✅ Принять', callback_data=f'accept:{session_id}'),
            InlineKeyboardButton(text='❌ Отказаться', callback_data=f'decline:{session_id}')
        ]
    ])
    await message.bot.send_message(
        partner_id,
        f'👋 Пользователь {message.from_user.full_name} хочет общаться с тобой. Принять?',
        reply_markup=kb
    )

    await message.answer('Ждём подтверждение от собеседника.')


@router.callback_query(F.data.startswith('accept:'))
async def accept_session(callback: CallbackQuery):
    session_id = callback.data.split(':')[1]
    session = storage.confirm_session(session_id)

    if not session:
        await callback.answer('Сессия не найдена', show_alert=True)
        return

    initiator_id = session['a']

    await callback.message.answer(
        '💬 Сессия активна.\nТеперь можно задавать вопросы 👇',
        reply_markup=session_kb,
    )

    await callback.bot.send_message(
        initiator_id,
        '🔥 Партнёр подтвердил.\nМожешь задавать вопросы 👇',
        reply_markup=session_kb,
    )


@router.callback_query(F.data.startswith('decline:'))
async def decline_session(callback: CallbackQuery):
    session_id = callback.data.split(':')[1]
    storage.cancel_session(session_id)
    await callback.message.answer('❌ Вы отказались от общения. Сессия отменена.')
