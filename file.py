import os
import inspect
from os import listdir


def get_module_dir():
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return mod_dir

def open_input_file(file, mode="rt"):
    mod_dir = get_module_dir()
    test_file = os.path.join(mod_dir, file)
    return open(test_file, mode)

def counttest(file,list1):
    f = open_input_file(file)
    lines = f.readlines()
    for temp in lines:
        if temp.startswith("def test"):
            list1[2]+=1


def count(file,list1):
    if "lesson" in file:
        list1[0]+=1
    elif "assignment" in file:
        list1[1]+=1
    counttest(file,list1)

def parse(files):
    prev=[0,0,0]
    list1,filename,name,total=[0,0,0],"",[],[]
    dic={}
    for file in files:
        if file.startswith("unit"):
            filename=file[:5]
            if filename not in name:
                list2 = [(x + y) for x, y in zip(prev, list1)]
                total.append(list2)
                prev=list2
                name.append(filename)
                list1=[0,0,0]
                count(file,list1)
                dic[filename]=list1
            elif filename in name:
                count(file,list1)
                dic[filename]=list1
    print(dic,total,name)

def print(dic,total,name):
    for temp in dic.values():
        print("a")




def main():
    file=open_input_file("unit6_input_data.txt")
    lines=file.readlines()
    arr=os.listdir()
    pyfiles=[file for file in arr if file.endswith(".py")]
    parse(pyfiles)




main()