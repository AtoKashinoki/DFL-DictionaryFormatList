import DFL
from DFL.dfl import (create_dfl, read_dlf)
from random import randrange


def create_random_list_recall(d_max=10, d=0) -> list:
    list_ = []
    for _ in range(randrange(9)):
        num = randrange(14)
        if num > 9 and d < d_max:
            num = create_random_list_recall(d_max, d+1)
        list_.append(num)
    return list_


if __name__ == '__main__':
    data = create_random_list_recall()
    print(data)
    dfl = DFL.DFL(data)
    print(dfl)
    print(dfl.get_list)
