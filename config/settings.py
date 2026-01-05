from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Settings:
    max_files: int = 10_000
    max_file_size_bytes: int = 2_000_000  # 2 MB
    temp_root: Path = Path("/tmp/nomad")
