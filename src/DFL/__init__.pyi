

def create_tag(
        tag_format: str,
        dimension: int | str,
        index: int | str,
) -> str: ...


class DFL:
    __data: dict
    __create_tag = create_tag


    @staticmethod
    def create_dfl(
            data: list,
            tag_format: str = "#{dimension}#{index}#",
            create_tag_function=create_tag,
    ) -> dict[str, any]: ...


    def __init__(
            self,
            data: list = (),
            tag_format: str = "#{dimension}#{index}#",
            create_tag_function=create_tag,
    ): ...


    def __repr__(self): ...
    @property
    def data(self) -> dict: ...
    @data.setter
    def data(self, dfl_dict: dict) -> None: ...
    @property
    def tag(self) -> str: ...
    @property
    def first_tag(self) -> str: ...
    def get_list(self) -> list: ...
    @property
    def list(self) -> list: ...
    def __getitem__(self, index: int): ...
    def __setitem__(self, index: int, value): ...
    def del_values(self, key) -> None: ...
    def __eq__(self, other): ...


def encode_dfl(
        data: list,
        tag_format: str = "#{dimension}#{index}#",
        create_tag_function=create_tag,
) -> dict[str, any]: ...


def decode_dfl(
        dfl: dict | DFL,
        create_tag_function=create_tag,
) -> list: ...


def write_dfls_in_file(
        *dfls: dict | DFL,
        path: str = "./None.dfl",
        encoding: str = "UTF-8",
) -> None: ...


def read_dfls_in_file(
        path: str,
        encoding: str = "UTF-8",
) -> tuple[DFL, ...]: ...