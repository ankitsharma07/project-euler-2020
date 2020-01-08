# problem_statement: https://projecteuler.net/problem=1


def multipleOf3and5(number):
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i

    return sum


print(multipleOf3and5(1000))
