from litestar import Litestar, get, Request
from litestar.events import listener

import logging

logger = logging.getLogger(__name__)

@listener("raise_exception")
async def raise_exception_if_odd(value) -> None:
    """Raise an exception to test Emit error."""
    if value is not None and value % 2 != 0:
        raise ValueError(f"{value} is odd")
    else:
        return "The value is even. No exception raised."

@get("/")
async def index() -> str:
    return "Hello, world!"

@get("/check-value/{value:int}")
async def check_value(request: Request, value: int) -> str:
    try:
        request.app.emit("raise_exception", value)
        return f"Checked {value}: No exception raised."
    except ValueError as e:
        return str(e)

app = Litestar([index, check_value], listeners=[raise_exception_if_odd])
