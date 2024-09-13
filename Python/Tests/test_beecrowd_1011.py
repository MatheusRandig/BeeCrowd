from Python.Problems import beecrowd_1011


# check circle volume of the function
def test_beginner1011_total_price_one():
    result = beecrowd_1011.volume_circle(3, 3)
    assert result == "113.097"


def test_beginner1011_total_price_two():
    result = beecrowd_1011.volume_circle(15, 3)
    assert result == "14137.155"


def test_beginner1011_total_price_three():
    result = beecrowd_1011.volume_circle(1523, 3)
    assert result == "14797486501.627"


# check exercise output
def test_beginner1011_print_one():
    result = beecrowd_1011.output_print(3)
    assert result == "VOLUME = 113.097"


def test_beginner1011_print_two():
    result = beecrowd_1011.output_print(15)
    assert result == "VOLUME = 14137.155"


def test_beginner1011_print_three():
    result = beecrowd_1011.output_print(1523)
    assert result == "VOLUME = 14797486501.627"
