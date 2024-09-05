from Python.Problems import beecrowd_1006

# Check Average
def test_beginner1006_one():
    result = beecrowd_1006.average_2_3_5(5.0, 6.0, 7.0, 1)
    assert result == "6.3"


def test_beginner1006_two():
    result = beecrowd_1006.average_2_3_5(5.0, 10.0, 10.0, 1)
    assert result == "9.0"


def test_beginner1006_thee():
    result = beecrowd_1006.average_2_3_5(10.0,10.0,5.0,1)
    assert result == "7.5"


# Check Output
def test_beginner1006_print_one():
    result = beecrowd_1006.output_print(5.0,6.0,7.0)
    assert result == "MEDIA = 6.3"


def test_beginner1006_print_two():
    result = beecrowd_1006.output_print(5.0,10.0,10.0)
    assert result == "MEDIA = 9.0"


def test_beginner1006_print_three():
    result = beecrowd_1006.output_print(10.0, 10.0, 5.0)
    assert result == "MEDIA = 7.5"