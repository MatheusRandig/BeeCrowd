from Python.Problems import beecrowd_1010

#check Total price of a product function
def test_beginner1010_total_price_one():
    result = beecrowd_1010.total_price(5.30,1)
    assert result == 5.30

def test_beginner1010_total_price_two():
    result = beecrowd_1010.total_price(5.20,4)
    assert result == 20.80

#check exercise output
def test_beginner1010_print_one():
    result = beecrowd_1010.output_print(5.30,1,5.10,2)
    assert result == "VALOR A PAGAR: R$ 15.50"

def test_beginner1010_print_two():
    result = beecrowd_1010.output_print(15.30,2,5.20,4)
    assert result == "VALOR A PAGAR: R$ 51.40"

def test_beginner1010_print_three():
    result = beecrowd_1010.output_print(15.10,1,15.10,1)
    assert result == "VALOR A PAGAR: R$ 30.20"