# https://judge.beecrowd.com/en/problems/view/1021


# Returns number of notes from determined size with decimal digits of precision
def bank_notes_mod(total, size, decimal):
    return round((total // size), decimal)


# Returns the exercise output
def output_print(total):
    result = "NOTAS:\n"

    notes = bank_notes_mod(total, 100, 3)
    result += (str(int(notes))) + " nota(s) de R$ 100.00\n"
    total = total - (notes * 100)

    notes = bank_notes_mod(total, 50, 3)
    result += (str(int(notes))) + " nota(s) de R$ 50.00\n"
    total = total - (notes * 50)

    notes = bank_notes_mod(total, 20, 3)
    result += (str(int(notes))) + " nota(s) de R$ 20.00\n"
    total = total - (notes * 20)

    notes = bank_notes_mod(total, 10, 3)
    result += (str(int(notes))) + " nota(s) de R$ 10.00\n"
    total = total - (notes * 10)

    notes = bank_notes_mod(total, 5, 3)
    result += (str(int(notes))) + " nota(s) de R$ 5.00\n"
    total = total - (notes * 5)

    notes = bank_notes_mod(total, 2, 3)
    result += (str(int(notes))) + " nota(s) de R$ 2.00\n"
    total = total - (notes * 2)

    result += "MOEDAS:\n"

    notes = bank_notes_mod(total, 1, 3)
    result += (str(int(notes))) + " moeda(s) de R$ 1.00\n"
    total = total - (notes * 1)

    notes = bank_notes_mod(total, 0.5, 3)
    result += (str(int(notes))) + " moeda(s) de R$ 0.50\n"
    total = total - (notes * 0.5)

    notes = bank_notes_mod(total, 0.25, 3)
    result += (str(int(notes))) + " moeda(s) de R$ 0.25\n"
    total = total - (notes * 0.25)

    notes = bank_notes_mod(total, 0.1, 3)
    result += (str(int(notes))) + " moeda(s) de R$ 0.10\n"
    total = total - (notes * 0.1)

    notes = bank_notes_mod(total, 0.05, 3)
    result += (str(int(notes))) + " moeda(s) de R$ 0.05\n"
    total = round(total - (notes * 0.05), 3)

    # decimal floating problem, used this trick for cents, without function
    result += str(int(-(-total // 0.01))) + " moeda(s) de R$ 0.01"

    return result


# user input
if __name__ == "__main__":
    x = float(input())

    print(output_print(x))
