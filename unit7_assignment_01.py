__author__ = 'Kalyan'

problem = """
 We are going to revisit unit6 assignment3 for this problem.

 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.


 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 This program should be written as a command line script. It takes one argument the input file of words and outputs
 <input>-results.txt where <input>.txt is the input file of words.
"""
import sys

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
    print(result)
    result.sort(key=lambda t: len(t),reverse=True)
    print(result)
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



if __name__ == "__main__":
    #cur_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    sys.argv.append('unit6_testinput_03.txt')
    sys.argv.append('unit6_testinput_03-results.txt')
    inFile = sys.argv[1]
    outfile=inFile[:inFile.find(".txt")]+"-results.txt"

    try:
        source = unit6utils.get_input_file(inFile)
        destination = unit6utils.get_temp_file(outfile)
        anagram_sort(source, destination)
    except:
        print("unsuccessfull")
    else:
        print("successfull")
    pass
    #sys.exit(main())