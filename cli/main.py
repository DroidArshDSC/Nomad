import argparse
from pathlib import Path
from nomad.core.execution import analyze
from nomad.config.settings import Settings
from nomad.audit.log import AuditLogger

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["analyze"])
    parser.add_argument("repo", help="Path to repository")

    args = parser.parse_args()

    settings = Settings()
    audit = AuditLogger(Path(".nomad_audit"))

    if args.command == "analyze":
        result = analyze(Path(args.repo), settings)
        run_id = audit.write({
            "mode": "analyze",
            "result": result
        })
        print(f"Analyze complete. Run ID: {run_id}")
        print(result)

if __name__ == "__main__":
    main()
