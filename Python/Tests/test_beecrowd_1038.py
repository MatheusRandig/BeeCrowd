from Python.Problems import beecrowd_1038


# check exercise snack menu
def test_beginner1038_snack_menu_one():
    result = beecrowd_1038.snack_menu(3, 2)
    assert result == 10.00


def test_beginner1038_snack_menu_two():
    result = beecrowd_1038.snack_menu(4, 3)
    assert result == 6.00


def test_beginner1038_snack_menu_three():
    result = beecrowd_1038.snack_menu(2, 3)
    assert result == 13.50


# check exercise snack menu
def test_beginner1038_output_print_one():
    result = beecrowd_1038.output_print(3, 2)
    assert result == "Total: R$ 10.00"


def test_beginner1038_output_print_two():
    result = beecrowd_1038.output_print(4, 3)
    assert result == "Total: R$ 6.00"


def test_beginner1038_output_print_three():
    result = beecrowd_1038.output_print(2, 3)
    assert result == "Total: R$ 13.50"
