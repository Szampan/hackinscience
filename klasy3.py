import statistics

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []            
    def add_exam(self, mark):
        self.marks.append(float(mark))      
    def get_mean(self):  
        return statistics.mean(self.marks)
        
class School:
    def __init__(self, name):
        self.name = name
        self.students = []     
    def add_student(self, studentToAdd):
        self.students.append(studentToAdd)     
    def get_mean(self):
        self.students_means = []
        for i in self.students:
            self.students_means.append(i.get_mean())
        return statistics.mean(self.students_means)
          
    def get_best_student(self):
        # posortuj studentów wg imię.get_mean() albo:   <----można spróbować sortowaniem
        return sorted(self.students, key=lambda s:s.get_mean(), reverse=True)[0]

        # bestMean = 0
        # bestStudent = "press f in the chat"
        # for s in self.students:
        #     if s.get_mean() > bestMean:
        #         bestMean = s.get_mean()
        #         bestStudent = s
        # return bestStudent

class City:
    def __init__(self, name):
        self.name = name;    
        self.schools = []
       
    def add_school(self, school):
        self.schools.append(school)

    def get_mean(self):
        self.schools_means = []
        for i in self.schools:
            self.schools_means.append(i.get_mean())
        return statistics.mean(self.schools_means)

    def get_best_school(self):
        bestMean = 0
        bestSchool = "OMG"
        for school in self.schools:
            if school.get_mean() > bestMean:
                bestMean = school.get_mean()
                bestSchool = school
        return bestSchool

    def get_best_student(self):
        bestMean = 0
        bestCityStudent = "Davie 504"
        for school in self.schools:
            if school.get_best_student().get_mean() > bestMean:
                bestMean = school.get_best_student().get_mean()
                bestCityStudent = school.get_best_student()
        return bestCityStudent

##############TESTY######################
#########################################        
def main():
    alice = Student("krzysztof")    
    
    for mark in (1, 2, 69,):
        alice.add_exam(mark)
    
    print(alice.name)
    print(alice.marks)
    print(alice.get_mean())
    print("########")
###################################    
    hkis = School('hkis')
    paris = City('paris')
    paris.add_school(hkis)
 
    # Student("Bob").add_exam(420)
    # hkis.add_student("Cindy")       # <- 1. dziala, ale źle

    # student = Student("Anastazja")      
    # hkis.add_student(student)      # <- 2. działa dodaje do listy studenta jako OBIEKT (a nie tylko imię)
    # student = Student ("Beata")
    # hkis.add_student(student)

    for student_name, student_marks in (('alice', (1, 2, 3)),
                                        ('bob', (2, 3, 4)),
                                        ('catherine', (3, 4, 5)),
                                        ('daniel', (4, 5, 6))):
        student = Student(student_name)
        for mark in student_marks:
            student.add_exam(mark)
        hkis.add_student(student)

    
    print(hkis.name)
    print(hkis.students)

    print(hkis.students[3].name)
    print("Średnia ocen powyższego studenta: ", hkis.students[3].get_mean())    #   o kurwa
 ###########   

    print("###### Test średniej get_mean szkoły ######")
    print(hkis.get_mean())
 ###########   

    print("###### Test get_best_student szkoły ######")
    print(hkis.get_best_student().name)
 ###########   

    print("###### Test get_best_student miasta ######")
    print(paris.get_best_student().name)


#########################################    
if __name__ == '__main__':
    main()