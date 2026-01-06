from enum import Enum
from dataclasses import dataclass

class ErrorCode(str, Enum):
    GUARD_VIOLATION = "GUARD_VIOLATION"
    SAFETY_VIOLATION = "SAFETY_VIOLATION"
    UNSUPPORTED = "UNSUPPORTED"
    INTERNAL_ERROR = "INTERNAL_ERROR"


@dataclass
class NomadError(Exception):
    code: ErrorCode
    message: str
    hint: str | None = None

    def __str__(self):
        base = f"[{self.code}] {self.message}"
        if self.hint:
            return f"{base}\nHint: {self.hint}"
        return base
