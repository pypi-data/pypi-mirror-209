from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class LogLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"

    def styled_string(self):
        style = self._style()
        return f"[{style}]{self.value:5}[/{style}]"

    def _style(self):
        return {
            LogLevel.DEBUG: "dim",
            LogLevel.INFO: "white",
            LogLevel.WARN: "bold yellow",
            LogLevel.ERROR: "bold red",
        }[self]


class JsonLog(BaseModel):
    source: str
    level: LogLevel
    message: str
    timestamp: datetime
    extra: dict

    @classmethod
    def fromDict(
        cls,
        *,
        source: str,
        level: LogLevel,
        message: str,
        timestamp: datetime | str,
        **kwargs,
    ) -> "JsonLog":
        return cls(
            source=source,
            level=level,
            message=message,
            timestamp=timestamp,
            extra=kwargs,
        )

    def __lt__(self, other: "JsonLog"):
        return self.timestamp < other.timestamp
