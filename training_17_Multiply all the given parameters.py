def mul(numbers):
    tmp = 1
    for i in numbers:
        tmp *= i
    return tmp


if __name__ == "__main__":
    assert mul([1, 2, 3]) == 6
    assert mul([0, 1, 2, 3]) == 0
    assert mul([2, 3, 4]) == 24