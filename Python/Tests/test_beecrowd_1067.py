from Python.Problems import beecrowd_1067


# check aodd_zero_to_range of exercise 1067
def test_beginner1067_odd_zero_to_range_one() -> None:
    result = beecrowd_1067.odd_zero_to_range(8)
    assert result == ([1, 3, 5, 7])


def test_beginner1067_odd_zero_to_range_two() -> None:
    result = beecrowd_1067.odd_zero_to_range(0)
    assert result == ([])


# check output_1067 in exercise 1067
def test_beginner1067_output_1067_one() -> None:
    result = beecrowd_1067.output_1067(8)
    assert result == ("1\n3\n5\n7")


def test_beginner1067_output_1067_two() -> None:
    result = beecrowd_1067.output_1067(0)
    assert result == ("")
