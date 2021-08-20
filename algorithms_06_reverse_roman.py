#!/usr/bin/env python3

def from_roman_numeral(roman_numeral):
    signs = {
        "M": 1000, 
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50, 
        "XL": 40, 
        "X": 10, 
        "IX": 9, 
        "V": 5, 
        "IV": 4, 
        "I": 1
    }
    num = 0

    print("podana rzymska liczba: ", roman_numeral)
    
    while len(roman_numeral) != 0:
        for i in list(signs.keys()):
            print("szukane znaki: ", i)
            while roman_numeral.startswith(i):
                if roman_numeral.startswith(i):
                    num += signs[i]
                    roman_numeral = roman_numeral.replace(i, "", 1)
                    print(f"rzymska liczba po odjęciu {i}: ", roman_numeral)
                print(f"liczba arabska po dodaniu {i}: ", num)
    print("szukana liczba to: ", num)

    
    # print(list(signs.keys())[0])    # list()[] robi listę z kluczy słownika i pokazuje wybrany element
    # print(signs[list(signs.keys())[0]])
    
    

    # 1992 = MCMXCII

    #return ...

from_roman_numeral("V")



# if __name__ == "__main__":
#     # *assert* enable you to test your code and get feedback on several examples.
#     # Keeping or removing this code has no effect on your submission.
#     assert from_roman_numeral("V") == 5
#     assert from_roman_numeral("XX") == 20
#     assert from_roman_numeral("DCCC") == 800
#     assert from_roman_numeral("MMMM") == 4000