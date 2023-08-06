from elefantolib_fastapi import exceptions
from elefantolib_fastapi.requests import Request

from fastapi import HTTPException, status


def request_depend(request: Request):
    try:
        request.pfm.validate()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def is_authenticated(request: Request):
    if not request.pfm.user.is_authenticated():
        raise exceptions.Unauthorized
