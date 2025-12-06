import secrets
from datetime import datetime, timedelta
from typing import Dict, Tuple

from aiogram import Router, F, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from cryptography.fernet import Fernet

from core.config import DECRYPT_TTL

router = Router()

# user_id -> ключ шифрования
_user_keys: Dict[int, bytes] = {}

# decrypt_id -> (original_text, expires_at)
_decrypt_storage: Dict[str, Tuple[str, datetime]] = {}


def _get_cipher(user_id: int) -> Fernet:
    if user_id not in _user_keys:
        _user_keys[user_id] = Fernet.generate_key()
    return Fernet(_user_keys[user_id])


def _generate_decrypt_id() -> str:
    return secrets.token_hex(8)


def _build_mood_prefix(text: str) -> str:
    length = len(text)
    has_emoji = any(ord(ch) > 0x1F000 for ch in text)
    is_caps = text.isupper() and length > 4

    if length > 200:
        return "📚 Ого, целая глава романа. Заворачиваю в шифрованный кокон.\n\n"
    if length < 10:
        return "✨ Минимализм — уважаю. Шифрую аккуратно.\n\n"
    if has_emoji:
        return "🙂 Поймал эмоции, шифрую и их тоже.\n\n"
    if is_caps:
        return "🔊 Немного громко, но я всё равно зашифрую потише.\n\n"

    return "🔐 Обрабатываю твой текст по всем правилам приватности.\n\n"


def _cleanup_expired() -> None:
    now = datetime.utcnow()
    to_delete = [k for k, (_, exp) in _decrypt_storage.items() if exp < now]
    for k in to_delete:
        _decrypt_storage.pop(k, None)


@router.callback_query(F.data.startswith("decrypt:"))
async def cb_decrypt(callback: types.CallbackQuery):
    decrypt_id = callback.data.split(":", 1)[1]

    _cleanup_expired()
    entry = _decrypt_storage.get(decrypt_id)

    if not entry:
        try:
            await callback.answer("Срок действия расшифровки истёк 🙂", show_alert=True)
        except RuntimeError:
            pass
        return

    original, _ = entry

    await callback.message.answer(
        f"🔓 <b>Расшифровка</b>\n\n<code>{original}</code>",
        parse_mode="HTML",
    )

    _decrypt_storage.pop(decrypt_id, None)

    try:
        await callback.answer()
    except RuntimeError:
        pass


@router.message(F.text)
async def encrypt_text(message: types.Message):
    text = (message.text or "").strip()
    if not text:
        return

    if text.startswith("/"):
        return

    cipher = _get_cipher(message.from_user.id)
    encrypted = cipher.encrypt(text.encode()).decode()

    decrypt_id = _generate_decrypt_id()
    expires_at = datetime.utcnow() + timedelta(seconds=DECRYPT_TTL)
    _decrypt_storage[decrypt_id] = (text, expires_at)

    mood = _build_mood_prefix(text)

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔓 Расшифровать",
                    callback_data=f"decrypt:{decrypt_id}",
                )
            ],
            [
                InlineKeyboardButton(
                    text="Открыть",
                    web_app=WebAppInfo(
                        url="https://gradolz.pythonanywhere.com/panel"
                    ),
                )
            ],
        ]
    )

    reply = (
        mood
        + "Твой текст теперь выглядит как шифр:\n"
        f"<code>{encrypted}</code>\n\n"
        "<i>Хочешь — могу расшифровать 😉</i>"
    )

    await message.answer(reply, parse_mode="HTML", reply_markup=keyboard)
