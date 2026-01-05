from pathlib import Path
from typing import List

class RepoReader:
    def __init__(self, repo_path: Path):
        if not repo_path.exists() or not repo_path.is_dir():
            raise ValueError("Invalid repository path")
        self.repo_path = repo_path

    def list_files(self) -> List[Path]:
        return [
            p for p in self.repo_path.rglob("*")
            if p.is_file() and ".git" not in p.parts
        ]
