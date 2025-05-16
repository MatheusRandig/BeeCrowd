from Python.Problems import beecrowd_1044


# check multiples
def test_beginner1044_multiples_one() -> None:
    assert beecrowd_1044.multiples(6, 24)


# check multiples
def test_beginner1044_multiples_two() -> None:
    assert not beecrowd_1044.multiples(6, 25)


# check exercise output
def test_beginner1044_output_print_one() -> None:
    result = beecrowd_1044.output_print([6, 24])
    assert result == "Sao Multiplos"


def test_beginner1044_output_print_two() -> None:
    result = beecrowd_1044.output_print([6, 25])
    assert result == "Nao sao Multiplos"
