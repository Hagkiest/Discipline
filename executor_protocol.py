from typing import Protocol
from .http_types import HttpRequest

class RequestExecutor(Protocol):
    def execute(self, request: HttpRequest):
        ... 