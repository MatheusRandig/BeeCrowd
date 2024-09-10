from Python.Problems import beecrowd_1035


# check exercise logic and output
def test_beginner1035_selection_test_one():
    result = beecrowd_1035.selection_test(5,6,7,8)
    assert result == "Valores nao aceitos"

def test_beginner1035_selection_test_two():
    result = beecrowd_1035.selection_test(2, 3,2,6)
    assert result == "Valores aceitos"

def test_beginner1035_selection_test_three():
    result = beecrowd_1035.selection_test(1,3,2,6)
    assert result == "Valores nao aceitos"