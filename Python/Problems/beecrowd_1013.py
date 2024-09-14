# https://judge.beecrowd.com/en/problems/view/1013

# Returns the biggest number of a string of number that are separated by an empty space
def biggest_int_number_oneliner(sequence: str) -> int:
    arr = [int(x) for x in sequence.split()]
    biggest = arr[0]
    for i in arr[1::]:
        if i > biggest:
            biggest = i
    return biggest


# Returns the exercise output
def output_print(user_input: str) -> str:
    return str(biggest_int_number_oneliner(user_input)) + " eh o maior"


# user input
if __name__ == "__main__":
    user_input = input()
    print(output_print(user_input))
