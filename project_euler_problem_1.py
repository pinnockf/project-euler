'''
Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def main(threshold):
    multiples = []
    for number in range(threshold):
        if number % 3 is 0 or number % 5 is 0:
            multiples.append(number)

    return sum(multiples)

if __name__ == '__main__':
    assert main(10) is 23
    print(main(1000))
