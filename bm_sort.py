#
#
#  --
#  --
#  --  bm_sort.py: sorting module
#  --
#  --  Use: >>> import bm_sort
#  --
#  --  Arguments: Lowest valid index (start with 0)
#  --             Highest valid index (NOT array length)
#  --
#  --  Methods (defined in that order):
#  --      bm_bubble_sort
#  --      bm_insertion_sort
#  --      bm_quicksort_stack
#  --      bm_quicksort_random
#  --      bm_quicksort_switch - don't use
#  --      bm_quicksort_rec - don't use
#  --      bm_issorted
#  --      bm_test
#  --
#  --  Georgios Drakopoulos 2022
#  --
#  --
#
#
import pandas
from cgi import test
import csv
import time
import random
import itertools
import numpy as np
import statistics as st
from enum import Enum
from collections import Counter

class bm_policy(Enum):
    MIDPOINT = 0     #standard midpoint selection (baseline)
    MEDIAN = 1       #median (baseline)
    MID_MEDIAN = 2   #median of a middle section (baseline)
    RANDOM = 3       #uniform random (stochastic baseline)
    CONVEX = 4       #random convex combination
    ALTERNATING = 5  #alternate between 0.4 and 0.6
    
 


def bm_bubble_sort(tab, low:int, high:int) -> None:
    """ bm_bubble_sort: Basic bubble sort """

    sorted = False

    if low < high:
        while not sorted:
            sorted = True
            for i in range(low, high):
                if tab[i] > tab[i+1]:
                    v = tab[i]; tab[i] = tab[i+1]; tab[i+1] = v
                    sorted = False
    return


def bm_insertion_sort(tab, low:int, high:int) -> None:
    """ bm_insertion_sort: Insertion sort - simple form """

    if low < high:
        for n in range(0,high-low+1):
            for i in range(n,0,-1):
                if tab[i-1] > tab[i]:
                    v = tab[i-1]; tab[i-1] = tab[i]; tab[i] = v
    return


def bm_quicksort_stack(tab, low:int, high:int) -> None:
    """bm_quicksort_stack: Quicksort - stack version

    """

    idx_stack = [(0, -1)]

    if high > low:
        while idx_stack:
            while low < high:
                mid = (low + high)//2
                pivot = tab[mid]
                pivot_elements = [v for v in tab[low:high+1] if v == pivot]
                lower_elements = [v for v in tab[low:high+1] if v < pivot]
                higher_elements = [v for v in tab[low:high+1] if v > pivot]
                new_high = low + len(lower_elements) - 1
                new_low = high - len(higher_elements) + 1
                tab[low:high+1] = list(itertools.chain(lower_elements, pivot_elements, higher_elements))
                list.append(idx_stack, (new_low, high))
                high = new_high
            low, high = idx_stack[-1]
            idx_stack = idx_stack[:-1]
    return


def bm_quicksort_random(tab, low:int, high:int,ipodiastimata:list,policy:bm_policy=bm_policy.RANDOM) -> None:
    """bm_quicksort_random: Randomized quicksort with stack

    """
    
    idx_stack = [(0, -1)]
    mid_elements = 16
    mid_distance = 0.25
    alt_excess =  0.6  #0.4 
    alt_excess_low = True
    pivot_idx = None
    depth = 0 
    ipodiastima = 0
    

    if high > low:
        while idx_stack: #SINEXIZO AN I STOIVA DNE INE KENI
            
            while low < high:
                
                if depth <=3  and depth >=1:
                    ipodiastima = high  - low + 1
                    #print(high, "tyoso")
                    #print(low,"INEE TO LOW")
                    ipodiastimata.append(ipodiastima)
                    
                    
                if bm_policy.MEDIAN == policy:
                    pivot = st.median(tab[low:high+1])
                    #print(pivot, "= pivot")
                    pivot_idx = None
                    #print((tab[low:high+1]))
                    #print(pivot)
                    #print(low,high)
                elif bm_policy.MID_MEDIAN == policy:
                    n = high - low + 1
                    if n >= mid_elements:
                        mid_low = int(low + mid_distance*n)
                        mid_high = int(high - mid_distance*n)
                        pivot = st.median(tab[mid_low:mid_high+1])
                        
                    else:
                        pivot = st.median(tab[low:high+1])
                    pivot_idx = None
                elif bm_policy.CONVEX == policy:
                    print("mpike in convex")
                    convex_low = np.random.uniform()
                    pivot_idx = int(convex_low*low + (1-convex_low)*high)
                elif bm_policy.ALTERNATING == policy:
                    pivot_idx = int(alt_excess*low + (1-alt_excess)*high) if alt_excess_low else int(alt_excess*high + (1-alt_excess)*low)
                    alt_excess_low = not alt_excess_low
                    #print("mpike sto aloternate")
                elif bm_policy.RANDOM == policy:
                    print("random")
                    pivot_idx = int(np.random.uniform(low, 1+high))
                    print(pivot_idx)
                    
                else:
                    pivot_idx = int(low+high)//2
                    
                if pivot_idx:
                    print("MPENI  STO  PIVODT[IDXP]")
                    pivot = tab[pivot_idx]
                
                
                #partition
                pivot_elements = [v for v in tab[low:high+1] if v == pivot]
                lower_elements = [v for v in tab[low:high+1] if v < pivot]
                higher_elements = [v for v in tab[low:high+1] if v > pivot]
                new_high = low + len(lower_elements) - 1
                new_low = high - len(higher_elements) + 1 #IPOLOGIZO TO LOW ORIO TOU DEXIOU
                tab[low:high+1] = list(itertools.chain(lower_elements, pivot_elements, higher_elements)) #ton arxiko pinaka den ton exo piraxei , sinenono ta 3 (voithitaka )dianismata
                list.append(idx_stack, (new_low, high))
                #edo thelo ton metriti +1
                depth += 1
                high = new_high #edo pao sto aristero melos
                #print(idx_stack)
                #analoga to vathos sti stoiva epistrefo mikos 
                
            
                
            low, high = idx_stack[-1] # VAZO TO LOW, HIGH STI TELEUTEA DIADA  I DIO AUTES GRAMMER ISODINAMOUN ME POP
            idx_stack = idx_stack[:-1] # OTI EXO IDI STI STOIVA -TIS TELEYTEAS TIMIS
            #metritis -1
            #depth -= 1  #autro to afairo gia na min mionete to depth.
            
            
            
    return 
    


def bm_quicksort_switch(tab, low:int, high:int, switch_size:int=32, secondary_sort=bm_insertion_sort) -> None:
    """bm_quicksort_switch: Quicksort switching to secondary sorting function

    """

    idx_stack = [(0, -1)]

    if high > low:
        while idx_stack:
            while low < high:
                if high - low <= switch_size:
                    secondary_sort(tab, low, high)
                    break
                else:
                    mid = (low + high)//2
                    pivot = tab[mid]
                    pivot_elements = [v for v in tab[low:high+1] if v == pivot]
                    lower_elements = [v for v in tab[low:high+1] if v < pivot]
                    higher_elements = [v for v in tab[low:high+1] if v > pivot]
                    if lower_elements:
                        new_high = low + len(lower_elements) - 1
                    else:
                        new_high = low
                    if higher_elements:
                        new_low = high - len(higher_elements) + 1
                    else:
                        new_low = high
                    tab[low:high+1] = list(itertools.chain(lower_elements, pivot_elements, higher_elements))
                    list.append(idx_stack, (new_low, high))
                    high = new_high
                    
            low, high = idx_stack[-1]
            idx_stack = idx_stack[:-1]
    return


def bm_quicksort_rec(tab, low:int, high:int) -> None:
    """bm_quickort_rec: Quicksort - recursive version
    """

    if high <= low:
        return
    elif high == 1 + low:
        if tab[low] > tab[high]:
            v = tab[low]; tab[low] = tab[high]; tab[high] = v
    elif (high == 2 + low) or (high == 3 + low) or (high == 4 + low):
        tab[low:high+1] = sorted(tab[low:high+1])
    else:
        mid = (low + high)//2
        pivot = tab[mid]
        pivot_elements = [v for v in tab[low:high+1] if v == pivot]
        lower_elements = [v for v in tab[low:high+1] if v < pivot]
        higher_elements = [v for v in tab[low:high+1] if v > pivot]
        new_high = low + len(lower_elements) - 1
        new_low = high - len(higher_elements) + 1
        tab[low:high+1] = list(itertools.chain(lower_elements, pivot_elements, higher_elements))
        bm_quicksort_rec(tab, low, new_high)
        bm_quicksort_rec(tab, new_low, high)
    return


def bm_issorted(tab) -> bool:
    """bm_issorted: Checks whether an array is sorted."""

    n = len(tab)
    for i in range(0, n-1):
        if tab[i] > tab[i+1]:
            return False
    return True

