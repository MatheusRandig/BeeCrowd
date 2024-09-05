from Python.Problems import beecrowd_1009

#check Total Salary function
def test_beginner1009_total_salary_one():
    result = beecrowd_1009.total_salary(500.00,1230.30)
    assert result == '684.54'


def test_beginner1009_total_salary_two():
    result = beecrowd_1009.total_salary(700.00,0.00)
    assert result == '700.00'


def test_beginner1009_total_salary_three():
    result = beecrowd_1009.total_salary(1700.00,1230.50)
    assert result == '1884.58'


#Check function output
def test_beginner1009_print_one():
    result = beecrowd_1009.output_print(500.00,1230.30)
    assert result == "TOTAL = R$ 684.54"


def test_beginner1009_print_two():
    result = beecrowd_1009.output_print(700.00,0.00)
    assert result == "TOTAL = R$ 700.00"


def test_beginner1009_print_three():
    result = beecrowd_1009.output_print(1700.00,1230.50)
    assert result == "TOTAL = R$ 1884.58"

