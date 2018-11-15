#!/usr/bin/env python
#coding=utf-8

def extract_author(input_str):
    name_list = input_str.split(' ')
    #print(name_list)
    if len(name_list) == 1:
        first_name = ''
        last_name  = name_list[0]
    else:
        first_name = input_str.split(' ')[0]
        last_name  = input_str.split(' ')[1]
    return (last_name, first_name)

if __name__ == "__main__":
    main() 