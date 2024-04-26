from DFL.dfl import DFL
from DFL.file import (
    write_dfls_in_file, read_dfls_in_file
)
from random import randrange


def create_random_list_recall(d_max=10, d=0) -> list:
    list_ = []
    for _ in range(randrange(1, 10)):
        num = randrange(14)
        if num > 9 and d < d_max:
            num = create_random_list_recall(d_max, d+1)
        list_.append(num)
    return list_


if __name__ == '__main__':
    dfls = [
        DFL(create_random_list_recall())
        for _ in range(100)
    ]
    path = "tests/dfl_test.dfl"
    before = dfls
    write_dfls_in_file(*dfls, path=path)
    after = read_dfls_in_file(path)
    print(before, after, sep="\n", end="\n\n")
    count: list = [0, 0]
    for b, a in zip(before, after):
        if b == a:
            count[0] += 1
        else:
            count[1] += 1
        continue
    print("True: {}, False: {}".format(*count))
    ...
