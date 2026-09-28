from time import time
from bag import bag
from student import student

def main():
    b = bag()
    t1 = time()
    with open ("Bag/FakeNames.txt", "r") as file:
        for line in file:
            s = student(line)
            error = b.insert(s)
            if error is False:
                print("Error item already in bag. Cause: " + s.first + " " + s.last)
    t2 = time()
    execution = t2-t1
    print(f"Inserting took {execution:.2f} seconds")
    print(f"The size of the bag is{b.size()} items")
    
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