from typing import Any

def pymeos_initialize(
    timezone: str | None = None,
    date_style: None | str | tuple[str, Any] = None,
    interval_style: None | str | tuple[str, int] = None,
) -> None: ...
def pymeos_finalize() -> None: ...
