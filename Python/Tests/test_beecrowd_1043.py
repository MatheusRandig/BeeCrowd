from Python.Problems import beecrowd_1043


# check exercise output
def test_beginner1043_output_print_one() -> None:
    result = beecrowd_1043.output_print([6.0, 4.0, 2.0])
    assert result == "Area = 10.0"


def test_beginner1043_output_print_two() -> None:
    result = beecrowd_1043.output_print([6.0, 4.0, 2.1])
    assert result == "Perimetro = 12.1"


# check area of the triangle function
def test_beginner1043_area_one() -> None:
    result = beecrowd_1043.area(6.0, 4.0, 2.0)
    assert result == 10.0


def test_beginner1043_area_two() -> None:
    result = beecrowd_1043.area(6.0, 4.0, 1.8)
    assert result == 9.0


# check perimeter of the triangle function
def test_beginner1043_perimeter_one() -> None:
    result = beecrowd_1043.perimeter(6.0, 4.0, 2.1)
    assert result == 12.1


def test_beginner1043_perimeter_two() -> None:
    result = beecrowd_1043.perimeter(6.0, 4.0, 3.0)
    assert result == 13.0
