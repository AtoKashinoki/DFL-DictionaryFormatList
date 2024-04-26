import DFL
from DFL.dfl import (create_dfl, read_dfl)
from random import randrange


def create_random_list_recall(d_max=10, d=0) -> list:
    list_ = []
    for _ in range(randrange(1, 10)):
        num = randrange(14)
        if num > 9 and d < d_max:
            num = create_random_list_recall(d_max, d+1)
        list_.append(num)
    return list_


def create_tag(tag_format: str, dimension: int, index: int) -> str:
    """
        Create tag data.
    :param tag_format: DFL tag to use.
    :param dimension: dimension count.
    :param index: index count.
    :return: tag.
    """
    tag_format += "test"
    tag: str = tag_format.replace(
        "{dimension}", f"{dimension}"
    )
    tag = tag.replace(
        "{index}", f"{index}"
    )
    return tag


if __name__ == '__main__':
    data = create_random_list_recall()
    print(data)
    dfl = DFL.DFL(data, create_tag_function=create_tag)
    dfl[0] = "ts"
    dfl.data["#0#0#test"] = "bug"
    print(dfl, dfl.data)
    print(read_dfl(dfl, create_tag_function=create_tag))
