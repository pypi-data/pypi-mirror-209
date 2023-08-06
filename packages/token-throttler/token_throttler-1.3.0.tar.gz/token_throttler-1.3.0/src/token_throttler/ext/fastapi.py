from typing import Callable, Optional

from fastapi import Depends, FastAPI, HTTPException, Request
from starlette import status

from ..token_throttler import TokenThrottler, TokenThrottlerException


class FastAPIThrottler:
    def __init__(self, throttler: TokenThrottler, exc: Optional[Exception] = None):
        self._throttler: TokenThrottler = throttler
        self._exc: Optional[Exception] = exc

    def enable(self, callback) -> Callable:
        def _dependency(identifier: str = Depends(callback)) -> None:
            if not self._throttler.consume(identifier=identifier):
                raise self._exc or HTTPException(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    detail=TokenThrottlerException().message,
                )

        return _dependency
