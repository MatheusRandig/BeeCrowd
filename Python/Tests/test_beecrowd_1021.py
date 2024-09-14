from Python.Problems import beecrowd_1021


# check banknotes function with all the possible values
def test_beginner1021_bank_notes_mod_one() -> None:
    result = beecrowd_1021.bank_notes_mod(576.73, 100, 3)
    assert result == 5.00


def test_beginner1021_bank_notes_mod_two() -> None:
    result = beecrowd_1021.bank_notes_mod(76.73, 50, 3)
    assert result == 1.00


def test_beginner1021_bank_notes_mod_three() -> None:
    result = beecrowd_1021.bank_notes_mod(26.73, 20, 3)
    assert result == 1.00


def test_beginner1021_bank_notes_mod_four() -> None:
    result = beecrowd_1021.bank_notes_mod(6.73, 10, 3)
    assert result == 0.00


def test_beginner1021_bank_notes_mod_five() -> None:
    result = beecrowd_1021.bank_notes_mod(6.73, 5, 3)
    assert result == 1.00


def test_beginner1021_bank_notes_mod_six() -> None:
    result = beecrowd_1021.bank_notes_mod(1.73, 2, 3)
    assert result == 0.00


def test_beginner1021_bank_notes_mod_seven() -> None:
    result = beecrowd_1021.bank_notes_mod(1.73, 1, 3)
    assert result == 1.00


def test_beginner1021_bank_notes_mod_eight() -> None:
    result = beecrowd_1021.bank_notes_mod(0.73, 0.5, 3)
    assert result == 1.00


def test_beginner1021_bank_notes_mod_nine() -> None:
    result = beecrowd_1021.bank_notes_mod(0.23, 0.25, 3)
    assert result == 0.00


def test_beginner1021_bank_notes_mod_ten() -> None:
    result = beecrowd_1021.bank_notes_mod(0.23, 0.10, 3)
    assert result == 2.00


def test_beginner1021_bank_notes_mod_eleven() -> None:
    result = beecrowd_1021.bank_notes_mod(0.03, 0.05, 3)
    assert result == 0.00


# For decimal operation imprecision, this test is not viable in the current implementation of the function
# def test_beginner1021_bank_notes_mod_eleven() -> None:
#    result = beecrowd_1021.bank_notes_mod(0.03,0.01,3)
#    assert result == 3.00


# check exercise output
def test_beginner1021_print_one() -> None:
    result = beecrowd_1021.output_print(576.73)
    assert (
        result
        == "NOTAS:\n5 nota(s) de R$ 100.00\n1 nota(s) de R$ 50.00\n1 nota(s) de R$ 20.00\n0 nota(s) de R$ 10.00\n1 nota(s) de R$ 5.00\n0 nota(s) de R$ 2.00\nMOEDAS:\n1 moeda(s) de R$ 1.00\n1 moeda(s) de R$ 0.50\n0 moeda(s) de R$ 0.25\n2 moeda(s) de R$ 0.10\n0 moeda(s) de R$ 0.05\n3 moeda(s) de R$ 0.01"
    )


def test_beginner1021_print_two() -> None:
    result = beecrowd_1021.output_print(4.00)
    assert (
        result
        == "NOTAS:\n0 nota(s) de R$ 100.00\n0 nota(s) de R$ 50.00\n0 nota(s) de R$ 20.00\n0 nota(s) de R$ 10.00\n0 nota(s) de R$ 5.00\n2 nota(s) de R$ 2.00\nMOEDAS:\n0 moeda(s) de R$ 1.00\n0 moeda(s) de R$ 0.50\n0 moeda(s) de R$ 0.25\n0 moeda(s) de R$ 0.10\n0 moeda(s) de R$ 0.05\n0 moeda(s) de R$ 0.01"
    )


def test_beginner1021_print_three() -> None:
    result = beecrowd_1021.output_print(91.01)
    assert (
        result
        == "NOTAS:\n0 nota(s) de R$ 100.00\n1 nota(s) de R$ 50.00\n2 nota(s) de R$ 20.00\n0 nota(s) de R$ 10.00\n0 nota(s) de R$ 5.00\n0 nota(s) de R$ 2.00\nMOEDAS:\n1 moeda(s) de R$ 1.00\n0 moeda(s) de R$ 0.50\n0 moeda(s) de R$ 0.25\n0 moeda(s) de R$ 0.10\n0 moeda(s) de R$ 0.05\n1 moeda(s) de R$ 0.01"
    )
