from Python.Problems import beecrowd_1003


# Checking sum
def test_beginner1001_one():
    result = beecrowd_1003.addition(30,10)
    assert result == 40


def test_beginner1001_two():
    result = beecrowd_1003.addition(-30,10)
    assert result == -20


def test_beginner1001_three():
    result = beecrowd_1003.addition(0,0)
    assert result == 0


#Checking output
def test_beginner1001_print_one():
    result = beecrowd_1003.output_print(30,10)
    assert result == "SOMA = 40"


def test_beginner1001_print_two():
    result = beecrowd_1003.output_print(-30,10)
    assert result == "SOMA = -20"


def test_beginner1001_print_three():
    result = beecrowd_1003.output_print(0,0)
    assert result == "SOMA = 0"
