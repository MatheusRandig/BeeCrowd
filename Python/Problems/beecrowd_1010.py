# https://judge.beecrowd.com/en/problems/view/1010

# Returns the total price of a product, the product of quantity and value
def total_price(value, quantity):
    return value * quantity


# Returns the correct output for the exercise
def output_print(p1, q1, p2, q2):
    return "VALOR A PAGAR: R$ " + "{:.2f}".format(total_price(p1, q1) + total_price(p2, q2))


# user input
if __name__ == "__main__":
    product1 = [float(x) for x in input().split()]
    product2 = [float(x) for x in input().split()]

    print(output_print(product1[2], product1[1], product2[2], product2[1]))
