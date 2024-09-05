#https://judge.beecrowd.com/en/problems/view/1006


# returns average value of 3 numbers
# Value1 has 2 weight
# Value2 has 3 weight
# Value3 has 5 weight
def average_2_3_5(value1,value2,value3,digits):
    result = ('{:.'+str(digits)+'f}').format( ((value1*2) + (value2*3) + (value3*5))/10 )
    return result


# print result
def output_print(x,y,z):
    return(f"MEDIA = {average_2_3_5(x,y,z,1)}")


if __name__ == "__main__":
    # input values from user
    x = float(input())
    y = float(input())
    z = float(input())

    #print result
    print(output_print(x,y,z))