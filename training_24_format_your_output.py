def list_pretty_print(items):
    formated = ""
    k = 0       # k, ponieważ lista podana w sposób ([42] * 6) nie podaje poprawnie indexów
    for i in items:
        if k == 0:
            formated += str(i)
            k+=1
        elif k % 5 != 0:
            formated += f", {i}"
            k+=1
        elif k % 5 == 0 and k != 0:
            formated += f"\n{i}"
            k+=1
    print(formated)


if __name__ == "__main__":
    list_pretty_print([42] * 6)
    list_pretty_print([1,2,3,4,5,6,7])