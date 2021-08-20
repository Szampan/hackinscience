class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
    def przedstaw_sie(self):
        print(f"Jestem {self.imie} {self.nazwisko}. Mam {self.wiek} lat.")
    def urodziny(self):
        wiek_przed = self.wiek
        self.wiek += 1
        return wiek_przed
def main():
    # tworzymy dwa obiekty klasy Osoba
    Jan = Osoba("Jan", "Nowak", 48)
    Adam = Osoba("Adam", "Mickiewicz", 220)
    
    # wywołujemy metodę przedstaw_sie() na każdym z nich
    Jan.przedstaw_sie()
    Adam.przedstaw_sie()
    
    wiek_Adama_przed = Adam.urodziny()
    Adam.przedstaw_sie()
    print(f"Wiek Adama sprzed urodzin: {wiek_Adama_przed}")
    
    # odwołujemy się do pól, modyfikujemy je
    Jan.imie = "Stanisław"
    Jan.nazwisko = "Witkiewicz"
    Jan.wiek = 133
    
    Jan.przedstaw_sie()
if __name__ == "__main__":
    main()



#     import statistics

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.marks = []
#         #self.mean = 0        
        
#     def add_exam(self, mark):
#         self.marks.append(float(mark))  
    
#     def get_mean(self):  
#         return statistics.mean(self.marks)
#         # giving average of its results
        
# class School:
#     def __init__(self, name):
#         self.name = name
        
#     #def add_student(self, student):
     
#     #def get_mean(self):
#         # giving the average of the students averages
        
#     # get_best_student(self):
#         #returning the best student
        
# def main():
#     alice = Student("cindy")    
    
#     for mark in (1, 2, 69,):
#         alice.add_exam(mark)
    
#     print(alice.name)
#     print(alice.marks)
#     print(alice.get_mean())
    
    
# if __name__ == '__main__':
#     main()