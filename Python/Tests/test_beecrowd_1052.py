from Python.Problems import beecrowd_1052


# check n_to_month of exercise 1052
def test_beginner1052_n_to_month_one() -> None:
    result = beecrowd_1052.n_to_month(1)
    assert result == "January"


def test_beginner1052_n_to_month_two() -> None:
    result = beecrowd_1052.n_to_month(10)
    assert result == "October"
