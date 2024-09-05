from Python.Problems import beecrowd_1005


# Checking average
def test_beginner1005_one():
    result = beecrowd_1005.average_35_75(5.0,7.1,5)
    assert result == '6.43182'


def test_beginner1005_two():
    result = beecrowd_1005.average_35_75(0.0,7.1,5)
    assert result == '4.84091'


def test_beginner1005_three():
    result = beecrowd_1005.average_35_75(10.0,10.0,5)
    assert result == '10.00000'


#Checking output
def test_beginner1005_print_one():
    result = beecrowd_1005.output_print(5.0,7.1)
    assert result == 'MEDIA = 6.43182'


def test_beginner1005_print_two():
    result = beecrowd_1005.output_print(0.0,7.1)
    assert result == 'MEDIA = 4.84091'


def test_beginner1005_print_three():
    result = beecrowd_1005.output_print(10.0,10.0)
    assert result == 'MEDIA = 10.00000'
