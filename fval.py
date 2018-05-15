from placeholders import *

import inspect
import os

import sys

import unit6utils
import string
import operator

def get_temp_dir():
    module_dir = get_module_dir()
    temp_dir = os.path.join(module_dir, "tempfiles")
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
    return temp_dir

def get_module_dir():
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return mod_dir

def open_input_file(file, mode="rt"):
    mod_dir = get_module_dir()
    test_file = os.path.join(mod_dir, file)
    return open(test_file, mode)

def open_temp_file(file, mode):
    data_dir = os.getenv("DATA_DIR", default=get_temp_dir())
    out_file = os.path.join(data_dir, file)
    return open(out_file, mode)

def check(word,fword):
    f=open('lowercase60k.txt','r')
    distance=0
    final=""
    for temp in f:
        friendword = 0
        if temp.strip()==word:
            continue
        else:
            for letter in temp.strip():
                friendword=friendword+ord(letter)
            if distance == 0:
                distance = abs(friendword - fword)
                final = temp
            else:
                if distance > abs(friendword - fword):
                    distance = abs(friendword - fword)
                    final = temp
    return final

def check1(word,fword,k):
    f = open('lowercase60k.txt', 'r')
    distance = 0
    final = ""
    dictionary={}
    for temp in f:
        friendword = 0
        if temp.strip() == word:
            continue
        else:
            for letter in temp.strip():
                friendword = friendword + ord(letter)
            dictionary[temp.strip()]=abs(friendword-fword)
    sorted_d = dict(sorted(dictionary.items(), key=operator.itemgetter(1)))
    return sorted_d







def fval(source,destination,k):
    file=open(source,"r")
    destination=open(destination,"w")
    #file = open_input_file("fval.txt")
    #destination = open_temp_file("destination.txt", 'w')
    #file=open(source,'r')
    words={}
    friendword=""
    fword=0
    if(k==1):
        for line in file:
            words = {}
            fword = 0
            word = line.strip()
            for letter in word:
                fword = fword + ord(letter)
            result = check(word, fword)
            words = {word: result}
            for key, value in words.items():
                destination.write('%s:%s' % (key, value))
        destination.close()
    else:
        for line in file:
            result1={}
            words = {}
            fword = 0
            word = line.strip()
            for letter in word:
                fword = fword + ord(letter)
            result1 = check1(word, fword,k)
            destination.write('%s:' % word)
            num=1
            for key,value in result1.items():
                if num>k-1:
                    destination.write('%s\n' % key)
                    break
                destination.write('%s '%key)
                num+=1
        destination.close()






if __name__ == "__main__":
    sys.argv.append('lowercase60k.txt')
    sys.argv.append('destination.txt')
    sys.argv.append(2)
    inFile = sys.argv[1]
    outfile = sys.argv[2]
    k=sys.argv[2]
    source = unit6utils.get_input_file(inFile)
    destination = unit6utils.get_temp_file(outfile)
    fval(source,destination,1)