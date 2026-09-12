import sys
import csv
from math import log
from random import randint

def random_list(num):
    return [randint(0,num-1) for _ in range(num)]

def mostly_sorted(num):
    mostly_sorted_list = random_list(num)
    mostly_sorted_list.sort()
    (mostly_sorted_list[0], mostly_sorted_list[-1]) = (mostly_sorted_list[-1], mostly_sorted_list[0])
    return mostly_sorted_list

def bubble_sort(rand_list):
    work = 0
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(rand_list)-1):
            work += 1
            if rand_list[i] > rand_list[i+1]:
                sorted = False
                work += 1
                (rand_list[i],rand_list[i+1]) = (rand_list[i+1],rand_list[i])
    return work

def shaker_sort(rand_list):
    work = 0
    sorted = False
    right_sorts = 0
    left_sorts = 0
    while not sorted:
        sorted = True
        for i in range(len(rand_list)-1):
            work += 1
            if rand_list[i] > rand_list[i+1]:
                sorted = False
                work += 1
                (rand_list[i],rand_list[i+1]) = (rand_list[i+1],rand_list[i])
        right_sorts += 1
        if sorted:
             break
        for j in range((len(rand_list)-2)-right_sorts, left_sorts-1,-1):
             work += 1
             if rand_list[j] > rand_list[j+1]:
                sorted = False
                work += 1
                (rand_list[j],rand_list[j+1]) = (rand_list[j+1],rand_list[j])
        left_sorts += 1
    return work

def counting_sort(rand_list):
    work = len(rand_list)
    counter = [0] * len(rand_list)
    for i in range(len(rand_list)):
        work += 1
        counter[rand_list[i]] += 1
    replacement_index = 0
    for index, value in enumerate(counter):
        while value:
            #realized after submission that a for loop here is more efficent
            work += 1
            rand_list[replacement_index] = index
            replacement_index += 1
            value -= 1
    return work

def merge_sort(rand_list):
    work = 0
    if len(rand_list) == 1:
        return work
    else:
        left = rand_list[:(len(rand_list)//2)]
        right = rand_list[(len(rand_list)//2):]
        work_left = merge_sort(left)
        work_right = merge_sort(right)
        work += (work_left + work_right)
        i = 0
        j = 0
        k = 0
        while j < len(left) and k < len(right):
            if left[j] < right[k]:
                rand_list[i] = left[j]
                j += 1
            else:
                rand_list[i] = right[k]
                k += 1
            i += 1
            work += 1
        while j < len(left):
            rand_list[i] = left[j]
            j += 1
            i += 1
            work += 1
        while k < len(right):
            rand_list[i] = right[k]
            k += 1
            i += 1
            work += 1
        return work

def quick_sort(rand_list, mod = False, START = 0, STOP = -1):
    work = 0
    #Bart does the partion then move swap the pivot method
    if STOP == -1:
        STOP = len(rand_list)-1
    if START == STOP:
        return work
    if mod:
        work += 1
        (rand_list[START], rand_list[(STOP-START+1)//2+START]) = (rand_list[(STOP-START+1)//2+START], rand_list[START])
        #just swaps middle index to first index for pivot
    low = 0
    high = 0
    #starts at index 1, bc index 0 is pivot
    for i in range(1,STOP-START+1):
        work += 1
        if rand_list[START + i] <= rand_list[START]:
            work += 1
            (rand_list[START + i], rand_list[START + 1 + low]) = (rand_list[START + 1 + low], rand_list[START + i])
            low += 1
            #swaps the index we are currently looking at with the next position 
            #after the known lows then increases the amount of lows we know we have.
        else:
            high += 1
            #no need to swap just increase amount of known highs for recursive call later
    work += 1
    (rand_list[START], rand_list[START + low]) = (rand_list[START + low], rand_list[START])
    #swap pivot with the right most low
    if low:
        work_low = quick_sort(rand_list, mod, START, START + low - 1)
        work += work_low
    if high:
        work_high = quick_sort(rand_list, mod, START + low + 1, STOP)
        work += work_high
    return work

def moded_quick_sort(rand_list):
    return quick_sort(rand_list, True)

def main():
    sys.setrecursionlimit(5000)
    sorts = [bubble_sort, shaker_sort, counting_sort, merge_sort, quick_sort, moded_quick_sort]
    sort_types = [random_list, mostly_sorted]
    for sort_type in sort_types:
        data = [
                ["Power", "Bubble", "Shaker", "Counting", "Merge", "Quick", "M_Quick"]
            ]
        for power in range(3,13):
            size = 2 ** power
            row = [power]
            for sort in sorts:
                a = sort_type(size)
                work = sort(a)
                work = log(work, 2)
                work = round(work, 2)
                row.append(work)
            data.append(row)
        print(data)

        with open(sort_type.__name__+".csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)
    
if __name__ == '__main__':
    main()