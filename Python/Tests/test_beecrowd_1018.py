from Python.Problems import beecrowd_1018


# check banknotes function with all the possible number
def test_beginner1018_bank_notes_mod_one():
    result = beecrowd_1018.bank_notes_mod(576, 100)
    assert result == 5


def test_beginner1018_bank_notes_mod_two():
    result = beecrowd_1018.bank_notes_mod(76, 50)
    assert result == 1


def test_beginner1018_bank_notes_mod_three():
    result = beecrowd_1018.bank_notes_mod(26, 20)
    assert result == 1


def test_beginner1018_bank_notes_mod_four():
    result = beecrowd_1018.bank_notes_mod(6, 10)
    assert result == 0


def test_beginner1018_bank_notes_mod_five():
    result = beecrowd_1018.bank_notes_mod(6, 5)
    assert result == 1


def test_beginner1018_bank_notes_mod_six():
    result = beecrowd_1018.bank_notes_mod(1, 2)
    assert result == 0


def test_beginner1018_bank_notes_mod_seven():
    result = beecrowd_1018.bank_notes_mod(1, 1)
    assert result == 1


# check exercise output
def test_beginner1018_print_one():
    result = beecrowd_1018.output_print(576)
    assert (
        result
        == "576\n5 nota(s) de R$ 100,00\n1 nota(s) de R$ 50,00\n1 nota(s) de R$ 20,00\n0 nota(s) de R$ 10,00\n1 nota(s) de R$ 5,00\n0 nota(s) de R$ 2,00\n1 nota(s) de R$ 1,00"
    )


def test_beginner1018_print_two():
    result = beecrowd_1018.output_print(11257)
    assert (
        result
        == "11257\n112 nota(s) de R$ 100,00\n1 nota(s) de R$ 50,00\n0 nota(s) de R$ 20,00\n0 nota(s) de R$ 10,00\n1 nota(s) de R$ 5,00\n1 nota(s) de R$ 2,00\n0 nota(s) de R$ 1,00"
    )


def test_beginner1018_print_three():
    result = beecrowd_1018.output_print(503)
    assert (
        result
        == "503\n5 nota(s) de R$ 100,00\n0 nota(s) de R$ 50,00\n0 nota(s) de R$ 20,00\n0 nota(s) de R$ 10,00\n0 nota(s) de R$ 5,00\n1 nota(s) de R$ 2,00\n1 nota(s) de R$ 1,00"
    )
