def selection_sort(array):
    i, size = 0, len(array)
    comps, swaps = 0, 0
    while i < size:
        min_i, j = i, i + 1

        while j < size:
            comps += 1
            if array[j] < array[min_i]:
                min_i = j
            j += 1
        swaps += 1
        array[i], array[min_i] = array[min_i], array[i]
        i += 1
    return array, comps, swaps

def merge(array, l, m, r):
    comps, swaps = 0, 0

    l_copy = array[l:m + 1]
    r_copy = array[m + 1:r + 1]

    l_copy_index = 0
    r_copy_index = 0
    sorted_index = l

    while l_copy_index < len(l_copy) and r_copy_index < len(r_copy):

        comps += 1
        if l_copy[l_copy_index] <= r_copy[r_copy_index]:
            array[sorted_index] = l_copy[l_copy_index]
            l_copy_index += 1
            swaps += 1
        else:
            array[sorted_index] = r_copy[r_copy_index]
            r_copy_index += 1
            swaps += 1

        sorted_index += 1

    while l_copy_index < len(l_copy):
        swaps += 1
        array[sorted_index] = l_copy[l_copy_index]
        l_copy_index = l_copy_index + 1
        sorted_index += 1

    while r_copy_index < len(r_copy):
        swaps += 1
        array[sorted_index] = r_copy[r_copy_index]
        r_copy_index += 1
        sorted_index += 1
    return comps, swaps

comps, swaps = 0, 0

def merge_sort(array, left, right):
    global comps, swaps
    if left < right:
        m = (left + right) // 2
        merge_sort(array, left, m)
        merge_sort(array, m + 1, right)
        temp_comps, temp_swaps = merge(array, left, m, right)
        print(array)
        comps += temp_comps
        swaps += temp_swaps
    return array, comps, swaps
