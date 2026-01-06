import argparse
from pathlib import Path
from nomad.core.execution import analyze
from nomad.config.settings import Settings
from nomad.audit.log import AuditLogger
from nomad.core.guards import assert_can_execute, GuardViolation
from nomad.audit.state import RunState
from nomad.core.errors import NomadError, ErrorCode


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["analyze"])
    parser.add_argument("repo", help="Path to repository")

    args = parser.parse_args()

    state = RunState(Path(".nomad_state"))
    last_run = state.load()

    try:
        assert_can_execute(args.command, last_run)

        if args.command == "analyze":
            settings = Settings()
            audit = AuditLogger(Path(".nomad_audit"))

            result = analyze(Path(args.repo), settings)

            run_id = audit.write({
                "mode": "analyze",
                "result": result
            })

            state.save(mode="analyze", status="success")

            print(f"Analyze complete. Run ID: {run_id}")
            print(result)

    except GuardViolation as e:
        print(f"ERROR: {e}")
        state.save(mode=args.command, status="failed")

    except Exception as e:
        print(f"ANALYZE FAILED: {e}")
        state.save(mode=args.command, status="failed")

    except NomadError as e:
        print(str(e))
        state.save(mode=args.command, status="failed")

    except Exception as e:
        print(NomadError(code=ErrorCode.INTERNAL_ERROR,message="Unexpected internal error",hint="Please report this issue"))
        state.save(mode=args.command, status="failed")

if __name__ == "__main__":
    main()
