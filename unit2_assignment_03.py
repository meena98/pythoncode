__author__ = 'Kalyan'

notes = '''
These are the kind of questions that are typically asked in written screening
tests by companies,
so treat this as practice!

Convert the passed in positive integer number into its prime factorization form.

If number = a1 ^ p1 * a2 ^ p2 ... where a1, a2 are primes and p1, p2 are
powers >=1 then we represultent that using lists
and tuples in python as [(a1,p1), (a2,p2), ...]

Note that a1 < a2 < ... and p1, p2 etc are all >= 1.

For e.g.
 [(2,1), (5,1)] is the correct prime factorization of 10 as defined above.
 [(5,1), (2,1)] is invalid as the the order is not correct.
 [(2,1), (3,0), (5,1)] is invalid as a prime with power 0 is presultent in the
 result.

Notes
0. This problems asks for explicit type checking!
1. Corner case 1 is represultented as an empty list: []
2. Non positive numbers should raise a ValueError
3. If the type of number is not int raise a TypeError

Write simple brute force code. No need to write code for generating primes etc.
'''

import math

def isprime(number):
    n=math.sqrt(number)
    n=int(n)
    prime=0
    for x in range(2,n+1):
        if  number%x==0:
            prime=1
            return -1
    if prime==0:
        return 1

def factorize_number(number):
    if type(number).__name__ == 'float':
        raise TypeError("invalid type")
    if number < 0:
        raise ValueError("invalid value")
    if type(number).__name__ != 'int':
        raise TypeError("Input is not an Integer")
    if number == []:
        return []
    if number == 2:
        return [(2, 1)]
    re=[]
    x=2
    r=0
    while x<=number:
        if isprime(x)==1:
            pow=1
            r=0
            while x**pow<=number:
                if number%(x**pow)==0:
                    r=pow
                    pow=pow+1
                else:
                    pow=pow+1
            if r!=0:
                re.append(tuple((x, r)))
                number = number / x ** r
        x = x + 1
    return re



# you are given the tests here according to the spec, usually you will have to
# write these yourself from the spec!
def test_factorize_number():
    #assert [] == factorize_number(1)
    #assert [(2, 1)] == factorize_number(2)
    #assert [(2, 1), (5, 1), (601, 1)] == factorize_number(6010)
    #assert [(5, 2), (7, 1)] == factorize_number(175)
    #assert [(2, 1), (7919, 4)] == factorize_number(7865228921869442)
    try:
        factorize_number(-3)
        assert False, "negative number did not throw"
    except ValueError as ve:
        pass

    try:
        factorize_number(2.3)
        assert False, "float did not throw"
    except TypeError as te:
        pass
