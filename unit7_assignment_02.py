__author__ = 'Kalyan'

problem = """
Pig latin is an amusing game. The goal is to conceal the meaning of a sentence by a simple encryption.

Rules for converting a word to pig latin are as follows:

1. If word starts with a consonant, move all continuous consonants at the beginning to the end
   and add  "ay" at the end. e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

You job is to write a program that takes a sentence from command line and convert that to pig latin and
print it back to console in a loop (till you hit Ctrl+C).

e.g "There is, however, no need for fear." should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."
Note that punctuation and capitalization has to be preserved

You must write helper sub routines to make your code easy to read and write.

Constraints: only punctuation allowed is , and . and they will come immediately after a word and will be followed
by a space if there is a next word. Acronyms are not allowed in sentences. Some words may be capitalized
(first letter is capital like "There" in the above example) and you have to preserve its capitalization in the
final word too (Erethay)
"""

import sys

vowels=('a', 'e', 'i', 'o', 'u')
puntuation=(',','.',' ')

def changeword(temp,sentence):
    temp=temp.lower()
    string=temp[:-1]
    puntuation=temp[-1]
    if string[0] in vowels:
        return string+"ay"+puntuation
    else:
        for item in string:
            if item not in vowels:
                string=string[1:]+string[0]
            else:
                break
        return string+"ay"+puntuation


def change(temp,sentence):
    if temp[-1] in puntuation:
        return changeword(temp,sentence)
    temp=temp.lower()
    if temp[0] in vowels:
        return temp+"ay"
    else:
        for item in temp:
            if item not in vowels:
                temp=temp[1:]+temp[0]
            else:
                break
        return temp+"ay"


def piglatin(sentence):
    listsen=list(sentence.split())
    result=""
    flag=0
    first=0
    if sentence[0].isupper():
        flag=1
    for temp in listsen:
        if first==0:
            result = result +change(temp,sentence)
            first=1
        else:
            result+=' '
            result = result + change(temp, sentence)
    if flag==1:
        result=result[0].upper()+result[1:]
    return result

if __name__ == "__main__":
    sys.argv.append("There is, however, no need for fear.")
    result = piglatin(sys.argv[1])
    try:
        print (result)
    except KeyboardInterrupt:
        print("stopped")
        pass
    #sys.exit(main())
#if __name__ == "__main__":
    #pass
    #print(sys.argv)
    #sys.exit(main())