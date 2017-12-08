"""Bubble sort a list."""
import time
from random import randint


def insert_sort(list):
    """Bubble sort a list."""
    for i in range(len(list) - 1):
        sort = True
        while sort:
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                if i > 0:
                    i -= 1
                else:
                    sort = False
            else:
                sort = False
    return list


if __name__ == '__main__':
    print('\nCASE 1: A small list to be sorted:\n'
          '[45, 25, 80, 3, 6, 19, 400, 34]\n')
    start_simple = time.time()
    test = [45, 25, 80, 3, 6, 19, 400, 34]
    print(insert_sort(test))
    solve_simple = (time.time() - start_simple) * 100
    print('\nSorted using insert_sort() in {} seconds.'.format(solve_simple))

    print('\nCASE 2: A list of 100 numbers:\n')
    hundred = [randint(1, 100000) for x in range(100)]
    print(test)
    start_hundred = time.time()
    print(insert_sort(hundred))
    solve_hundred = (time.time() - start_hundred) * 100
    print('\nSorted using insert_sort() in {} seconds.'.format(solve_hundred))

    print('\nCASE 3: A list of 1,000 random numbers:')
    thousand = [randint(1, 100000) for x in range(1000)]
    print(thousand)
    start_thousand = time.time()
    print(insert_sort(thousand))
    solve_thousand = (time.time() - start_thousand) * 100
    print('\nSorted using insert_sort() {} seconds'.format(solve_thousand))

    print('\nCASE 4: A list of 10,000 numbers (not shown):\n')
    ten = [randint(1, 100000) for x in range(10000)]
    start_ten = time.time()
    print(insert_sort(ten))
    solve_ten = (time.time() - start_ten) * 100
    print('\nSorted using insert_sort() in {} seconds.'.format(solve_ten))

    print('\nCASE 5: A list of 100,000 words:\n')
    mil = [randint(1, 100000) for x in range(100000)]
    start_mil = time.time()
    print(insert_sort(mil))
    solve_mil = (time.time() - start_mil) * 100
    print('\nSorted using insert_sort() in {} seconds.'.format(solve_mil))
