from Python.Problems import beecrowd_1007


# check prod
def test_beginner1007_prod_one() -> None:
    result = beecrowd_1007.prod(5, 6)
    assert result == 30


def test_beginner1007_prod_two() -> None:
    result = beecrowd_1007.prod(31, -17)
    assert result == -527


def test_beginner1007_prod_three() -> None:
    result = beecrowd_1007.prod(-11, -23)
    assert result == 253


# Check Dif
def test_beginner1007_dif_one() -> None:
    result = beecrowd_1007.dif(5, 6, 7, 8)
    assert result == -26


def test_beginner1007_dif_two() -> None:
    result = beecrowd_1007.dif(0, 0, 7, 8)
    assert result == -56


def test_beginner1007_dif_three() -> None:
    result = beecrowd_1007.dif(5, 6, -7, 8)
    assert result == 86


# Check Output
def test_beginner1007_print_one() -> None:
    result = beecrowd_1007.output_print(5, 6, 7, 8)
    assert result == "DIFERENCA = -26"


def test_beginner1007_print_two() -> None:
    result = beecrowd_1007.output_print(0, 0, 7, 8)
    assert result == "DIFERENCA = -56"


def test_beginner1007_print_three() -> None:
    result = beecrowd_1007.output_print(5, 6, -7, 8)
    assert result == "DIFERENCA = 86"
