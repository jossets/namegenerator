#!/bin/python


import sys
from random import randint 



def gen_random_name():
    f = open('name_family.txt', 'r')
    name_list = f.readlines()
    f.close()
    index = randint(0, len(name_list)-1)
    name = strip(name_list[index])
    if name.startswith("#"):
        gen_random_name()
    
    
    
def gen_random_surname():
    if randint(0, 10)>5:
        f = open('name_female.txt', 'r')
    else:
        f = open('name_male.txt', 'r')
    name_list = f.readlines()
    f.close()
    index = randint(0, len(name_list)-1)
    name = strip(name_list[index])
    if name.startswith("#"):
        gen_random_name()


cmd='name';
def my_main():
    if len(sys.argv)>1:
        cmd = sys.argv[1]
    if cmd == 'name':
        gen_random_name()
    if cmd == 'surname':
        gen_random_surname()

        

if __name__ == "__main__":
    my_main()
