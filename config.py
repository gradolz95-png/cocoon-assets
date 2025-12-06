from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

BOT_TOKEN = "8586981594:AAHVx-UMmRmZi8cZkn7lulR80HBMiuAI67U"
ADMIN_ID = 6925491305

# новая база в отдельной папке data
DB_PATH = str(BASE_DIR / "data" / "cocoon_chat.db")

DECRYPT_TTL = 600

