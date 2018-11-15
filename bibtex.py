#!/usr/bin/env python
#coding=utf-8

def extract_author(input_str):

    if (',' in input_str):
        name_list = input_str.split(', ')
        #print(name_list)
        first_name = name_list[1]
        last_name  = name_list[0]
    else:
        name_list = input_str.split(' ')
    
        if len(name_list) == 1:
            first_name = ''
            last_name  = name_list[0]
        elif len(name_list) == 2:
            first_name = input_str.split(' ')[0]
            last_name  = input_str.split(' ')[1]
        elif len(name_list) == 3:
            first_name = "{} {}".format(name_list[0], name_list[1])
            last_name  = name_list[2] 
    return (last_name, first_name)

if __name__ == "__main__":
    main() 