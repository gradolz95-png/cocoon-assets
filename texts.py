from datetime import datetime
from typing import Set

start_time = datetime.utcnow()
total_messages: int = 0
total_encrypts: int = 0
unique_users: Set[int] = set()


WELCOME_TEXT = (
    "👋 Привет!\n\n"
    "Я <b>Cocoon</b> — лёгкий бот в стиле TON.\n"
    "Заворачиваю твой текст в шифрованный кокон.\n\n"
    "Нажми «🔒 Проверить приватность» и отправь любое сообщение 😌"
)

PRIVACY_TEXT = (
    "🔐 <b>Приватность Cocoon x TON</b>\n\n"
    "• У каждого пользователя свой шифровальный слой\n"
    "• Ключи только в памяти узла\n"
    "• Веб-панель шифрует локально\n"
    "• Чат работает через скрытые комнаты\n\n"
    "Минимализм и прозрачность 🔵"
)

ABOUT_TEXT = (
    "🤍 <b>Cocoon</b>\n\n"
    "Минималистичный бот про приватность.\n"
    "Лёгкое шифрование, скрытые чаты, WebApp панель.\n"
)


def update_stats(user_id: int, is_encrypt: bool = False) -> None:
    global total_messages, total_encrypts
    total_messages += 1
    unique_users.add(user_id)
    if is_encrypt:
        total_encrypts += 1


def format_stats() -> str:
    uptime = datetime.utcnow() - start_time
    hours, remainder = divmod(int(uptime.total_seconds()), 3600)
    minutes, _ = divmod(remainder, 60)
    return (
        "📊 <b>Статистика Cocoon</b>\n\n"
        f"⏱ Аптайм: {hours} ч {minutes} мин\n"
        f"👥 Уникальных пользователей: {len(unique_users)}\n"
        f"💬 Сообщений обработано: {total_messages}\n"
        f"🔒 Шифрований: {total_encrypts}\n"
    )
