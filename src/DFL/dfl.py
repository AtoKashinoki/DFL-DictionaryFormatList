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
        "dimension", f"{dimension}"
    )
    tag = tag.replace(
        "index", f"{index}"
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
            create_tag(tag_format, dimension,0)
        ]

    # create dfl
    dfl_line: list = []
    recall_args_que: list[tuple] = []

    # list datas check
    for index, data in enumerate(list_):

        if type(data) is list:
            # create tag
            tag: str = create_tag(
                tag_format, dimension+1, index
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
        Create DFL format data from list.
    :param data: List data to manage.
    :param tag_format: DFL tag format.
    :return: DFL format list.
    """
    return create_dfl_recall(
        data, tag_format
    )


""" Create List from DFL format data """


def read_dlf(dlf: dict):
    pass


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
            tag_format: str = "#dimension#index#",
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
            tag_format: str = "#dimension#index#",
    ):
        """
            Initialize values and settings.
        :param data: List data to manage.
        :param tag_format: DFL tag format.
        """
        self.__data = self.create_dfl(data, tag_format)
        self.__tag = tag_format
        return

    def __repr__(self):
        return f"{self.__data}"
