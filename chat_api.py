from flask import Blueprint, request, jsonify
from core.db import get_db_conn

bp_chat = Blueprint("chat", __name__, url_prefix="/api")


@bp_chat.get("/room/<room_id>/history")
def api_room_history(room_id):
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT author_name, author_id, text,
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


@bp_chat.post("/room/<room_id>/send")
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
