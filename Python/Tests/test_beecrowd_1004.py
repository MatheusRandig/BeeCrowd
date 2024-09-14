from Python.Problems import beecrowd_1004


# Checking sum
def test_beginner1004_one() -> None:
    result = beecrowd_1004.prod(3, 9)
    assert result == 27


def test_beginner1004_two() -> None:
    result = beecrowd_1004.prod(-30, 10)
    assert result == -300


def test_beginner1004_three() -> None:
    result = beecrowd_1004.prod(0, 9)
    assert result == 0


# Checking output
def test_beginner1004_print_one() -> None:
    result = beecrowd_1004.output_print(3, 9)
    assert result == "PROD = 27"


def test_beginner1004_print_two() -> None:
    result = beecrowd_1004.output_print(-30, 10)
    assert result == "PROD = -300"


def test_beginner1004_print_three() -> None:
    result = beecrowd_1004.output_print(0, 0)
    assert result == "PROD = 0"
