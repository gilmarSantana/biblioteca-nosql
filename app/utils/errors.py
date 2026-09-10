from fastapi import HTTPException


def raise_api_error(status_code: int, msg: str, code: str):
    raise HTTPException(
        status_code=status_code,
        detail={"status_code": status_code, "msg": msg, "code": code}
    )