"""
    DFL.DFL

This file contains DFL class.
"""

# import descriptor
from Descriptors import (
    DataType,
)

# import types


""" Create DFL format data from list """


def create_tag(tag_format, dimension, index) -> str:
    """
        Create tag data.
    :param tag_format: DFL tag to use.
    :param dimension: dimension count.
    :param index: index count.
    :return: tag.
    """
    tag: str = tag_format.replace(
        "{dimension}", f"{dimension}"
    )
    tag = tag.replace(
        "{index}", f"{index}"
    )
    return tag


def create_dfl_recall(
        list_: list,
        tag_format: str,
        dfl: dict = None,
        tag_log: list = None,
        dimension: int = 0,
) -> dict[str, any]:
    """
        Create DFL format from list recall function.
    :param list_: List data to change.
    :param tag_format: DFL tag to use.
    :param dfl: [Recall] Output data.
    :param tag_log: [Recall] self tag.
    :param dimension: [Recall] Dimension count.
    :return: DFL format dict.
    """
    # initialize dfl
    if dfl is None:
        dfl = {"tag_format": tag_format}

    # initialize tag_log
    if tag_log is None:
        tag_log = [
            create_tag(tag_format, dimension, 0)
        ]

    # create dfl
    dfl_line: list = []
    recall_args_que: list[tuple] = []

    # list datas check
    for index, data in enumerate(list_):

        if type(data) is list:
            # create tag
            tag: str = create_tag(
                tag_format, dimension + 1, index
            )

            for i in range(dimension):
                if tag not in dfl.keys():
                    break

                tag = tag_log[-i - 1] + tag
                continue

            recall_args_que.append(
                (data, tag)
            )
            data = tag

        dfl_line.append(data)
        continue

    # register dfl_line
    dfl[tag_log[-1]] = dfl_line

    # recall process
    for data, tag in recall_args_que:
        dfl = create_dfl_recall(
            data,
            tag_format,
            dfl,
            tag_log + [tag],
            dimension + 1,
        )

    return dfl


def create_dfl(
        data: list,
        tag_format: str = "#{dimension}#{index}#",
) -> dict[str, any]:
    """
        Create DFL format dictionary data from list.
    :param data: List data to manage.
    :param tag_format: DFL tag format.
    :return: DFL format list.
    """
    return create_dfl_recall(
        data, tag_format
    )


""" Create List from DFL format data """


def replace_all(value: str, __olds: tuple[str, ...], __new: str) -> str:
    """
        Execute replace all.
    :param value: string data to change.
    :param __olds: olds strings to change.
    :param __new: new string.
    :return: string
    """
    for old in __olds:
        value = value.replace(f"{old}", f"{__new}")
    return value


def remove_number(value: str) -> str:
    """
        Create string object not in numbers.
    :param value: string data to remove numbers.
    :return: string object.
    """
    return replace_all(value, tuple(range(10)), "")


def read_dlf_recall(dlf: dict, self_tag: str, tag_key: str) -> list:
    """
        Create list from DLF format dictionary recall function.
    :param dlf: DLF data to change.
    :param self_tag: [recall]self tag.
    :param tag_key: validate tag key.
    :return: list format data.
    """
    return_list: list = []

    for value in dlf[self_tag]:

        if (
                type(value) is str and
                remove_number(value)[-len(tag_key):] == tag_key
        ):
            value = read_dlf_recall(dlf, value, tag_key)

        return_list.append(value)

    return return_list


def read_dlf(dlf: dict) -> list:
    """
        Create list  from DLF format dictionary.
    :param dlf: DLF data to change.
    :return: list format data.
    """
    tag_format = dlf["tag_format"]
    self_tag = replace_all(
        tag_format,
        ("{dimension}", "{index}"), "0"
    )
    tag_key = replace_all(
        tag_format,
        ("{dimension}", "{index}"), ""
    )
    return read_dlf_recall(
        dlf, self_tag, tag_key
    )


""" DFL-DictionaryFormatList """


class DFL:
    """
        DictionaryFormatList

    This class manage DFL format data.
    """

    # variables
    __data: dict = DataType(dict)
    __tag: str = DataType(str)

    # constants

    @staticmethod
    def create_dfl(
            data: list,
            tag_format: str = "#{dimension}#{index}#",
    ) -> dict[str, any]:
        """
            Create DFL format data from list.
        :param data: List data to manage.
        :param tag_format: DFL tag format.
        :return: DFL format list.
        """
        return create_dfl(data, tag_format)

    def __init__(
            self,
            data: list = (),
            tag_format: str = "#{dimension}#{index}#",
    ):
        """
            Initialize values and settings.
        :param data: List data to manage.
        :param tag_format: DFL tag format.
        """
        self.__data = self.create_dfl(data, tag_format)
        return

    def __repr__(self):
        return f"{self.__data}"

    @property
    def data(self):
        """ Return DFL format dictionary data """
        return self.__data

    @property
    def tag(self):
        """ Return DFL data tag """
        return self.__data["tag_format"]

    @property
    def get_list(self):
        """ Create and Return list format data from self DFL"""
        return read_dlf(self.__data)
