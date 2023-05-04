#!/usr/bin/env python3

def return_evens(num_list):
    new_list = [n for n in num_list if n % 2 == 0]
    return new_list


def make_exclamation(sentence_list):
    excited_list = [(f'{sentence}!') for sentence in sentence_list]
    return excited_list
