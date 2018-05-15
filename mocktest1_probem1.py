__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Given 2 strings str1 and str2, find out the minimum number of right rotations str1 needs to undergo
to create str2. If is not possible, return -1

Notes:
1. Assume inputs are either None or valid strings
2. Write plain brute force code.
3. result should be -1 if not possible
4. If it is possible then give the 'minimum rotations' required.
5. No need for type checking.
'''

def get_right_rotations(str1, str2):
    if len(str1)!=len(str2) and sorted(str1)!=sorted(str2):
        return -1
    dis=1
    count=0
    check=str1
    i=len(str1)-1
    j=len(str2)-1
    while(i>=0):
        if str1[i]==str2[j]:
            i=i-1
            j=j-1
        elif str1[i]!=str2[j]:
            i=i-1
            count+=1
    return count
    pass


# basic test given, write more tests to ensure correctness.
def test_get_right_rotations():
    assert 1 == get_right_rotations("abcd", "dabc")