import json
from datetime import datetime
from pathlib import Path
from uuid import uuid4

class AuditLogger:
    def __init__(self, log_dir: Path):
        self.log_dir = log_dir
        self.log_dir.mkdir(parents=True, exist_ok=True)

    def write(self, payload: dict) -> str:
        run_id = str(uuid4())
        payload["run_id"] = run_id
        payload["timestamp"] = datetime.utcnow().isoformat()

        path = self.log_dir / f"{run_id}.json"
        path.write_text(json.dumps(payload, indent=2))

        return run_id
