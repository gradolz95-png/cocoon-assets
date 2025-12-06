from aiogram import Dispatcher

from .handlers_commands import router as commands_router
from .handlers_encrypt import router as encrypt_router


def create_dispatcher() -> Dispatcher:
    dp = Dispatcher()
    dp.include_router(commands_router)
    dp.include_router(encrypt_router)
    return dp
