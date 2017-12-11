"""Function to run a bubble sort on a given list of numbers."""
import time
from random import randint


def bubble_sort(list):
    """Bubble sort function."""
    global looped
    looped = 1
    for i in range(len(list) - looped):
        if list[i] > list[i + 1]:
            list[i], list[i + 1] = list[i + 1], list[i]
        else:
            continue  # pragma: no cover
        looped += 1
        bubble_sort(list)
    return list

if __name__ == '__main__':

    short_list = [randint(1, 50) for _ in range(10)]
    print('\nCASE 1: A small list to be sorted:\n', short_list)
    short_list = timeit.timeit("bubble_sort(short_list)", setup="from __main__ import short_list, bubble_sort")
    print('Short list time: ', short_list)

    print('\nCASE 2: A list of 100 numbers:\n')
    hundred = [randint(1, 100000) for x in range(100)]
    start_hundred = time.time()
    solve_hundred = (time.time() - start_hundred) * 1000
    print(bubble_sort(hundred))
    print('\nSorted using bubble_sort() in {} seconds.'.format(solve_hundred))

    print('\nCASE 3: A list of 1,000 random numbers:')
    thousand = [randint(1, 100000) for x in range(1000)]
    start_thousand = time.time()
    solve_thousand = (time.time() - start_thousand) * 1000
    print(thousand)
    print(bubble_sort(thousand))
    print('\nSorted using bubble_sort() {} seconds'.format(solve_thousand))

    print('\nCASE 4: A list of 10,000 numbers (not shown):\n')
    ten = [randint(1, 100000) for x in range(10000)]
    start_ten = time.time()
    solve_ten = (time.time() - start_ten) * 1000
    print(bubble_sort(ten))
    print('\nSorted using bubble_sort() in {} seconds.'.format(solve_ten))

    print('\nCASE 5: A list of 100,000 words:\n')
    mil = [randint(1, 100000) for x in range(100000)]
    start_mil = time.time()
    solve_mil = (time.time() - start_mil) * 1000
    print(bubble_sort(mil))
    print('\nSorted using bubble_sort() in {} seconds.'.format(solve_mil))
