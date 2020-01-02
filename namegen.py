#!/bin/python


import sys
from random import randint 
import string 


def gen_random_name():
    f = open('name_family.txt', 'r')
    name_list = f.readlines()
    f.close()
    index = randint(0, len(name_list)-1)
    name = name_list[index].strip()
    if name.startswith("#"):
        gen_random_name()
    else:
        return name.lower()
    
    
def gen_random_surname():
    if randint(0, 10)>5:
        f = open('name_girl.txt', 'r')
    else:
        f = open('name_male.txt', 'r')
    name_list = f.readlines()
    f.close()
    index = randint(0, len(name_list)-1)
    name = name_list[index].strip()
    if name.startswith("#"):
        gen_random_name()
    else:
        return name.lower()
    


def my_main():
    cmd='name'
    if len(sys.argv)>1:
        cmd = sys.argv[1]
    if (cmd == 'name'):
        print gen_random_name()
    if cmd == 'surname':
        print gen_random_surname()

        

if __name__ == "__main__":
    my_main()
