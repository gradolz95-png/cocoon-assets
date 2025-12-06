import asyncio

from flask import Flask, request, jsonify
from aiogram.types import Update
from aiogram import Bot
from aiogram.client.session.aiohttp import AiohttpSession

from core.db import init_db, get_db_conn
from core.config import BOT_TOKEN
from web.panel_html import PANEL_HTML
from bot import create_dispatcher


# --------------------------------------------------
# Flask-приложение
# --------------------------------------------------
app = Flask(__name__)


# --------------------------------------------------
# TON Connect manifest
# --------------------------------------------------
@app.route("/tonconnect-manifest.json")
def tonconnect_manifest():
    manifest = {
        "url": "https://gradolz.pythonanywhere.com",
        "name": "Cocoon",
        "iconUrl": "https://raw.githubusercontent.com/gradolz95-png/cocoon-assets/main/000025_1764570763_751668_big-no-bg-preview%20(carve.photos)%20(2).png",
    }
    response = jsonify(manifest)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


# --------------------------------------------------
# БД и aiogram
# --------------------------------------------------
init_db()
dp = create_dispatcher()


async def process_update(update_json: dict):
    """Обработка апдейта aiogram-ом."""
    update = Update.model_validate(update_json)

    session = AiohttpSession()
    bot = Bot(token=BOT_TOKEN, session=session)
    try:
        await dp.feed_update(bot, update)
    finally:
        await bot.session.close()


# --------------------------------------------------
# Webhook бота
# --------------------------------------------------
@app.route("/webhook", methods=["POST"])
def webhook():
    update_json = request.get_json(force=True)
    asyncio.run(process_update(update_json))
    return "OK", 200


# --------------------------------------------------
# WebApp панель
# --------------------------------------------------
@app.route("/", methods=["GET"])
def index():
    # главная страница — панель Cocoon
    return PANEL_HTML


@app.route("/panel", methods=["GET"])
def panel():
    # дублирующий роут, если где-то уже используется /panel
    return PANEL_HTML


# --------------------------------------------------
# API для чата
# --------------------------------------------------
@app.route("/api/room/<room_id>/history", methods=["GET"])
def api_room_history(room_id):
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT author_name,
               author_id,
               text,
               strftime('%H:%M', created_at) AS time
        FROM chat_messages
        WHERE room_id = ?
        ORDER BY id ASC
        LIMIT 100
        """,
        (room_id,),
    )
    rows = cur.fetchall()
    conn.close()
    messages = [
        {
            "author_name": row["author_name"],
            "author_id": row["author_id"],
            "text": row["text"],
            "time": row["time"],
        }
        for row in rows
    ]
    return jsonify({"messages": messages})


@app.route("/api/room/<room_id>/send", methods=["POST"])
def api_room_send(room_id):
    data = request.get_json(force=True) or {}
    text = (data.get("text") or "").strip()
    author_name = (data.get("author_name") or "")[:64]
    author_id = str(data.get("author_id") or "")

    if not text:
        return jsonify({"ok": False, "error": "EMPTY"}), 400

    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO chat_messages (room_id, author_name, author_id, text)
        VALUES (?, ?, ?, ?)
        """,
        (room_id, author_name, author_id, text),
    )
    conn.commit()
    conn.close()
    return jsonify({"ok": True})
