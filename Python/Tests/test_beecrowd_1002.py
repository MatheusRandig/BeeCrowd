from Python.Problems import beecrowd_1002


# Checking Circle Area
def test_beginner1002_one() -> None:
    result = beecrowd_1002.circle_area(2.00, 4)
    assert result == "12.5664"


def test_beginner1002_two() -> None:
    result = beecrowd_1002.circle_area(100.64, 4)
    assert result == "31819.3103"


def test_beginner1002_three() -> None:
    result = beecrowd_1002.circle_area(150.00, 4)
    assert result == "70685.7750"


# Checking output
def test_beginner1002_print_one() -> None:
    result = beecrowd_1002.output_print(2.00)
    assert result == "A=12.5664"


def test_beginner1002_print_two() -> None:
    result = beecrowd_1002.output_print(100.64)
    assert result == "A=31819.3103"


def test_beginner1002_print_three() -> None:
    result = beecrowd_1002.output_print(150.00)
    assert result == "A=70685.7750"
