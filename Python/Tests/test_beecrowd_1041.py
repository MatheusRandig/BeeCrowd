from Python.Problems import beecrowd_1041


# check exercise output
def test_beginner1041_output_print_one() -> None:
    result = beecrowd_1041.output_print(4.5, -2.2)
    assert result == "Q4"


def test_beginner1041_output_print_two() -> None:
    result = beecrowd_1041.output_print(0.1, 0.1)
    assert result == "Q1"


def test_beginner1041_output_print_three() -> None:
    result = beecrowd_1041.output_print(0.0, 0.0)
    assert result == "Origem"


def test_beginner1041_output_print_four() -> None:
    result = beecrowd_1041.output_print(1.0, 0.0)
    assert result == "Eixo X"


def test_beginner1041_output_print_five() -> None:
    result = beecrowd_1041.output_print(0.0, 0.5)
    assert result == "Eixo Y"


def test_beginner1041_output_print_six() -> None:
    result = beecrowd_1041.output_print(-10.0, 4.0)
    assert result == "Q2"


def test_beginner1041_output_print_seven() -> None:
    result = beecrowd_1041.output_print(-10.0, -4.0)
    assert result == "Q3"
