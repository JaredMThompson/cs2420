from time import time
from bag import bag
from student import student

def main():
    b = bag()

    #Inserting
    t1 = time()
    with open ("Bag/FakeNames.txt", "r") as file:
        for line in file:
            student_info = line.split()
            s = student(student_info[0], student_info[1], student_info[2], student_info[3], student_info[4])
            error = b.insert(s)
            if error is False:
                print(f"Error: Item already in bag.\nCause: {s.first} {s.last}\nSSN: {s.ssn}\n")
    t2 = time()
    execution = t2-t1
    print(f"Inserting took {execution:.2f} seconds.")
    print(f"The size of the bag is {b.size()} items.\n")
    
    #Traversal/Iteration
    t1 = time()
    total_age = 0
    for item in b:
        total_age += int(item.age)
    avg_age = total_age/b.size()
    t2 = time()
    execution = t2-t1
    print(f"Traversal/Iteration took {execution:.2f} seconds.")
    print(f"The average age was {avg_age:.4f} years old.\n")

    #Deletion
    t1 = time()
    with open ("Bag/DeleteNames.txt", "r") as file:
        for line in file:
            ssn = line.strip()
            s2 = student("", "", ssn, "", "")
            error = b.delete(s2)
            if error is False:
                print(f"Error: Item not in bag.\nCause: {ssn}\n")
    t2 = time()
    execution = t2-t1
    print(f"Deletion took {execution:.2f} seconds.")
    print(f"The size of the bag is {b.size()} items.\n")

    #Retrival


    '''
    inserting
    open fakenames.txt
        read each line make a student with info from line
            put in bag or print error
    print time
    print size

    traverse/iterate

    for s in b:
        print(s)
        this will call iter for the bag class
    do this to find and pring average age

    delete

    with open delete names this is a txt file that has a list of what to be deleted i think
        for line in file:
            ssn = line.strip()
            s2 = student.student("",ssn,"","")
            ok = b.delete(s2)
            if !ok:
                print error
    print time
    print size

    '''

if __name__ == '__main__':
    main()