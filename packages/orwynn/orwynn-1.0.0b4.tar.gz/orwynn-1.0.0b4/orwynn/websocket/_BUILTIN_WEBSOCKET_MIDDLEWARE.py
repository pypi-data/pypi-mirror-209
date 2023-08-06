from orwynn.websocket._middleware.ConnectionBuiltinWebsocketMiddleware import (
    ConnectionBuiltinWebsocketMiddleware,
)

from ._context.ContextBuiltinWebsocketMiddleware import (
    ContextBuiltinWebsocketMiddleware,
)
from ._context.RequestContextBuiltinWebsocketMiddleware import (
    RequestContextBuiltinWebsocketMiddleware,
)
from ._errorhandler.ErrorHandlerWebsocketMiddleware import (
    ErrorHandlerWebsocketMiddleware,
)
from ._middleware.BuiltinWebsocketMiddleware import BuiltinWebsocketMiddleware

BUILTIN_WEBSOCKET_MIDDLEWARE: list[type[BuiltinWebsocketMiddleware]] = [
    # Connection middleware should be first, since the exception handlers will
    # access websocket object
    ConnectionBuiltinWebsocketMiddleware,
    ContextBuiltinWebsocketMiddleware,
    ErrorHandlerWebsocketMiddleware,
    RequestContextBuiltinWebsocketMiddleware
]
