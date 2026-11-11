students = []

def display_menu():
    print("""
    1. Add Student
    2. View All Students
    3. Search Student by ID
    4. Update Student Marks
    5. Delete Student
    6. Display Grade Report
    7. Exit 
    """)

def add_student():
    while True:
        student_id = input("Enter Student ID:")

        id_exist=False

        for student in students:
            if (student_id == student["id"]):
                id_exist=True
                break
        if id_exist :
            print("Id already exist ")
        else:
            break   

    student_name = input("Enter Student Name:")    
    while True :
        marks = int(input("Enter Student Marks:"))

        if  0 <= marks <= 100 :
            break
        else:
            print("Invalid marks. Enter between 0 and 100.")

    students.append ({
        "id": student_id,
        "name": student_name,
        "marks": marks
            })
    print("Student Added successfully!")

def view_students():
    if not students:
        print("No students found")
    else:
        for student in students:
            print("Student ID:", student["id"])
            print("Student Name:", student["name"])
            print("Marks:", student["marks"])
            print("--------------------")

def search_student():
    search_id = input("Enter Student Id:")
    found=False
    
    for student in students:
        if (search_id == student["id"]):
            found=True
            print("Student ID:", student["id"])
            print("Student Name:", student["name"])
            print("Marks:", student["marks"])
            break
    if not found:
        print("Student not Found")

def update_marks():
    update_id = input("Enter Student id:")
    found=False
    
    for student in students:
        if (update_id == student["id"]):

            while True :
                new_marks =int(input("Enter New Marks:"))
                if  0 <= new_marks <= 100 :
                    student["marks"]= new_marks
                    print("Marks Updated Successfully")
                    break
                else:
                    print("Invalid marks. Enter between 0 and 100.")
            found=True
            break
    if not found:
        print("Student not Found")

def delete_student():
    delete_id= input("Enter Student id:")
    found = False
    
    for student in students:
        if(delete_id == student["id"]):
            found=True
            students.remove(student)
            print("Student Successfully Deleted")
            break

    if not found:
        print("Student not Found")

def grade_report():
    if not students:
        print ("No Students Found")
    
    else:
        top_student = students[0]
        total_marks=0
        total_students=0
        for student in students:
            marks= student["marks"]

            if 75 <= marks:
                grade="A"
            elif 65 <= marks:
                grade="B"
            elif 55 <= marks:
                grade="C"
            elif 35 <= marks:
                grade="S"
            else:
                grade="W"

            if student["marks"] > top_student["marks"]:
                top_student = student
            total_marks += student["marks"]
            total_students += 1
            print("Student Name:", student["name"])
            print("Marks:",student["marks"])
            print("Grade:",grade)
            
        print("Class Average", round(total_marks / total_students, 2))
        print("Top Performer:" ,top_student["name"])
        print("Highest Marks:" ,top_student["marks"])


while True:

    display_menu()

    choice = int(input("Enter your choice: "))


    if choice == 1:
        add_student()

    elif(choice==2):
        view_students()
     
    elif(choice==3):
        search_student()

    elif(choice==4):
        update_marks()
       
    elif(choice==5):
        delete_student()
        
    elif(choice==6):
        grade_report()

    elif(choice==7):
        print("Application Closed")
        break          
    
    else:
        print("Invalid choice")    
