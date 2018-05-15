__author__ = 'Kalyan'

notes = '''
1. Read instructions for the function carefully and constraints carefully.
2. Try to generate all possible combinations of tests which exhaustively test the given constraints.
3. If behavior in certain cases is unclear, you can ask on the forums
'''
from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists (string.split), only use string functions
# assume words are separated by a single space. you can use control flow statements
# So sentence is of form <blah> either <something> or <somethingelse> and gets converted to <blah> <something>
# if it is not of the correct form, you just return the original sentence.
def prune_either_or(sentence):
    if sentence==None:
        return None
    if 'neither' in sentence or 'nor' in sentence:
        return sentence
    if 'either' not in sentence or 'or' not in sentence:
        return sentence
    if sentence.count('either')>1:
        return sentence
    pos=sentence.find("either")
    if pos ==0:
        return sentence
    if sentence[pos+6]!=' ':
        return sentence
    pos1 = sentence.find("or")
    if pos1<pos:
        return sentence
    if sentence[pos1+2]!=' ':
        return sentence
    result=""
    result=sentence[0:pos]
    pos=pos+7
    if pos==pos1:
        return sentence
    result=result+sentence[pos:pos1-1]
    return result
    pass


def test_prune_either_or_student():
    assert "None" == prune_either_or("None")
    assert "we could either go either to a movie or a hotel" == prune_either_or("we could either go either to a movie or a hotel")
    assert "we could or either go to a movie or a hotel" == prune_either_or("we could or either go to a movie or a hotel")
    assert "we could either or go to a movie or a hotel" == prune_either_or(
        "we could either or go to a movie or a hotel")
    pass


# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_prune_either_or_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_prune_either_or(prune_either_or)
