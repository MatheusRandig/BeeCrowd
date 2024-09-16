from Python.Problems import beecrowd_1046


# check exercise output
def test_beginner1046_output_print_one() -> None:
    result = beecrowd_1046.output_print(16, 2)
    assert result == "O JOGO DUROU 10 HORA(S)"


def test_beginner1046_output_print_two() -> None:
    result = beecrowd_1046.output_print(0, 0)
    assert result == "O JOGO DUROU 24 HORA(S)"


def test_beginner1046_output_print_three() -> None:
    result = beecrowd_1046.output_print(2, 16)
    assert result == "O JOGO DUROU 14 HORA(S)"
