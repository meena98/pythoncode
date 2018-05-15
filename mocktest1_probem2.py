__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Palindrome is a word which spells the same from both ends.

Create the smallest palindrome from a given word by appending characters to its end.

Examples:
- Malayalam -> Malayalam
- Malayal -> Malayalam (we want smallest palindrome)


Notes:
1. Don't change the letters of the initial word, only add new small letters
2. The palindrome is case-insensitive (ie) Tat is a valid palindrome
3. Only letters are allowed, any other characters should raise a ValueError
4. Non strings should raise a TypeError
5. Empty string is considered as a palindrome.
'''

def ispalindrome(word):
    reverse = ''.join(reversed(word))
    if word==reverse:
        return 1
    else:
        return 0

def smallest_palindrome(word):
   if word == "":
       return ""
   if type(word).__name__ != 'str':
       raise TypeError("invalid type")
   if not word.isalpha():
       raise ValueError("invalid")
   if len(word)==0 or len(word)==1:
       return word
   word = word.lower()
   temp=0
   length=len(word)
   while temp<=length-1:
       if (ispalindrome(word[temp:length])==1):
           temp1=word[0:temp]
           temp1=temp1[::-1]
           result=word+temp1
           return result
       else:
           temp+=1
   l=length-1
   w=word[0:l]
   word=word+w[::-1]
   if ispalindrome(word)==1:
       return word



# write your own tests
def test_smallest_palindrome():
    assert "malayalam"==smallest_palindrome("malayal")
    assert "a" == smallest_palindrome("a")

    pass
