
from DFL.dfl import DFL


def write_dfls_in_file(
        *dfls: dict | DFL,
        path: str = "./None.dfl",
        encoding: str = "UTF-8",
) -> None: ...


def read_dfls_in_file(
        path: str,
        encoding: str = "UTF-8",
) -> tuple[DFL, ...]: ...
