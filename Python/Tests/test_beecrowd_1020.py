from Python.Problems import beecrowd_1020


# check days to years function
def test_beginner1020_days_to_years_one() -> None:
    result = beecrowd_1020.days_to_years(400)
    assert result == 1


def test_beginner1020_days_to_years_two() -> None:
    result = beecrowd_1020.days_to_years(800)
    assert result == 2


def test_beginner1020_days_to_years_three() -> None:
    result = beecrowd_1020.days_to_years(30)
    assert result == 0


# check days to month function
def test_beginner1020_days_to_month_one() -> None:
    result = beecrowd_1020.days_to_month(70)
    assert result == 2


def test_beginner1020_days_to_month_two() -> None:
    result = beecrowd_1020.days_to_month(35)
    assert result == 1


def test_beginner1020_days_to_months_three() -> None:
    result = beecrowd_1020.days_to_month(30)
    assert result == 1


# check output of the exercise
def test_beginner1020_output_print_one() -> None:
    result = beecrowd_1020.output_print(400)
    assert result == "1 ano(s)\n1 mes(es)\n5 dia(s)"


def test_beginner1020_output_print_two() -> None:
    result = beecrowd_1020.output_print(800)
    assert result == "2 ano(s)\n2 mes(es)\n10 dia(s)"


def test_beginner1020_output_print_three() -> None:
    result = beecrowd_1020.output_print(30)
    assert result == "0 ano(s)\n1 mes(es)\n0 dia(s)"
