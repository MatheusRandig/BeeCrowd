from Python.Problems import beecrowd_1060


# check positive_numbers of exercise 1060
def test_beginner1060_positive_numbers_one() -> None:
    result = beecrowd_1060.positive_numbers([7, -5, 6, -3.4, 4.6, 12])
    assert result == 4


def test_beginner1060_positive_numbers_two() -> None:
    result = beecrowd_1060.positive_numbers([7, 2, 6, 3, 0, 12])
    assert result == 5


def test_beginner1060_positive_numbers_three() -> None:
    result = beecrowd_1060.positive_numbers([-2, -2, -6, -3, 0, -12])
    assert result == 0
