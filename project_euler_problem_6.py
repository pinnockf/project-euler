'''The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
'''

def main(threshold):
    square_of_sum = 0
    sum_of_squares = sum([x**2 for x in range(1, threshold+1)])

    square_of_sum = sum([x for x in range(1, threshold+1)])**2

    return square_of_sum - sum_of_squares

if __name__ == "__main__":
    assert main(10)==2640
    main(100)