from Python.Problems import beecrowd_1037


# check exercise logic and output
def test_beginner1037_interval_one() -> None:
    result = beecrowd_1037.interval(25.01)
    assert result == "Intervalo (25,50]"


def test_beginner1037_interval_two() -> None:
    result = beecrowd_1037.interval(25.00)
    assert result == "Intervalo [0,25]"


def test_beginner1037_interval_three() -> None:
    result = beecrowd_1037.interval(100.00)
    assert result == "Intervalo (75,100]"


def test_beginner1037_interval_four() -> None:
    result = beecrowd_1037.interval(-25.02)
    assert result == "Fora de intervalo"
