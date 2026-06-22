while True: 
    print("1. Add Student Detail")
    print("2. Delete Student Detail")
    print("3. Search Student Detail")
    print("4. View Student Detail")
    print("5. Exit")

    n=int(input("Select an option: "))
    
    if n > 5 or n<1:
        print("Please pick a valid option!")

    elif n == 1:
        a0=int(input("Enter Student's Roll number: "))
        a1=input("Enter Student's Name: ")
        a2=int(input("Enter Student's Class: "))
        a3=int(input("Enter Student's Maths Mark: "))
        a4=int(input("Enter Student's Science Mark: "))
        a5=int(input("Enter Student's English Mark: "))
        avg=round(((a3+a4+a5)/3),3)

        f=open("student.csv", "a")
        f.write(f"{a0},{a1},{a2},{a3},{a4},{a5},{avg}\n")
        f.close()
        print("Student Details Added Successfully!")

    elif n==2:
        delvalue=input("Enter The Roll Number of the Student: ")
        
        f=open("student.csv", "r")
        read=f.readlines()
        f.close()
        
        found = False
        
        for line in read:
            data = line.strip().split(",")
            if data[0] == delvalue:
                found = True
                
        if found == False:
            print("Student detail does not exist!")
            
        else:
            f=open("student.csv", "w")
            for line in read:
                data=line.strip().split(",")
                if data[0]!= delvalue:
                    f.write(line)
                    
        f.close()
        print("Student Detail Deleted Successfully!")

    elif n == 3:

        search = input("Enter Roll Number: ")

        f = open("student.csv", "r")
        read = f.readlines()
        f.close()

        found = False

        for line in read:

            data = line.strip().split(",")

            if data[0] == search:

                found = True

                print("Student Found!")
                print("Roll Number:", data[0])
                print("Name:", data[1])
                print("Class:", data[2])
                print("Maths:", data[3])
                print("Science:", data[4])
                print("English:", data[5])
                print("Average:", data[6])

        if found == False:
            print("Student does not exist!")

    elif n == 4:

        f = open("student.csv", "r")

        for line in f:
            print(line)

        f.close()

    else:
        print("Thank you for using Student Management System!")
        break
    


