from Python.Problems import beecrowd_1045


# check exercise output
def test_beginner1045_output_print_one() -> None:
    result = beecrowd_1045.output_print(7.0, 7.0, 5.0)
    assert result == "TRIANGULO ACUTANGULO\nTRIANGULO ISOSCELES"


def test_beginner1045_output_print_two() -> None:
    result = beecrowd_1045.output_print(10.0, 6.0, 6.0)
    assert result == "TRIANGULO OBTUSANGULO\nTRIANGULO ISOSCELES"


def test_beginner1045_output_print_three() -> None:
    result = beecrowd_1045.output_print(6.0, 6.0, 6.0)
    assert result == "TRIANGULO ACUTANGULO\nTRIANGULO EQUILATERO"


def test_beginner1045_output_print_four() -> None:
    result = beecrowd_1045.output_print(7.0, 5.0, 2.0)
    assert result == "NAO FORMA TRIANGULO"


def test_beginner1045_output_print_five() -> None:
    result = beecrowd_1045.output_print(10.0, 8.0, 6.0)
    assert result == "TRIANGULO RETANGULO"


# check not triangle
def test_beginner1045_not_triangle_one() -> None:
    check = 0
    result = beecrowd_1045.not_triangle(6.0, 6.0, 6.0)
    if not result:
        check = 1
    assert check == 1


def test_beginner1045_not_triangle_two() -> None:
    result = beecrowd_1045.not_triangle(7.0, 5.0, 2.0)
    check = 0
    if result:
        check = 1
    assert check == 1


# check rectangle triangle
def test_beginner1045_rectangle_triangle_one() -> None:
    check = 0
    result = beecrowd_1045.rectangle_triangle(6.0, 6.0, 6.0)
    if not result:
        check = 1
    assert check == 1


def test_beginner1045_rectangle_triangle_two() -> None:
    result = beecrowd_1045.rectangle_triangle(10.0, 8.0, 6.0)
    check = 0
    if result:
        check = 1
    assert check == 1


# check obtuse triangle
def test_beginner1045_obtuse_triangle_one() -> None:
    check = 0
    result = beecrowd_1045.obtuse_triangle(6.0, 6.0, 6.0)
    if not result:
        check = 1
    assert check == 1


def test_beginner1045_obtuse_triangle_two() -> None:
    result = beecrowd_1045.obtuse_triangle(10.0, 6.0, 6.0)
    check = 0
    if result:
        check = 1
    assert check == 1


# check acute triangle (kawaii)
def test_beginner1045_acute_triangle_one() -> None:
    check = 0
    result = beecrowd_1045.acute_triangle(10.0, 6.0, 6.0)
    if not result:
        check = 1
    assert check == 1


def test_beginner1045_acute_triangle_two() -> None:
    result = beecrowd_1045.acute_triangle(6.0, 6.0, 6.0)
    check = 0
    if result:
        check = 1
    assert check == 1


# check acute triangle (kawaii)
def test_beginner1045_equilateral_triangle_one() -> None:
    check = 0
    result = beecrowd_1045.equilateral_triangle(10.0, 6.0, 6.0)
    if not result:
        check = 1
    assert check == 1


def test_beginner1045_equilateral_triangle_two() -> None:
    result = beecrowd_1045.equilateral_triangle(7.0, 7.0, 7.0)
    check = 0
    if result:
        check = 1
    assert check == 1


# check isosceles triangle
def test_beginner1045_isosceles_triangle_one() -> None:
    check = 0
    result = beecrowd_1045.isosceles_triangle(7.0, 6.0, 5.0)
    if not result:
        check = 1
    assert check == 1


def test_beginner1045_isosceles_triangle_two() -> None:
    result = beecrowd_1045.isosceles_triangle(10.0, 6.0, 6.0)
    check = 0
    if result:
        check = 1
    assert check == 1
