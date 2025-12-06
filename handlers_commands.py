from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from core.config import ADMIN_ID

router = Router()


# ====== ТЕКСТЫ ======

WELCOME_TEXT = (
    "👋 Привет!\n\n"
    "Я <b>Cocoon</b> — лёгкий бот в стиле TON.\n"
    "Заворачиваю твой текст в шифрованный кокон и отпускаю в сеть.\n\n"
    "Нажми «🔒 Проверить приватность» и отправь любое сообщение 😌"
)

PRIVACY_TEXT = (
    "🔐 <b>Приватность Cocoon x TON</b>\n\n"
    "• У каждого пользователя свой шифровальный слой\n"
    "• Ключи хранятся только в памяти узла (бота)\n"
    "• Никаких логов и баз данных\n\n"
    "Лёгкий демо-узел в духе TON: чисто, прозрачно, без шума 🔵"
)

ABOUT_TEXT = (
    "🤍 <b>Cocoon</b>\n\n"
    "Минималистичный бот про приватность в стиле TON.\n"
    "Шифрую аккуратно, не храню лишнего и иногда шучу.\n\n"
    "Скоро здесь появится ещё больше функций 💎"
)


# ====== КНОПКИ ======

def main_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔒 Проверить приватность",
                    callback_data="test",
                )
            ],
            [
                InlineKeyboardButton(
                    text="Открыть",
                    web_app=WebAppInfo(
                        url="https://gradolz.pythonanywhere.com/panel?v=2"
                    ),
                )
            ],
            [
                InlineKeyboardButton(
                    text="ℹ️ О боте",
                    callback_data="about",
                )
            ],
        ]
    )


# ====== КОМАНДЫ ======

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        WELCOME_TEXT,
        reply_markup=main_keyboard(),
        parse_mode="HTML",
    )


@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        '✉️ Если нужна помощь или есть идеи по Cocoon, напиши сюда:\n'
        '<a href="https://t.me/cocoon_en_ru">@cocoon_en_ru</a>',
        parse_mode="HTML",
        disable_web_page_preview=True,
    )


@router.message(Command("privacy"))
async def cmd_privacy(message: types.Message):
    await message.answer(PRIVACY_TEXT, parse_mode="HTML")


@router.message(Command("about"))
async def cmd_about(message: types.Message):
    await message.answer(ABOUT_TEXT, parse_mode="HTML")


@router.message(Command("panel"))
async def cmd_panel(message: types.Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Открыть",
                    web_app=WebAppInfo(
                        url="https://gradolz.pythonanywhere.com/panel?v=2"
                    ),
                )
            ]
        ]
    )
    await message.answer("Мини-панель Cocoon:", reply_markup=kb)


@router.message(Command("stats"))
async def cmd_stats(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("Эта команда только для владельца 🙂")
        return
    # Простейший вывод, если нет своей статистики
    await message.answer("Статистика пока не подключена.", parse_mode="HTML")


# ====== CALLBACK-КНОПКИ ======

@router.callback_query(F.data == "test")
async def cb_test(callback: types.CallbackQuery):
    # текст под кнопкой "🔒 Проверить приватность"
    await callback.message.answer(
        "Отправь текст — я заверну его в шифрованный кокон 🔵"
    )
    # тихо пытаемся ответить на callback, чтобы убрать "часики"
    try:
        await callback.answer()
    except Exception:
        pass


@router.callback_query(F.data == "about")
async def cb_about(callback: types.CallbackQuery):
    # текст под кнопкой "ℹ️ О боте"
    await callback.message.answer(ABOUT_TEXT, parse_mode="HTML")
    try:
        await callback.answer()
    except Exception:
        pass

