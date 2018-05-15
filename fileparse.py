import os
import inspect

def open_input_file(file, mode="rt"):
    mod_dir = get_module_dir()
    test_file = os.path.join(mod_dir, file)
    return open(test_file, mode)

def get_module_dir():
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return mod_dir

def count_tests_in_file(file):
    f=open_input_file(file,'rt')
    lines,count=f.readlines(),0
    for line in lines:
        if line.startswith('def test'):
            count=count+1
    return count

def count_tests_lessons_assignments(file,list_data):
    if 'lesson' in file:                              #to check file name is lesson
        tests_count=count_tests_in_file(file)
        list_data[0]+=1
        list_data[2]+=tests_count
    elif 'assignment' in file:                        #to check file name is assignment
        tests_count=count_tests_in_file(file)
        list_data[1]+=1
        list_data[2]+=tests_count

def parse_files(all_py_files):
    '''units is dict to store info of lessons/assignments,tests of each unit, lst is to store [tot_lessons,tot_assignments,tot_tests] of each unit'''
    units, list1, prev_unit = {}, None, None
    for file in all_py_files:
        if file.startswith('unit'):
            unit_name = file[:5]
            if unit_name not in units:
                if list1 != None:
                    units[prev_unit] = list1
                units[unit_name] = list1
                list1 = [0, 0, 0]
            count_tests_lessons_assignments(file, list1)
            prev_unit = unit_name
    units[unit_name] = list1
    return units

def print_table(data):
    print('{0}        {1}     {2}'.format('unit','lesson-assign-tests','running-total'))
    for d in data:
        print(' '.join(str(x).ljust(17) for x in d))

def main():
    all_files=[file.name for file in os.scandir() if file.is_file()]
    all_py_files=list(filter(lambda file:file.endswith('.py'),all_files))
    dict_data=parse_files(all_py_files)  #stores unit_name as key and list containing ([tot_lessons,tot_assignments,tot_tests] as value
    final_output,temp=[],[0,0,0]     #final_o/p is  list of lists containing [unit_name,lessons/assignments/tests,running_total],temp is  to store previous run value
    for key in sorted(dict_data.keys()):
        lst = [x + y for x, y in zip(dict_data[key], temp)]
        final_output.append((key, dict_data[key], lst))
        temp=lst
    print_table(final_output)
    print('Done')

if __name__=='__main__':
    main()