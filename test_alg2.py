import unittest
from alg2 import selection_sort, merge_sort
import random


class Test(unittest.TestCase):

    def test_selection(self):
        dimension = 100
        test_array = list(range(dimension))
        shuffled_array = test_array[:]
        random.shuffle(shuffled_array)
        shuffled_array, _, _ = selection_sort(shuffled_array)
        self.assertEqual(test_array, shuffled_array)

    def test_merge(self):
        dimension = 100
        test_array = list(range(dimension))
        shuffled_array = test_array[:]
        random.shuffle(shuffled_array)
        shuffled_array, _, _ = merge_sort(shuffled_array, 0, len(shuffled_array)-1)
        self.assertEqual(test_array, shuffled_array)


if __name__ == '__main__':
    unittest.main()
