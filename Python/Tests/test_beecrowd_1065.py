from Python.Problems import beecrowd_1065


# check average_of_positives of exercise 1065
def test_beginner1064_count_between_5_one() -> None:
    result = beecrowd_1065.count_between_5([7.0, -5.0, 6.0, -4.0, 12.0])
    assert result == (3)


def test_beginner1064_count_between_5_two() -> None:
    result = beecrowd_1065.count_between_5([2.0, 4.0, 6.0, -4.0, 8.0])
    assert result == (5)


# ocheck output_1065 of ecercise 1065
def test_beginner1065_output_1065_one() -> None:
    result = beecrowd_1065.output_1065([7.0, -5.0, 6.0, -4.0, 12.0])
    assert result == "3 valores pares"


def test_beginner1065_output_1065_two() -> None:
    result = beecrowd_1065.output_1065([-7.0, -5.0, 7.0, -3.7, -4.3])
    assert result == "0 valores pares"
