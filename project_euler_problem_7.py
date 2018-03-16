'''
10001st prime
Problem 7 
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
def is_prime(number):
    number_is_prime = None
    range_start = 0
    range_end = number//2 + 1
    range_step = 6
    for possible_factor in range(range_start, range_end, range_step):
        if possible_factor is 0:
            if number%2 is 0:
                number_is_prime = False
            if number%3 is 0:
                number_is_prime = False
            if number%5 is 0:
                number_is_prime = False
            if number_is_prime is False:
                return False
            else:
                continue
        if number%(possible_factor+1) is 0 or number%(possible_factor+5) is 0:
            return False

    number_is_prime = True
    return number_is_prime

def main(threshold):
    primes = [2,3,5,7,11,13]
    number = 14
    while(len(primes) < threshold):
        if is_prime(number):
            primes.append(number)
        number = number + 1

    return primes

if __name__ == "__main__":
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert is_prime(11)
    assert is_prime(13)
    print(main(10001))
