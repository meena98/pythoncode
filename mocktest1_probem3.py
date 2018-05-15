__author__ = 'Kalyan'

max_marks = 35 # 15 marks for encode and 20 for decode

problem_notes ='''
 This problem deals with number conversion into a custom base 5 notation and back.
 In this notation, the vowels a e i o u are used for digits 0 to 4.

 E.g. decimal 10 in this custom base 5 notation is "ia", decimal 5 is "ea" etc.

 Your job is to write encoding and decoding (both) routines to deal with this notation.
'''

# Notes:
# - If number is not a valid int raise TypeError
# - Negative numbers should result in a - prefix to the result similar to how bin works
#  use lower case letters in your result [aeiou].


def to_custom_base5(number):
    if number<0:
        flag=1
    d = {"0": "a", "1": "e", "2": "i", "3": "o", "4": "u"}
    result = ""
    num = ""
    flag=0
    if number < 0:
        flag = 1
    while number != 0:
        result = str(number % 5) + result
        number = number // 5
    for s in result:
        if s in d:
            num = num + d[s]
    if flag==1:
        return "-"+num
    return num
    pass

# Notes:
# - if s is not a string, raise TypeError
# - if the encoding is not right or empty string, raise ValueError
# - allow both - and + as prefixes which represent sign.
# - allow trailing and starting spaces (but not once the sign or number starts)
# - allow both capital and small letters.
# - return a int that corresponds to the number.

def from_custom_base5(s):
    if type(s)!=str:
        raise TypeError
    d = {"a":"0","e": "1","i":"2","o":"3","u":"4"}
    number=""
    result=0
    for temp in s:
        if temp in d:
            number=number+d[temp]
    n=int(number)
    digit = 0
    while n!=0:
        rem=n%10
        result+=rem*(5**digit)
        n=n//10
        digit+=1
    return result
    pass

# a basic test is given, write your own tests based on constraints.
def test_to_custom_base5():
    assert "ia" == to_custom_base5(10)

# a basic test is given, write your own tests based on constraints.
def test_from_custom_base5():
    assert 10 == from_custom_base5("ia")
