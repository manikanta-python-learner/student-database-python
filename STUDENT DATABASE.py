students = []
while True:
 print("==============================")
 print(" STUDENT DATABASE")
 print("==============================")

 print("\n Available options")
 print("1. Add student ")
 print("2. view Student ")
 print("3. search student")
 print("4. Delete Student")
 print("5. update Student age")
 print("6. Total Students")
 print("7. Clear students")
 print("8. Exit ")
 
 choice = input("Enter Your option: ")
 
 
 if choice == "1":
     name=input("Enter Your name: ")
     age = int(input("Enter your age: "))
     
     student = {
         "name": name,
         "age": age
         }
     students.append(student)
     print("Student Added Successfully")
     
     
 elif choice == "2":
    for student in students:
        print("Name :",student["name"])
        print("age: ",student["age"])
        print("-" * 20)
        
        
 elif choice == "3":
     search_student = input("Enter student name to search: ")
     found = False
     
     for student in students:
         if student["name"]== search_student:
             print("Student Found")
             found = True
     if found == False :
        print("Student Not Found")
        
        
 elif choice == "4":
     delete_student = input("Enter name to delete: ")
     found = False
     for student in students:
         
         if student["name"] == delete_student:
             students.remove(student)
             print("Student Deleted Successfully")
             found = True
        
     if found == False:
             print("Student Not Found")
             

 elif choice == "5":
     update = input("Enter Student Name to update: ")
     found = False
     for student in students:
         
        if student["name"] == update:
            found = True
            new_age = int(input("Enter new age to update:"))
            student["age"] = new_age
            print("Age Updated Successfully")
            
     if found == False:
         print("Student Not Found")
         
 elif choice == "6":
     print("Total Students :",len(students))
     
 elif choice == "7":
     students.clear()
     print("All Students Cleared Succesfully")
                                                                   
 elif choice == "8":
     print("Thank you")
     break            
