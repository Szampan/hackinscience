import statistics

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []
        #self.mean = 0        
        
    def add_exam(self, mark):
        self.marks.append(float(mark))  
    
    def get_mean(self):  
        return statistics.mean(self.marks)
        # giving average of its results
        
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
        bestMean = 0
        bestStudent = "press f in the chat"
        for s in self.students:
            if s.get_mean() > bestMean:
                bestMean = s.get_mean()
                bestStudent = s
        return bestStudent

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