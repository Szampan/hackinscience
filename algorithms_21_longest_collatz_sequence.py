def collatz_length(n):
    k = 0
    while n != 1:
        k += 1
        if n % 2 == 0:
            n /= 2
        else:
            n *= 3
            n += 1
    return k


if __name__ == "__main__":
    assert collatz_length(10) == 6