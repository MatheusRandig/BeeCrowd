from Python.Problems import beecrowd_1064


# check average_of_positives of exercise 1064
def test_beginner1064_average_of_positives_one() -> None:
    result = beecrowd_1064.average_of_positives([7, -5, 6, -3.4, 4.6, 12], 0, 0)
    assert result == (29.6, 4)


def test_beginner1064_average_of_positives_two() -> None:
    result = beecrowd_1064.average_of_positives([1, 1, 1, 1, 1, 1], 5, 5)
    assert result == (11, 11)


# ocheck output_1064 of ecercise 1064
def test_beginner1064_output_1064_one() -> None:
    result = beecrowd_1064.output_1064([7.0, -5.0, 6.0, -3.4, 4.6, 12.0])
    assert result == "4 valores positivos\n7.4"


def test_beginner1064_output_1064_two() -> None:
    result = beecrowd_1064.output_1064([-7.0, -5.0, -6.0, -3.4, -4.6, -12.0])
    assert result == "Sem Valores Positivos"
