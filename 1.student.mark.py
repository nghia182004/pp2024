def input_number_of_students():
    n=int(input("enter the number of students:"))
    return n

def input_students_information():
    
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth: ")

    return {'id': student_id, 'name': name, 'dob': dob, 'marks': {}}

def students_information(n,students):
    if n==0:
        print("no students")
    else:    
    
        for i in range(n):
          student = input_students_information()
          students.append(student)

        return students

def input_number_of_course():
    m=int(input("enter the number of courses:"))
    return m

def input_courses_information():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    
    return {'id': course_id, 'name': name}

def course_information(m,courses):
    if m==0:
        print("no courses")
    else: 

     for i in range(m):
        course = input_courses_information()
        courses.append(course)

     return courses

def input_mark(students,courses):
    select_course=input("select a course id:")

    for course in courses:
        if course['id']==select_course:
            for student in students:
                mark = input(f"enter the mark for student: {student['name']} : {(student['id'])} : ")
                student['marks'] = mark
            return
        else:
             print("course not found")
             break

def list_courses(courses):
    print("\nList of Courses:")
    for course in courses:
        print(f"{course['id']} : {course['name']}")

def list_students(students):
    print("\nList of students:")      
    for student in students:
        print(f"{student['id']} : {student['name']} : {student['dob']}")  

def list_marks(students,courses):
    select_course=input("enter a course to display:")

    for course in courses:
        if course['id']==select_course:
            for student in students:
                print(f"{student['id']} : {student['name']} : {student['marks']}")
            return        
        else: 
             print("no mark yet")
             break

def main():
    students = []
    courses = []
    number_of_students=0
    number_of_courses=0

    while True:
        print("\nOptions:")
        print("1. Input number of students")
        print("2. Input student information")
        print("3. Input number of courses")
        print("4. Input course information")
        print("5. Input marks for a course")
        print("6. List courses")
        print("7. List students")
        print("8. Show student marks for a course")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            number_of_students = input_number_of_students()
        elif choice == '2':
            students_information(number_of_students,students)
        elif choice == '3':
            number_of_courses = input_number_of_course()
        elif choice == '4':
            course_information(number_of_courses,courses)
        elif choice == '5':
            input_mark(students, courses)
        elif choice == '6':
            list_courses(courses)
        elif choice == '7':
            list_students(students)
        elif choice == '8':
            list_marks(students, courses)
        elif choice == '9':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()    

