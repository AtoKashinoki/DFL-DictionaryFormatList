"""
    DFL.file

This file contain management program of file.
"""


# import DFL class
from DFL.dfl import DFL

# import json
import json


""" Write DFL data in file"""


def write_dfls_in_file(
        *dfls: dict | DFL,
        path: str = "./None.dfl",
        encoding: str = "UTF-8",
) -> None:
    """
        Write DFL data in file.
    :param dfls: data to write.
    :param path: file position to write.
    :param encoding: text code.
    """
    dfls = list(dfls)

    for i, dfl in enumerate(dfls):
        if type(dfl) is DFL:
            dfls[i] = dfl.data
            ...
        continue

    with open(file=path, mode="w", encoding=encoding) as file:
        json.dump(dfls, file, indent=4)
        ...

    print(f" Success write dfl data in '{path}'")

    return


""" Read DFL data in file """


def read_dfls_in_file(
        path: str,
        encoding: str = "UTF-8",
) -> tuple[DFL, ...]:
    """
        Read DFL data in file.
    :param path: file position to read.
    :param encoding: text code.
    :return: DFL data.
    """

    with open(file=path, mode="r", encoding=encoding) as file:
        dfl_dicts: list[dict | DFL, ...] = json.load(file)
        ...

    dfls: list[DFL] = []
    for dfl_dict in dfl_dicts:
        dfl = DFL()
        dfl.data = dfl_dict
        dfls.append(dfl)
        continue

    return tuple(dfls)
