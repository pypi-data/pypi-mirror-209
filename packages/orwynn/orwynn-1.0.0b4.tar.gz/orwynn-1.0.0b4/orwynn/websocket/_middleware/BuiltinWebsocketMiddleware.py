from orwynn.websocket._middleware.WebsocketMiddleware import (
    WebsocketMiddleware,
)


class BuiltinWebsocketMiddleware(WebsocketMiddleware):
    """Special framework's middleware which covers all possible routes."""
    def __init__(self) -> None:
        # Cover all routes
        super().__init__(["*"])
