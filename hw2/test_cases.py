import hw2_debugging


def test_1():
    assert hw2_debugging.merge_sort([1, 3, 2]) == [1, 2, 3]


def test_2():
    assert hw2_debugging.merge_sort([]) == []


def test_3():
    assert hw2_debugging.merge_sort(
        [-3, 4, 0, 2, 3, 6, 5]) == [-3, 0, 2, 3, 4, 5, 6]
