from random import randint

def random_list(num):
    return [randint(0,num-1) for _ in range(num)]

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

def main():
    rand_list = random_list(10)
    sorted_list = (rand_list.copy())
    sorted_list.sort()
    sorted_bubble = bubble_sort(rand_list.copy())
    sorted_shaker = shaker_sort(rand_list.copy())
    sorted_counting = counting_sort(rand_list.copy())
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
    
if __name__ == '__main__':
    main()