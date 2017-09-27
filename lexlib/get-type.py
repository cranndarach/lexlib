#!/usr/bin/env python3

#import sys
# import numpy as np

# given a file organized with lines containing a target word and a neighbor
# wordlist = np.loadtxt('types-test.txt',dtype=str)
#wordlist = sys.argv[1]

def get_neighbor_types(neighbor_dict):
    types = {}
    base_words = neighbor_dict.keys()
    for i, j in wordlist: # where i is the target word and j is the neighbor
        if len(i) == len(j): # if they are the same length, the change was a substitution
            types.append([i,j,'S'])
        elif len(i) > len(j): # if the target is longer than the neighbor, the change was a deletion
            types.append([i,j,'D'])
        elif len(i) < len(j): # if the target is shorter than the neighbor, the change was an addition
            types.append([i,j,'A'])
        else: # just to be sure
            bad.append([i,j])
