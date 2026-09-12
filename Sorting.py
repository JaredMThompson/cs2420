from random import randint
import sys

def random_list(num):
    return [randint(0,num-1) for _ in range(num)]

def mostly_sorted(num):
    mostly_sorted_list = random_list(num)
    mostly_sorted_list.sort()
    (mostly_sorted_list[0], mostly_sorted_list[-1]) = (mostly_sorted_list[-1], mostly_sorted_list[0])
    return mostly_sorted_list

def bubble_sort(rand_list):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(rand_list)-1):
            if rand_list[i] > rand_list[i+1]:
                sorted = False
                (rand_list[i],rand_list[i+1]) = (rand_list[i+1],rand_list[i])
    return rand_list

def shaker_sort(rand_list):
    sorted = False
    right_sorts = 0
    left_sorts = 0
    while not sorted:
        sorted = True
        for i in range(len(rand_list)-1):
            if rand_list[i] > rand_list[i+1]:
                sorted = False
                (rand_list[i],rand_list[i+1]) = (rand_list[i+1],rand_list[i])
        right_sorts += 1
        if sorted:
             break
        for j in range((len(rand_list)-2)-right_sorts, left_sorts-1,-1):
             if rand_list[j] > rand_list[j+1]:
                sorted = False
                (rand_list[j],rand_list[j+1]) = (rand_list[j+1],rand_list[j])
        left_sorts += 1
    return rand_list

def counting_sort(rand_list):
    counter = [0] * len(rand_list)
    for i in range(len(rand_list)):
        counter[rand_list[i]] += 1
    replacement_index = 0
    for index, value in enumerate(counter):
        while value:
            #realized after submission that a for loop here is more efficent
            rand_list[replacement_index] = index
            replacement_index += 1
            value -= 1
    return rand_list

def merge_sort(rand_list):
    if len(rand_list) == 1:
        return rand_list
    else:
        left = merge_sort(rand_list[:(len(rand_list)//2)])
        right = merge_sort(rand_list[(len(rand_list)//2):])
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
        while j < len(left):
            rand_list[i] = left[j]
            j += 1
            i += 1
        while k < len(right):
            rand_list[i] = right[k]
            k += 1
            i += 1
        return rand_list

def quick_sort(rand_list, mod = False, START = 0, STOP = -1):
    #Bart does the partion then move swap the pivot method
    if STOP == -1:
        STOP = len(rand_list)-1
    if START == STOP:
        return
    if mod:
        (rand_list[START], rand_list[(STOP-START+1)//2+START]) = (rand_list[(STOP-START+1)//2+START], rand_list[START])
        #just swaps middle index to first index for pivot
    low = 0
    high = 0
    #starts at index 1, bc index 0 is pivot
    for i in range(1,STOP-START+1):
        if rand_list[START + i] <= rand_list[START]:
            (rand_list[START + i], rand_list[START + 1 + low]) = (rand_list[START + 1 + low], rand_list[START + i])
            low += 1
            #swaps the index we are currently looking at with the next position 
            #after the known lows then increases the amount of lows we know we have.
        else:
            high += 1
            #no need to swap just increase amount of known highs for recursive call later
    (rand_list[START], rand_list[START + low]) = (rand_list[START + low], rand_list[START])
    #swap pivot with the right most low
    if low:
        quick_sort(rand_list, mod, START, START + low - 1)
    if high:
        quick_sort(rand_list, mod, START + low + 1, STOP)
    return

def moded_quick_sort(rand_list):
    return quick_sort(rand_list, True)

def main():
    rand_list = random_list(10)
    sorted_list = (rand_list.copy())
    sorted_list.sort()
    sorted_bubble = bubble_sort(rand_list.copy())
    sorted_shaker = shaker_sort(rand_list.copy())
    sorted_counting = counting_sort(rand_list.copy())
    sorted_merge = merge_sort(rand_list.copy())
    sorted_quick = rand_list.copy()
    quick_sort(sorted_quick)
    sorted_mod = rand_list.copy()
    moded_quick_sort(sorted_mod)
    print("Original list:\n"  + str(rand_list))
    if sorted_list != sorted_bubble:
        print("Error on Bubble Sort")
    else:
        print("Success on Bubble Sort!\n" + str(sorted_bubble))
    if sorted_list != sorted_shaker:
        print("Error on Shaker Sort")
    else:
        print("Success on Shaker Sort!\n" + str(sorted_shaker))
    if sorted_list != sorted_counting:
        print("Error on Counting Sort")
    else:
        print("Success on Counting Sort!\n" + str(sorted_counting))
    if sorted_list != sorted_merge:
            print("Error on Merge Sort")
    else:
        print("Success on Merge Sort!\n" + str(sorted_merge))
    if sorted_list != sorted_quick:
            print("Error on Quick Sort")
    else:
        print("Success on Quick Sort!\n" + str(sorted_quick))
    if sorted_list != sorted_mod:
            print("Error on Moded Quick Sort")
    else:
        print("Success on Moded Quick Sort!\n" + str(sorted_mod))
    '''
    swaping/moving data and comparing data is work
    
    sys.recursionlimit(5000)

    sorts = [functions]
    for s in range(3,13):
        size = s ** 2
        print(s, end = "")
        for value in sorts:
            a = randlist(size)
            work = vlaue(a)
            work = log(work,2)
            print(work, end = "")
        print()
        

    make functions sort in place roather than returning the list. then do return work

    for counting
    len a work added at each step will be 3n at the end

    merge
    spliting in half is len a work


    '''
    
if __name__ == '__main__':
    main()