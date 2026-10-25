from app.core.security import (
    create_access_token,
    decode_access_token,
    hash_password,
    verify_password,
)


def test_password_hashing():
    password = "test-password-123"
    hashed = hash_password(password)

    assert hashed != password
    assert verify_password(password, hashed)
    assert not verify_password("wrong-password", hashed)


def test_access_token():
    token = create_access_token(user_id=123)
    payload = decode_access_token(token)

    assert payload["sub"] == "123"
    assert "exp" in payload