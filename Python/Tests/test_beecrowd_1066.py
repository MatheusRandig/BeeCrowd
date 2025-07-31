from Python.Problems import beecrowd_1066


# check average_of_positives of exercise 1066
def test_beginner1064_separete_in_bucktes_one() -> None:
    result = beecrowd_1066.separete_in_bucktes([-5, 0, -3, -4, 12])
    assert result == ([3, 2, 1, 3])


def test_beginner1064_separete_in_bucktes_two() -> None:
    result = beecrowd_1066.separete_in_bucktes([0, 0, 0, 0, 0])
    assert result == ([5, 0, 0, 0])


# ocheck output_1066 of ecercise 1066
def test_beginner1066_output_1066_one() -> None:
    result = beecrowd_1066.output_1066([-5, 0, -3, -4, 12])
    assert (
        result
        == "3 valor(es) par(es)\n2 valor(es) impar(es)\n1 valor(es) positivo(s)\n3 valor(es) negativo(s)"
    )


def test_beginner1066_output_1066_two() -> None:
    result = beecrowd_1066.output_1066([-7, -5, 7, -3, -4])
    assert (
        result
        == "1 valor(es) par(es)\n4 valor(es) impar(es)\n1 valor(es) positivo(s)\n4 valor(es) negativo(s)"
    )
