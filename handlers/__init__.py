# /beta_tg_bot/handlers/
from aiogram import Dispatcher

from . import base, catch_all, questions


def setup_routers(dp: Dispatcher) -> None:
    dp.include_router(base.router)
    dp.include_router(questions.router)
    dp.include_router(catch_all.router)
