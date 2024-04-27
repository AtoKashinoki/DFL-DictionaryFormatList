"""
    DFL.file

This file contain management program of file.
"""


# import DFL class
from DFL.dfl import DFL
from DFL.dfl import encode_dfl

# import json
import json


""" Write DFL data in file"""


def write_dfls_in_file(
        *datas: dict | DFL | list,
        path: str = "./None.dfl",
        encoding: str = "UTF-8",
) -> None:
    """
        Write DFL data in file.
    :param datas: data to write.
    :param path: file position to write.
    :param encoding: text code.
    """
    datas = list(datas)

    for i, dfl in enumerate(datas):
        if type(dfl) is DFL:
            datas[i] = dfl.data
            ...
        elif type(dfl) is list:
            dfl[i] = encode_dfl(dfl)
        continue

    with open(file=path, mode="w", encoding=encoding) as file:
        json.dump(datas, file, indent=4)
        ...

    print(f" Success write dfl data in '{path}'")

    return


""" Read DFL data in file """


def read_dfls_in_file(
        path: str,
        encoding: str = "UTF-8",
) -> tuple[DFL, ...] | DFL:
    """
        Read DFL data in file.
    :param path: file position to read.
    :param encoding: text code.
    :return: DFL data.
    """

    with open(file=path, mode="r", encoding=encoding) as file:
        dfl_dicts: list[dict | DFL, ...] | dict | DFL = json.load(file)
        ...

    if not type(dfl_dicts) is list:
        dfl = DFL()
        dfl.data = dfl_dicts
        return dfl

    dfls: list[DFL] = []
    for dfl_dict in dfl_dicts:
        dfl = DFL()
        dfl.data = dfl_dict
        dfls.append(dfl)
        continue

    return tuple(dfls)
