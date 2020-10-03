from models.Student import Student

def menu1():
    correct = False
    while correct==False:
        print("Please data below : ")
        nama = input("Input name : ")
        kelas = input("Input kelas : ")
        umur = input("Input umur : ")
        ipk = input("Input ipk : ")
        
        flag = input("Data is correct [Y | N]? ")
        correct = True if flag.upper()=='Y' else False
    
    print("Success insert new student !")
    student = Student(nama, kelas, umur, ipk)
    return student
    
def menu2(LIST):
    if LIST.__len__()==0:
        print("No student inserted")
    else:
        number = 1
        print('-'*92)
        print('|{:5} |{:40} |{:7} |{:4} |{:25} |'.format('No','Name','Class','Age','IPK'))
        print('-'*92)
        for s in LIST:
            print('|{:5} |{:40} |{:7} |{:4} |{:25} |'.format(number,s.nama,s.kelas,s.umur,s.ipk))
            print('-'*92)
            number+=1

def menu3():
    flagWrong = True
    if LIST_STUDENT.__len__()==0:
        print("No student inserted")
    else:
        while flagWrong:
            print("Choose Student want to be update")
            menu2()
            flag=int(input("Choose number : "))
            if flag>LIST_STUDENT.__len__() or flag <= 0:
                print("Wrong number")
            else:
                LIST_STUDENT[flag-1] = menu1()
                flagWrong=False

def menu4():
    print("Search Student by name")
    name = input("Input student name : ")
    TEMP_STUDENT = []
    for s in LIST_STUDENT:
        if name in s.nama:
            TEMP_STUDENT.append(s)
    if TEMP_STUDENT.__len__() == 0:
        print("Student not found")
    else:
        menu2(TEMP_STUDENT)

def menu5():
    print("Delete student")
    menu2(LIST_STUDENT)
    index = int(input("Choose number for delete student : "))
    if index > LIST_STUDENT.__len__() or index <= 0:
        print("Wrong number")
    else:
        del LIST_STUDENT[index-1]
    

def print_menu():
    print("Welcome to Databook Student")
    print("1. Insert New Student")
    print("2. Get AlL Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Delete Student")
    print("6. Exit")


menu = 0
LIST_STUDENT = []
while menu != 6:
    print_menu()
    menu = int(input("Choose menu : "))
    if menu==1:
        LIST_STUDENT.append(menu1())
    elif menu==2:
        print("List All Student")
        menu2(LIST_STUDENT)
    elif menu==3:
        menu3()
    elif menu==4:
        menu4()    
    elif menu==5:
        menu5()    
    
print("Thank you !")