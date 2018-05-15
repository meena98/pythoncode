__author__ = 'Kalyan'

notes = '''
Write your own implementation of converting a number to a given base. It is important to have a good logical
and code understanding of this.

Till now, we were glossing over error checking, for this function do proper error checking and raise exceptions
as appropriate.

Reading material:
    http://courses.cs.vt.edu/~cs1104/number_conversion/convexp.html
'''

def convert(number, base):
    """
    Convert the given number into a string in the given base. valid base is 2 <= base <= 36
    raise exceptions similar to how int("XX", YY) does (play in the console to find what errors it raises).
    Handle negative numbers just like bin and oct do.
    """
    if base<2:
        raise ValueError("base <2")
    if base > 36:
        raise ValueError("base >36")
    if type(number).__name__ == 'str' or type(base).__name__ == 'str':
        raise TypeError("invalid type")
    if number == None:
        raise TypeError("invalid type")
    res=''
    flag = 0
    if base == 2:
        while number != 0:
            if number & 1 == 1:
                res = '1' + res
            else:
                res = '0' + res
            number = number // 2
        return res
    if base == 16 or base ==20:
        if number<0:
            number = number * -1
            flag=1
        while number!=0:
            rem=number%base
            number=number//base
            if rem<10:
                res='rem'+res
            if rem == 10:
                res = 'A' + res
            if rem == 11:
                res = 'B' + res
            if rem == 12:
                res = 'C' + res
            if rem == 13:
                res = 'D' + res
            if rem == 14:
                res = 'E' + res
            if rem == 15:
                res = 'F' + res
            if rem == 16:
                res = 'G' + res
            if rem == 17:
                res = 'H' + res
            if rem == 18:
                res = 'I' + res
            if rem == 19:
                res = 'J' + res
            if rem == 20:
                res = 'K' + res
        if flag == 1:
            res = '-' + res
        return res
    else:
        while number!=0:
            rem = number % base
            number = number // base
            res = str(rem) + res
        return res
    pass


def test_convert():
    assert "100" == convert(4,2)
    assert "FF" == convert(255,16)
    assert "377" == convert(255, 8)
    assert "JJ" == convert(399, 20)
    assert "-JJ" == convert(-399, 20)

    try:
        convert(10,1)
        assert False, "Invalid base <2 did not raise error"
    except ValueError as ve:
        print(ve)

    try:
        convert(10, 40)
        assert False, "Invalid base >36 did not raise error"
    except ValueError as ve:
        print(ve)

    try:
        convert("100", 10)
        assert False, "Invalid number did not raise error"
    except TypeError as te:
        print(te)

    try:
        convert(None, 10)
        assert False, "Invalid number did not raise error"
    except TypeError as te:
        print(te)


    try:
        convert(100, "10")
        assert False, "Invalid base did not raise error"
    except TypeError as te:
        print(te)
