from Python.Problems import beecrowd_1051


# check taxes of exercise
def test_beginner1051_taxes_one() -> None:
    result = beecrowd_1051.taxes(3002.00)
    assert result == "R$ 80.36"


def test_beginner1051_taxes_two() -> None:
    result = beecrowd_1051.taxes(1701.12)
    assert result == "Isento"


def test_beginner1051_taxes_three() -> None:
    result = beecrowd_1051.taxes(4520.00)
    assert result == "R$ 355.60"
