from Python.Problems import beecrowd_1001


# Checking sum
def test_beginner1001_one():
    result = beecrowd_1001.beginner1001(10,9)
    assert result == 19

def test_beginner1001_two():
    result = beecrowd_1001.beginner1001(-10,4)
    assert result == -6

def test_beginner1001_three():
    result = beecrowd_1001.beginner1001(15,-7)
    assert result == 8

#Checking output
def test_beginner1001_print_one():
    result = beecrowd_1001.beginner1001_print(10,9)
    assert result == "X = 19"

def test_beginner1001_print_two():
    result = beecrowd_1001.beginner1001_print(-10,4)
    assert result == "X = -6"

def test_beginner1001_print_three():
    result = beecrowd_1001.beginner1001_print(15,-7)
    assert result == "X = 8"
