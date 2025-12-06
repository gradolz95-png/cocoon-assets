import secrets
from datetime import datetime, timedelta
from typing import Dict, Tuple

from cryptography.fernet import Fernet


_user_keys: Dict[int, bytes] = {}
_decrypt_storage: Dict[str, Tuple[str, datetime]] = {}


def get_cipher(user_id: int) -> Fernet:
    if user_id not in _user_keys:
        _user_keys[user_id] = Fernet.generate_key()
    return Fernet(_user_keys[user_id])


def generate_decrypt_id() -> str:
    return secrets.token_hex(8)


def put_decrypt_text(text: str, ttl_seconds: int) -> str:
    decrypt_id = generate_decrypt_id()
    expires_at = datetime.utcnow() + timedelta(seconds=ttl_seconds)
    _decrypt_storage[decrypt_id] = (text, expires_at)
    return decrypt_id


def pop_decrypt_text(decrypt_id: str) -> str | None:
    item = _decrypt_storage.get(decrypt_id)
    if not item:
        return None
    text, expires_at = item
    if datetime.utcnow() > expires_at:
        del _decrypt_storage[decrypt_id]
        return None
    del _decrypt_storage[decrypt_id]
    return text
