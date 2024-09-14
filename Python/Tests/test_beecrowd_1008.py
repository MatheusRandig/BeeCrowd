from Python.Problems import beecrowd_1008


# Checking employee number function
def test_beginner1008_employee_number_one() -> None:
    result = beecrowd_1008.employee_number(25)
    assert result == "NUMBER = 25"


def test_beginner1008_employee_number_two() -> None:
    result = beecrowd_1008.employee_number(1)
    assert result == "NUMBER = 1"


def test_beginner1008_employee_number_three() -> None:
    result = beecrowd_1008.employee_number(6)
    assert result == "NUMBER = 6"


# check salary calculation function
def test_beginner1008_salary_one() -> None:
    result = beecrowd_1008.salary(100, 5.50)
    assert result == "SALARY = U$ 550.00"


def test_beginner1008_salary_two() -> None:
    result = beecrowd_1008.salary(200, 20.50)
    assert result == "SALARY = U$ 4100.00"


def test_beginner1008_salary_three() -> None:
    result = beecrowd_1008.salary(145, 15.55)
    assert result == "SALARY = U$ 2254.75"
