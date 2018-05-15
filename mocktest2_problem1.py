max_marks = 20

problem_notes = '''
Given a sentence in which words are separated by spaces.

Re-arrange it so that words are reordered according to the following criteria.
 - longer words come before shorter words
 - if two words have same length, the one with smaller vowel occurance count comes first (feeel counts as 3 vowel occurances)
 - if even that is same, then order them lexicographically (case insensitive). For e.g. a comes before b

Constraints:
- Only allowed characters are a-zA-Z in the words
- raise a ValueError if the sentence contains any characters beyond the above
- raise a TypeError if input is not a string
- The result should preserve the words as is without changing case etc. but the sentence should be sorted so that
longer words precede shorter words. In case of tie, the word with fewer vowels comes first, if there is a tie even there,
preserve the original order.
- If there are multiple spaces, merge them into a single space in the result.
- If there is any leading or trailing space, remove it from the result.


Note: 
1. use the features of python to solve this problem, DON'T WRITE YOUR OWN SORT ROUTINE!
2. You can write additional routines as you see fit.


def transform(sentence):
    if type(sentence).__name__!='str':
        raise TypeError
    if sentence.isalpha():
        raise AttributeError
    mylist=sentence.split()
    mylist.sort(key=len,reverse=True)
    result=""
    #dictionary={}
    #for words in mylist:
        #dictionary[words]=len(words)
    temp=0
    while temp<len(mylist)-1:
        if len(mylist[temp])>len(mylist[temp+1]):
            result+=mylist[temp]
            result+=' '
            temp+=1
        elif len(mylist[temp])==len(mylist[temp+1]):
            temp1=temp+2
            check=[]
            check.append(mylist[temp])
            check.append(mylist[temp+1])
            while(temp1<=(len(mylist)-1) and len(mylist[temp])==len(mylist[temp1])):
                check.append(mylist[temp1])
                temp1+=1
                temp=temp1
            templ=sorted(check,key=lambda word: sum(ch in 'aeiou' for ch in word),reverse=True)
            for i in templ:
                result+=i+" "
    result+=mylist[len(mylist)-1]
    return result


    print (mylist)
    print(dictionary)
    pass
'''

def vowel(word):
    count=0
    for temp in word:
        if temp.lower() in "aeiou":
            count+=1
    return count

def transform(sentence):
    strlist=list(sentence.split())
    strlist.sort(key=lambda x:(-len(x),vowel(x),str.lower(x)))
    result= " ".join(strlist)
    return result


def test_transform():
    assert "elephant walking runway on" == transform("walking elephant on runway")
    transform("1asdf")