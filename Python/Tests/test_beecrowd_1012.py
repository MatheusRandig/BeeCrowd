from Python.Problems import beecrowd_1012


# check area rectangle triangle
def test_beginner1012_area_rectangle_triangle_one() -> None:
    result = beecrowd_1012.area_rectangle_triangle(3.0, 5.2, 3)
    assert result == "7.800"


def test_beginner1012_area_rectangle_triangle_two() -> None:
    result = beecrowd_1012.area_rectangle_triangle(12.7, 15.2, 3)
    assert result == "96.520"


# check area circle
def test_beginner1012_area_circle_one() -> None:
    result = beecrowd_1012.area_circle(5.2, 3)
    assert result == "84.949"


def test_beginner1012_area_circle_two() -> None:
    result = beecrowd_1012.area_circle(15.2, 3)
    assert result == "725.833"


# check area trapezium
def test_beginner1012_area_trapezium_one() -> None:
    result = beecrowd_1012.area_trapezium(3.0, 4.0, 5.2, 3)
    assert result == "18.200"


def test_beginner1012_area_trapezium_two() -> None:
    result = beecrowd_1012.area_trapezium(12.7, 10.4, 15.2, 3)
    assert result == "175.560"


# check area square
def test_beginner1012_area_square_one() -> None:
    result = beecrowd_1012.area_square(4.0, 3)
    assert result == "16.000"


def test_beginner1012_area_square_two() -> None:
    result = beecrowd_1012.area_square(10.4, 3)
    assert result == "108.160"


# check area rectangle
def test_beginner1012_area_rectangle_one() -> None:
    result = beecrowd_1012.area_rectangle(3.0, 4.0, 3)
    assert result == "12.000"


def test_beginner1012_area_rectangle_two() -> None:
    result = beecrowd_1012.area_rectangle(12.7, 10.4, 3)
    assert result == "132.080"


# check exercise output
def test_beginner1012_print_one() -> None:
    result = beecrowd_1012.output_print(3.0, 4.0, 5.2)
    assert (
        result
        == "TRIANGULO: 7.800\nCIRCULO: 84.949\nTRAPEZIO: 18.200\nQUADRADO: 16.000\nRETANGULO: 12.000"
    )


def test_beginner1012_print_two() -> None:
    result = beecrowd_1012.output_print(12.7, 10.4, 15.2)
    assert (
        result
        == "TRIANGULO: 96.520\nCIRCULO: 725.833\nTRAPEZIO: 175.560\nQUADRADO: 108.160\nRETANGULO: 132.080"
    )
