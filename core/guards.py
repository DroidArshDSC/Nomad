from nomad.core.errors import NomadError, ErrorCode

def assert_can_execute(requested_mode: str, last_run: dict | None):
    if requested_mode == "analyze":
        return  # always allowed

    if last_run is None:
        raise NomadError(
            code=ErrorCode.GUARD_VIOLATION,
            message=f"{requested_mode} blocked: no prior analyze run",
            hint="Run `nomad analyze <repo>` first"
        )

    if requested_mode == "plan":
        if last_run["mode"] != "analyze" or last_run["status"] != "success":
            raise NomadError(
                code=ErrorCode.GUARD_VIOLATION,
                message="plan blocked: analyze not completed successfully",
                hint="Re-run analyze and ensure it completes without errors"
            )

    if requested_mode == "apply":
        if last_run["mode"] != "plan" or last_run["status"] != "success":
            raise NomadError(
                code=ErrorCode.GUARD_VIOLATION,
                message="apply blocked: plan not completed successfully",
                hint="Run `nomad plan` first"
            )
