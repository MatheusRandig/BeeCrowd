#https://judge.beecrowd.com/en/problems/view/1018

# Returns number of notes from determined size
def bank_notes_mod(total,size):
    return total//size



# Returns the exercise output
def output_print(total):

    result = (str(total))+"\n"

    notes = bank_notes_mod(total,100)
    result += ((str(notes))+" nota(s) de R$ 100,00\n")
    total = total - (notes*100)

    notes = bank_notes_mod(total,50)
    result += ((str(notes))+" nota(s) de R$ 50,00\n")
    total = total - (notes*50)

    notes = bank_notes_mod(total,20)
    result += ((str(notes))+" nota(s) de R$ 20,00\n")
    total = total - (notes*20)

    notes = bank_notes_mod(total,10)
    result += ((str(notes))+" nota(s) de R$ 10,00\n")
    total = total - (notes*10)

    notes = bank_notes_mod(total,5)
    result += ((str(notes))+" nota(s) de R$ 5,00\n")
    total = total - (notes*5)

    notes = bank_notes_mod(total,2)
    result += ((str(notes))+" nota(s) de R$ 2,00\n")
    total = total - (notes*2)

    notes = bank_notes_mod(total,1)
    result += ((str(notes))+" nota(s) de R$ 1,00")
    return result

# user input
if __name__ == "__main__":

    x = int(input())

    print(output_print(x))