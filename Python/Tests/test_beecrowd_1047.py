from Python.Problems import beecrowd_1047


# check exercise output
def test_beginner1047_output_print_one() -> None:
    result = beecrowd_1047.output_print(428, 550)
    assert result == "O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)"


def test_beginner1047_output_print_two() -> None:
    result = beecrowd_1047.output_print(427, 427)
    assert result == "O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)"


def test_beginner1047_output_print_three() -> None:
    result = beecrowd_1047.output_print(430, 489)
    assert result == "O JOGO DUROU 0 HORA(S) E 59 MINUTO(S)"
