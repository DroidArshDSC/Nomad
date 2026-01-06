import json
from pathlib import Path
from typing import Optional

STATE_FILE = "last_run.json"

class RunState:
    def __init__(self, state_dir: Path):
        self.state_dir = state_dir
        self.state_dir.mkdir(parents=True, exist_ok=True)
        self.path = self.state_dir / STATE_FILE

    def load(self) -> Optional[dict]:
        if not self.path.exists():
            return None
        return json.loads(self.path.read_text())

    def save(self, mode: str, status: str):
        payload = {
            "mode": mode,
            "status": status
        }
        self.path.write_text(json.dumps(payload, indent=2))
