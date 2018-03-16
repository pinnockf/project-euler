'''Largest palindrome product
Problem 4 
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

def is_num_palindrome(number):

    return str(number) == str(number)[::-1]

def main(num1, num2, debug=False):
    palindromes = {}
    for num1 in range(num1,99,-1):
        for num2 in range(num2,99,-1):
            product = num1*num2
            if debug:
                print(num1,num2,product)
            if (is_num_palindrome(product)):
                palindromes[product] = (num1,num2)
                    
    largest_palindrome = max(palindromes.keys())
    factor1 = palindromes[largest_palindrome][0]
    factor2 = palindromes[largest_palindrome][1]
    
    if debug:
        print("Largest palindrome made from the product of the two 3-digit numbers:", largest_palindrome)
        print("Factor 1: {}, Factor 2: {}".format(factor1, factor2))

    return largest_palindrome


if __name__ == "__main__":
    #Check that given case is true
    assert is_num_palindrome(9009)
    print(main(999, 999))
    