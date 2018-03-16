'''
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, 
a^2 + b^2 = c^2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def main():
    for a in range(1, 999):
        for b in range(1, 999):
                c = (a**2 + b**2)**.5
                sum = a+b+c
                
                if sum == 1000:
                    print("a:", a, "b:", b, "c:", c, "sum:", sum)
                    product = a*b*c
                    print("Product:", product) 
                    return product
                    

if __name__ == "__main__":
    print(main())