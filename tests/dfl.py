import DFL
from random import randrange


def create_random_list_recall(d_max = 10, d=0) -> list:
    list_ = []
    for _ in range(randrange(9)):
        num = randrange(14)
        if num > 9 and d < d_max:
            num = create_random_list_recall(d_max, d+1)
        list_.append(num)
    return list_


if __name__ == '__main__':
    data = create_random_list_recall()
    dfl = DFL.DFL(data)
    print(dfl)

