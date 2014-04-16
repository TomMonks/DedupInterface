#--------------------------------------------------------------------
#
#   Module:         difference
#   Description:    Difference between 2 reference lists
#   Author:         T.Monks
#   Python ver:     2.7.2
#
#   Logic:          
#--------------------------------------------------------------------

import string
import sys
from dedupFuncs import Results

def diff(refs, seen, idfun=None):
    """ Difference two reference files.
    seen is a set that contains depunctuated titles from another file
    This function is cery similar to unique_titles in dedupFuncs.
    The difference is that 'seen' is a parameter"""
    if idfun is None:
        def idfun(x): return x
    #seen = {}
    unique = Results()
   
    for item in refs:
        marker = idfun(item)
        if marker in seen:
            unique.duplicates.append(item)
            continue
        seen[marker] = 1
        unique.edit.append(item)

    return unique


#lambda x: x[len(x)-1:][0]

def create_seen_list(refs,  idfun=None):
    """returns a fast lookup list useful for differencing"""
    seen = {}

    if idfun is None:
        def idfun(x): return x

    for item in refs:
        marker = idfun(item)
        seen[marker] = 1

    return seen
    


