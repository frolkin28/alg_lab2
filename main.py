from alg2 import merge_sort, selection_sort
import random
import time


def main():
    dims = [10]
    for dim in dims:
        test_array = list(range(dim))
        shuffled_array = test_array[:]
        random.shuffle(shuffled_array)
        # print(shuffled_array)
        start_time = time.time()
        # a, comps, swaps = merge_sort(shuffled_array, 0 ,len(shuffled_array)-1)
        a, comps, swaps = merge_sort(shuffled_array, 0, len(shuffled_array)-1)
        print(time.time() - start_time)
        print('Comparisons={} | Swaps={}'.format(comps, swaps))

if __name__ == '__main__':
    main()
