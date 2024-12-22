#!/usr/bin/env python3
num_list = [7,2,4,5,6,6]
def return_evens(num_list):
    return [num for num  in num_list if num%2==0]

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]

print(return_evens(num_list))