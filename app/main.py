def format_linter_error(error: dict) -> dict:
    return {error['line']: error['column']}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return dict(path=str(file_path), status="failed" if errors else "passed",
                errors=[format_linter_error(error) for error in errors])


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(file["path"], file["errors"]) for file in linter_report]
