from Python.Problems import beecrowd_1044


# check multiples
def test_beginner1044_multiples_one() -> None:
    check = 0
    result = beecrowd_1044.multiples(6, 24)
    if result:
        check = 1
    assert check == 1


def test_beginner1044_multiples_two() -> None:
    result = beecrowd_1044.multiples(6, 25)
    check = 0
    if not result:
        check = 1
    assert check == 1


# check exercise output
def test_beginner1044_output_print_one() -> None:
    result = beecrowd_1044.output_print([6, 24])
    assert result == "Sao Multiplos"


def test_beginner1044_output_print_two() -> None:
    result = beecrowd_1044.output_print([6, 25])
    assert result == "Nao sao Multiplos"
