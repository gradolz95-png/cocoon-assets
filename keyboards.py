from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo


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
                    web_app=WebAppInfo(url="https://Gradolz.pythonanywhere.com/panel"),
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
