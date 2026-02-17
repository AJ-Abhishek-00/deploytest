import base64
import json
from datetime import datetime


def encode_cursor(created_at, id):

    cursor_dict = {
        "created_at": created_at.isoformat(),
        "id": id
    }

    cursor_str = json.dumps(cursor_dict)

    return base64.b64encode(cursor_str.encode()).decode()


def decode_cursor(cursor: str):

    decoded_bytes = base64.b64decode(cursor)

    decoded_str = decoded_bytes.decode()

    decoded_dict = json.loads(decoded_str)

    # CRITICAL FIX: convert string to datetime
    decoded_dict["created_at"] = datetime.fromisoformat(
        decoded_dict["created_at"]
    )

    return decoded_dict
