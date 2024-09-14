from Python.Problems import beecrowd_1014


# check litter to km function
def test_beginner1014_liter_km_one() -> None:
    result = beecrowd_1014.liter_km(500, 35.0, 3)
    assert result == "14.286"


def test_beginner1014_liter_km_two() -> None:
    result = beecrowd_1014.liter_km(2254, 124.4, 3)
    assert result == "18.119"


def test_beginner1014_liter_km_three() -> None:
    result = beecrowd_1014.liter_km(4554, 464.6, 3)
    assert result == "9.802"


# check exercise output
def test_beginner1014_print_one() -> None:
    result = beecrowd_1014.output_print(500, 35.0)
    assert result == "14.286 km/l"


def test_beginner1014_print_two() -> None:
    result = beecrowd_1014.output_print(2254, 124.4)
    assert result == "18.119 km/l"


def test_beginner1014_print_three() -> None:
    result = beecrowd_1014.output_print(4554, 464.6)
    assert result == "9.802 km/l"
