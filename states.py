from aiogram.fsm.state import State, StatesGroup

class SessionStates(StatesGroup):
    waiting_partner = State()
    waiting_confirmation = State()
    in_chat = State()
