from Python.Problems import beecrowd_1017

# check fuel needed for a trip
def test_beginner1017_liter_needed_one():
    result = beecrowd_1017.liter_needed(10,85,12,3)
    assert result == '70.833'

def test_beginner1017_liter_needed_two():
    result = beecrowd_1017.liter_needed(2,92,12,3)
    assert result == '15.333'

def test_beginner1017_liter_needed_three():
    result = beecrowd_1017.liter_needed(22,67,12,3)
    assert result == '122.833'

