from Python.Problems import beecrowd_1071


# check sum_odd_in_between of exercise 1071
def test_beginner1071_sum_odd_in_between_one() -> None:
    result = beecrowd_1071.sum_odd_in_between(0, 0)
    assert result == (0)


def test_beginner1071sum_odd_in_between_two() -> None:
    result = beecrowd_1071.sum_odd_in_between(6, -5)
    assert result == (5)


def test_beginner1071sum_odd_in_between_three() -> None:
    result = beecrowd_1071.sum_odd_in_between(12, 15)
    assert result == (13)
