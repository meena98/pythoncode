__author__ = 'Kalyan'

notes = '''
 This problem will require you to put together many things you have learnt
 in earlier units to solve a problem.

 In particular you will use functions, nested functions, file i/o, functions, lists, dicts, iterators, generators,
 comprehensions,  sorting etc.

 Read the constraints carefully and account for all of them. This is slightly
 bigger than problems you have seen so far, so decompose it to smaller problems
 and solve and test them independently and finally put them together.

 Write subroutines which solve specific subproblems and test them independently instead of writing one big
 mammoth function.

 Do not modify the input file, the same constraints for processing input hold as for unit6_assignment_02
'''

problem = '''
 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 source - file containing words, one word per line, some words may be capitalized, some may not be.
 - read words from the source file.
 - group them into anagrams. how?
 - sort each group in a case insensitive manner
 - sort these groups by length (desc) and in case of tie, the first word of each group
 - write out these groups into destination
'''

import unit6utils
import string
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
    if letters==letters1:
        return 1
    else:
        return 0
    pass

def anagram_sort(source, destination):
    f = open(source, "r")
    temp=0
    list = []
    result=[]
    processed=[]
    tuple=()
    tup=0
    for line in f:
        if len(line) <= 1 or '#' in line:
            continue
        else:
            list.append(line.strip())
    for temp in range(len(list)):
        if list[temp] in processed:
            continue
        else:
            processed.append(list[temp])
            tuple+=(list[temp], )
            for temp1 in range (temp+1,len(list)):
                if list[temp1] in processed:
                    continue
                if (are_anagrams(list[temp], list[temp1])==1):
                    tuple+=(list[temp1], )
                    processed.append(list[temp1])
                else:
                    continue

            l=sorted(tuple,key=lambda x:(not x.islower(), x))
            result.append(l)
            tuple=()
    result.sort(key=lambda x: x[0].lower())
    result.sort(key=lambda t: len(t),reverse=True)
    f.close()

    op=open(destination,"w")
    str=""
    for temp in result:
        str+='\n'.join(temp)
        str+='\n'
        op.write(str)
        str=""
    op.close()




    pass

def test_anagram_sort():
    import sys
    print("sdv")
    print(sys.argv)
    source = unit6utils.get_input_file("unit6_testinput_03.txt")
    expected = unit6utils.get_input_file("unit6_expectedoutput_03.txt")
    destination = unit6utils.get_temp_file("unit6_output_03.txt")
    anagram_sort(source, destination)
    result = [word.strip() for word in open(destination)]
    expected = [word.strip() for word in open(expected)]
    assert expected == result
