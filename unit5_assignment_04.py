__author__ = 'Kalyan'

notes = '''
Implement a left binary search and write exhaustive tests for the same. Left binary search returns the index of left most
element when a search key repeats. For e.g if input is [1,2,3,3,4,4,5] and I search 3, it should return 2 as index 2 is
the left most occurance of 3.

In [1,1,1,1,1,1,1,1], I search for 1, you should return 0.

Note that we are looking for a binary search => we want not more than log(N) lookups, so a solution that involves finding
a random 1 and then doing a linear scan to the left is not a solution :).

- input is an indexable, value is any object.
- return -1 if not found or index of 1st occurance if found.
'''

def check(input):
    flag=0
    flag1=0
    for x in input:
        if type(x)==int or type(x)==float:
            if flag1==1:
                return -1
            elif flag==0:
                flag=1
        else:
            if flag==1:
                return -1
            elif flag1==0:
                flag1=1
    if flag==1 and flag1==0 or flag==0 and flag1==1:
        return 1
    else:
        return -1


def left_binary_search(input, value):
    if input == []:
        return -1
    if input == None:
        return -1
    if len(input)==1:
        if input[0]==value:
            return 0
        else:
            return -1
    a=check(input)
    if a==-1:
        return -1
    if type(input)==list:
        input.sort()
    low = 0
    high = len(input) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if value < input[mid]:
            high = mid - 1
        elif value == input[mid]:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result
    pass

# write your own exhaustive tests :)
def test_left_binary_search_student():
    assert 2 == left_binary_search([1,2,3,3,4,4,5],3)
    assert 0 == left_binary_search([1,1,1,1,1,1,1,1], 1)
    assert 4 == left_binary_search([1, 2, 3, 3, 4, 4, 5], 4)
    assert -1 == left_binary_search([1, 2, 3, 3, 4, 4, 5], 10)
    assert 3 == left_binary_search([-1, -2, -3, -3, -4, -4, -5,8], -3)
    assert 3 == left_binary_search(range(10), 3)
    assert 3 == left_binary_search(['a','b','c','d','f','a','g','c'],'c')
    assert 3 == left_binary_search(['ap', 'ball', 'col', 'def', 'fck', 'apl','gun', 'col'],'col')
    assert -1 == left_binary_search(['ap', 'ball', 'col', 'def', 'fck','apl', 'gun', 'col',4,5,6,6], 'col')
    assert -1 == left_binary_search([None,3,2,5,6,7,8,12,4,5,8,96,78,25,0,23,5,
                                    89,4,78,56,25,86,78,58,632,8,4,7,5,8,9,63,52,14,5,9.36,0.23,657,7,25], 8)
    pass


# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_left_binary_search_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_left_binary_search(left_binary_search)
