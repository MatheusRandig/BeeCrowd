from Python.Problems import beecrowd_1048


# check exercise output
def test_beginner1048_output_print_one() -> None:
    result = beecrowd_1048.output_print(400.00)
    assert result == "Novo salario: 460.00\nReajuste ganho: 60.00\nEm percentual: 15 %"


def test_beginner1048_output_print_two() -> None:
    result = beecrowd_1048.output_print(700.00)
    assert result == "Novo salario: 784.00\nReajuste ganho: 84.00\nEm percentual: 12 %"


def test_beginner1048_output_print_three() -> None:
    result = beecrowd_1048.output_print(800.01)
    assert result == "Novo salario: 880.01\nReajuste ganho: 80.00\nEm percentual: 10 %"


def test_beginner1048_output_print_four() -> None:
    result = beecrowd_1048.output_print(2000.00)
    assert result == "Novo salario: 2140.00\nReajuste ganho: 140.00\nEm percentual: 7 %"


def test_beginner1048_output_print_five() -> None:
    result = beecrowd_1048.output_print(3000.00)
    assert result == "Novo salario: 3120.00\nReajuste ganho: 120.00\nEm percentual: 4 %"
