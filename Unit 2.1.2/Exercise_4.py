# Gets the student name by ID

class Student:
    
    def __init__(self, name, student_id):
        self.name = name
        
        self.student_id = student_id


def find_student_by_id(students, search_id):
    for i in range(0, len(students)):
        
        if students[i].student_id == search_id:
            return students[i]

# Added another student with the missing ID
students = [Student("Alice", 42), Student("Bob", 87), Student("George", 5)]

# Could've also removed the id 5 from the array.
search_ids = [42, 5, 87]

for i in range(0, len(search_ids)):
    student = find_student_by_id(students, search_ids[i])
    
    print("The student with id " + str(search_ids[i]) + " is " + student.name)