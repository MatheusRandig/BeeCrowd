from Python.Problems import beecrowd_1042


# check exercise output
def test_beginner1042_output_print_one() -> None:
    result = beecrowd_1042.output_print([7, 21, -14])
    assert result == "-14\n7\n21\n\n7\n21\n-14"


def test_beginner1042_output_print_two() -> None:
    result = beecrowd_1042.output_print([-14, 21, 7])
    assert result == "-14\n7\n21\n\n-14\n21\n7"


# check exercise output
def test_beginner1042_sorter_one() -> None:
    result = beecrowd_1042.sorter([7, 21, -14])
    assert result == "-14\n7\n21"


def test_beginner1042_sorter_two() -> None:
    result = beecrowd_1042.sorter([-14, 21, 7])
    assert result == "-14\n7\n21"
