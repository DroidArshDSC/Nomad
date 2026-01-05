from collections import Counter
from pathlib import Path
from nomad.git.repo_reader import RepoReader
from nomad.audit.log import AuditLogger
from nomad.config.settings import Settings

def analyze(repo_path: Path, settings: Settings) -> dict:
    reader = RepoReader(repo_path)
    files = reader.list_files()

    if len(files) > settings.max_files:
        raise RuntimeError("Repo too large to analyze safely")

    extensions = Counter(p.suffix for p in files)

    oversized = [
        str(p) for p in files
        if p.stat().st_size > settings.max_file_size_bytes
    ]

    return {
        "repo_path": str(repo_path),
        "file_count": len(files),
        "language_breakdown": dict(extensions),
        "oversized_files": oversized,
        "risk_flags": {
            "too_many_files": len(files) > settings.max_files,
            "large_files_present": len(oversized) > 0
        }
    }
