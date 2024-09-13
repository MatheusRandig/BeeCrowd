from Python.Problems import beecrowd_1013


# check biggest int number
def test_beginner1013_biggest_int_number_oneliner_one():
    result = beecrowd_1013.biggest_int_number_oneliner("7 14 106")
    assert result == 106


def test_beginner1013_biggest_int_number_oneliner_two():
    result = beecrowd_1013.biggest_int_number_oneliner("217 14 6")
    assert result == 217


# check exercise output
def test_beginner1013_print_one():
    result = beecrowd_1013.output_print("7 14 106")
    assert result == "106 eh o maior"


def test_beginner1013_print_two():
    result = beecrowd_1013.output_print("217 14 6")
    assert result == "217 eh o maior"
