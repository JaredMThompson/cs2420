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
            success = b.insert(s)
            if success is False:
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
            temp = student("", "", ssn, "", "")
            success = b.delete(temp)
            if success is False:
                print(f"Error: Item not in bag.\nCause: {ssn}\n")
    t2 = time()
    execution = t2-t1
    print(f"Deletion took {execution:.2f} seconds.")
    print(f"The size of the bag is {b.size()} items.\n")

    #Retrival
    t1 = time()
    total_age = 0
    students_retrieved = 0
    with open ("Bag/RetrieveNames.txt", "r") as file:
        for line in file:
            ssn = line.strip()
            temp = student("", "", ssn, "", "")
            success = b.retrieve(temp)
            if success is False:
                print(f"Error: Item not in bag.\nCause: {ssn}\n")
            else:
                total_age += int(success.age)
                students_retrieved += 1
    avg_age = total_age/students_retrieved
    t2 = time()
    execution = t2-t1
    print(f"Retrival took {execution:.2f} seconds.")
    print(f"The average age was {avg_age:.4f} years old.\n")

if __name__ == '__main__':
    main()