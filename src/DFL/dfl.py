"""
    DFL.DFL

This file contains DFL class.
"""

# import copy
import copy

# import descriptor
from Descriptors import (
    DataType,
)


""" Create tag data """


def create_tag(
        tag_format: str,
        dimension: int | str,
        index: int | str,
) -> str:
    """
        Insert datas in dimension and index.
    :param tag_format: tag format to insert.
    :param dimension: dimension number.
    :param index: index number.
    :return: DFL tag.
    """
    value: str = tag_format
    for old, new in zip(
            ("{dimension}", "{index}"),
            (f"{dimension}", f"{index}"),
    ):
        value = value.replace(old, new)
        continue
    return value


""" DFL-DictionaryFormatList """


class DFL:
    """
        DictionaryFormatList

    This class manage DFL format data.
    """

    # variables
    __data: dict = DataType(dict)
    __create_tag = create_tag

    # constants

    @staticmethod
    def create_dfl(
            data: list,
            tag_format: str = "#{dimension}#{index}#",
            create_tag_function=create_tag,
    ) -> dict[str, any]:
        """
            Create DFL format data from list.
        :param data: List data to manage.
        :param tag_format: DFL tag format.
        :param create_tag_function: create tag function.
        :return: DFL format list.
        """
        return encode_dfl(
            data,
            tag_format,
            create_tag_function=create_tag_function
        )

    def __init__(
            self,
            data: list | dict = (),
            tag_format: str = "#{dimension}#{index}#",
            create_tag_function=create_tag,
    ):
        """
            Initialize values and settings.
        :param data: List data to manage.
        :param tag_format: DFL tag format.
        """
        if type(data) is dict and "tag_format" in data.keys():
            self.__data = data
            ...
        elif type(data) is list:
            self.__data = self.create_dfl(
                data,
                tag_format,
                create_tag_function=create_tag_function
            )
            ...
        else:
            raise TypeError(
                f"TypeError: Failed to convert data to DFL format -> "
                f"{data}({type(data)})"
            )
        self.__create_tag = create_tag_function
        return

    def __repr__(self):
        return f"{self.__data[self.first_tag]}"

    @property
    def data(self) -> dict:
        """ Return DFL format dictionary data """
        return copy.copy(self.__data)

    @property
    def tag(self) -> str:
        """ Return DFL data tag """
        return self.__data["tag_format"]

    @property
    def first_tag(self) -> str:
        """ Return DFL data first tag """
        return self.__create_tag(
            self.tag, 0, 0
        )

    def get_list(self) -> list:
        """ Create and Return list format data from self DFL"""
        return decode_dfl(self.__data, self.__create_tag)

    @property
    def list(self) -> list:
        """ Create and Return list format data from self DFL"""
        return self.get_list()

    def __getitem__(self, index: int) -> list:
        """
            Get values from self.
        :param index: data position.
        :return: list
        """
        tag = self.first_tag
        value = self.__data[tag][index]
        if validate_tag(value, self.tag):
            value = DFLValues(value, self)
            ...
        return value

    def __setitem__(self, index: int, value) -> None:
        """
            Set value in self.
        :param index: position to set.
        :param value: data to set.
        """
        tag = self.first_tag
        pre_value = self.__data[tag][index]
        if validate_tag(pre_value, self.tag):
            self.del_values(pre_value)
            ...
        self.__data[tag][index] = value
        return

    def del_values(self, key) -> None:
        """
            Delete values.
        :param key: tag key to delete.
        """

        for value in copy.deepcopy(self.__data[key]):
            if validate_tag(value, self.tag):
                self.del_values(value)
                ...
            continue

        del self.__data[key]
        return

    def __eq__(self, other) -> bool:
        """ Validate self and other """
        if type(other) is DFL:
            other = other.data
            ...

        return self.data == other

    def __iter__(self):
        """ Return iterator of list """
        return iter(self.list)

    ...


class DFLValues(list):
    """
        DFL values list

    This class is DFL get data list.
    """
    __dfl = DataType(DFL)
    __tag = DataType(str)

    def __init__(self, tag: str, dfl: DFL):
        self.__dfl = dfl
        self.__tag = tag
        super().__init__(dfl.data[tag])
        return

    def __getitem__(self, index: int):
        value = list.__getitem__(self, index)
        if validate_tag(value, self.__dfl.tag):
            value = DFLValues(value, self.__dfl)
            ...
        return value

    def __setitem__(self, index, value):
        pre_value = list.__getitem__(self, index)
        if validate_tag(pre_value, self.__dfl.tag):
            self.__dfl.del_values(pre_value)
            ...
        self.__dfl.data[self.__tag][index] = value
        return


""" Encode DFL format data """


def encode_dfl_recall(
        list_: list,
        tag_format: str,
        dfl: dict = None,
        tag_log: list = None,
        dimension: int = 0,
        create_tag_function=create_tag,
) -> dict[str, any]:
    """
        Encode DFL format from list recall function.
    :param list_: List data to change.
    :param tag_format: DFL tag to use.
    :param dfl: [Recall] Output data.
    :param tag_log: [Recall] self tag.
    :param dimension: [Recall] Dimension count.
    :param create_tag_function: create tag function.
    :return: DFL format dict.
    """
    # initialize dfl
    if dfl is None:
        dfl = {"tag_format": tag_format}
        ...

    # initialize tag_log
    if tag_log is None:
        tag_log = [
            create_tag_function(tag_format, dimension, 0)
        ]
        ...

    # encode dfl
    dfl_line: list = []
    recall_args_que: list[tuple] = []

    # list datas check
    for index, data in enumerate(list_):

        if type(data) is list:
            # create tag
            tag: str = create_tag_function(
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
            ...

        dfl_line.append(data)
        continue

    # register dfl_line
    dfl[tag_log[-1]] = dfl_line

    # recall process
    for data, tag in recall_args_que:
        dfl = encode_dfl_recall(
            data,
            tag_format,
            dfl,
            tag_log + [tag],
            dimension + 1,
            create_tag_function,
        )
        continue

    return dfl


def encode_dfl(
        data: list,
        tag_format: str = "#{dimension}#{index}#",
        create_tag_function=create_tag,
) -> dict[str, any]:
    """
        Encode DFL format dictionary data from list.
    :param data: List data to manage.
    :param tag_format: DFL tag format.
    :param create_tag_function: create tag function.
    :return: DFL format list.
    """
    return encode_dfl_recall(
        data, tag_format, create_tag_function=create_tag_function,
    )


""" Decode DFL format data """


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
        continue
    return value


def remove_number(value: str) -> str:
    """
        Create string object not in numbers.
    :param value: string data to remove numbers.
    :return: string object.
    """
    return replace_all(value, tuple(range(10)), "")


def validate_tag(
        value,
        tag_format: str | None,
        tag_key: str = None
) -> bool:
    """
        Validate tag.
    :param value: tag to validate.
    :param tag_format: tag format.
    :param tag_key: tag key
    :return: bool
    """
    if tag_key is None:
        tag_key = create_tag(
            tag_format, "", ""
        )
        ...
    return (
            type(value) is str and
            remove_number(value)[-len(tag_key):] == tag_key
    )


def decode_dfl_recall(dfl: dict, self_tag: str, tag_key: str) -> list:
    """
        Decode list from DFL format dictionary recall function.
    :param dfl: DFL data to change.
    :param self_tag: [recall]self tag.
    :param tag_key: validate tag key.
    :return: list format data.
    """
    return_list: list = []

    for value in dfl[self_tag]:

        if validate_tag(value, None, tag_key):
            value = decode_dfl_recall(dfl, value, tag_key)
            ...

        return_list.append(value)

        continue

    return return_list


def decode_dfl(
        dfl: dict | DFL,
        create_tag_function=create_tag
) -> list:
    """
        Create list  from DFL format dictionary.
    :param dfl: DFL data to change.
    :param create_tag_function: create tag function.
    :return: list format data.
    """
    if type(dfl) is DFL:
        dfl = dfl.data
        ...

    tag_format = dfl["tag_format"]
    self_tag = create_tag_function(
        tag_format, "0", "0"
    )
    tag_key = create_tag_function(
        tag_format, "", ""
    )
    return decode_dfl_recall(
        dfl, self_tag, tag_key
    )
