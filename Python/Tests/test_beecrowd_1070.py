from Python.Problems import beecrowd_1070


# check aodd_zero_to_range of exercise 1070
def test_beginner1070_next_six_odd_one() -> None:
    result = beecrowd_1070.next_six_odd(8)
    assert result == ([9, 11, 13, 15, 17, 19])


def test_beginner1070_next_six_odd_two() -> None:
    result = beecrowd_1070.next_six_odd(1)
    assert result == ([1, 3, 5, 7, 9, 11])


# check output_1070 in exercise 1070
def test_beginner1070_output_1070_one() -> None:
    result = beecrowd_1070.output_1070(8)
    assert result == ("9\n11\n13\n15\n17\n19")


def test_beginner1070_output_1070_two() -> None:
    result = beecrowd_1070.output_1070(1)
    assert result == ("1\n3\n5\n7\n9\n11")
