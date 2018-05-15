__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Given a string of digits, you must return a list of all (substring, count) in the input string such that count >=2 and 
len(substring) >= 2. count represents the number of times the substring repeats in the input string (non-overlapping 
occurances).

The result must be sorted by count first (descending) and then in case of a tie the numerical value of 
substring (descending)

For e.g. if input is "123451236786712" you must return [("12", 3), ("123", 2), ("67", 2), ("23", 2)]

Notes:
1. if input is not a str, raise TypeError
2. Write clean bruteforce code to do this using python features. Do not devise new algorithms in the exam!
3. Write your own test cases 
'''
from operator import itemgetter

def repeats(digits):
    try:
        if type(digits) != str:
            raise TypeError
    except TypeError as te:
        print(error)
    digits=digits.strip()
    p=0
    result=[]
    string=""
    l=2
    while True:
        if p+l > len(digits):
            l=2
            p+=1
        if p>len(digits):
            break
        string=digits[p:p+l]
        if len(string)>=2:
            count=digits.count(string)
        else:
            count=0
        if count>=2:
            if (string,count) not in result:
                result.append((string,count))
        l+=1
        if p>len(digits):
            break
    return sorted(result,key=lambda x:(x[1],int(x[0])),reverse=True)


    pass


def test_repeats():
    assert [("12", 3), ("123", 2), ("67", 2), ("23",2)] == repeats("123451236786712")
    assert []==repeats("1")