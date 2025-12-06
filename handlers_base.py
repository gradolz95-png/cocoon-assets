import asyncio
from aiogram import Router, types
from aiogram.filters import Command

from .keyboards import main_keyboard
from .texts import WELCOME_TEXT, PRIVACY_TEXT, ABOUT_TEXT, update_stats, format_stats
from core.config import ADMIN_ID

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    update_stats(message.from_user.id)
    await message.answer(WELCOME_TEXT, reply_markup=main_keyboard(), parse_mode="HTML")


@router.message(Command("privacy"))
async def cmd_privacy(message: types.Message):
    update_stats(message.from_user.id)
    await message.answer(PRIVACY_TEXT, parse_mode="HTML")


@router.message(Command("about"))
async def cmd_about(message: types.Message):
    update_stats(message.from_user.id)
    await message.answer(ABOUT_TEXT, parse_mode="HTML")


@router.message(Command("stats"))
async def cmd_stats(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("Эта команда только для владельца 🙂")
        return
    await message.answer(format_stats(), parse_mode="HTML")
