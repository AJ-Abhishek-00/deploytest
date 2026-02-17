from src.core.security.jwt import create_access_token, decode_token


def test_create_and_decode_token():

    token = create_access_token(
        {"user_id": 1}
    )

    payload = decode_token(token)

    assert payload["user_id"] == 1
