__author__ = 'Kalyan'

notes = '''
Now we move on to writing both the function and the tests yourself.

In this assignment you have to write both the tests and the code. We will verify your code against our own tests
after you submit.
'''

# fill up this routine to test if the 2 given words given are anagrams of each other. http://en.wikipedia.org/wiki/Anagram
# your code should handle
#  - None inputs
#  - Case  (e.g Tip and Pit are anagrams)
def are_anagrams(first, second):
    import collections
    if first == None or second == None:
        return False
    if first == [] or second == []:
        return []
    if first =="" or second == "":
        return  False
    if type(first)!=str or type(second)!=str:
        return -1
    first = ''.join(e for e in first if e.isalnum())
    second = ''.join(e for e in second if e.isalnum())
    first = first.lower()
    second = second.lower()
    letters = collections.Counter(first)
    letters1 = collections.Counter(second)
    return letters==letters1
    pass


# write your own exhaustive tests based on the spec given
def test_are_anagrams_student():
    assert True == are_anagrams("pit", "tip") #sample test.
    assert True == are_anagrams("dormitory", "dirty room")
    assert True == are_anagrams("slot machines", "Cash Lost In Me!!")
    assert True == are_anagrams("Tom Marvolo Riddle", "I am Lord Voldemort")
    assert True == are_anagrams("O, Draconian devil!", "Leonardo Da Vinci")
    assert True == are_anagrams("Jim Morrison", "Mr. Mojo Risin '")
    assert True == are_anagrams("October Sky", "Rocket Boys")
    assert True == are_anagrams("Mother-In-Law", "Woman Hitler")
    assert True == are_anagrams("The end of the World is nigh!", "Down this hole, frightened.")
    assert False == are_anagrams(None, None)
    assert False == are_anagrams("", "tip")


# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_are_anagrams_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_are_anagrams(are_anagrams)
