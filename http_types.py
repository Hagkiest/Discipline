from dataclasses import dataclass
from typing import Any, Dict, Optional, Literal

Method = Literal["GET", "POST"]

@dataclass(frozen=True)
class HttpRequest:
    method: Method
    url: str
    params: Optional[Dict[str, Any]] = None
    headers: Optional[Dict[str, str]] = None
    json: Optional[Any] = None
    timeout: Optional[float] = None 