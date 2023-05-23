from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([0], 0, "test") == 0
    assert arrs.get([6, 5, 7], -1, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -1, 4) == [3]
    assert arrs.my_slice([], 0) == []
    assert arrs.my_slice([1, 2, 3], -4) == [1, 2, 3]
    