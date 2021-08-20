def list_pretty_print(items):

    # robi nową podlistę z kolejnych 5 elementów, zaczynając od co piątego elementu
    chunks=[items[i:i+5] for i in range(0,len(items),5)]   


    for i in chunks:
        print(", ".join(str(j) for j in i))


if __name__ == "__main__":
    list_pretty_print([42] * 7)
    list_pretty_print([1,2,3,4,5,6,7])




    # a[start:stop]  # items start through stop-1
    # a[start:]      # items start through the rest of the array
    # a[:stop]       # items from the beginning through stop-1
    # a[:]           # a copy of the whole array

    # There is also the step value, which can be used with any of the above:

    # a[start:stop:step] # start through not past stop, by step
    # The key point to remember is that the :stop value represents the first value that is not in the selected slice. So, the difference between stop and start is the number of elements selected (if step is 1, the default).

    # The other feature is that start or stop may be a negative number, which means it counts from the end of the array instead of the beginning. So:

    # a[-1]    # last item in the array
    # a[-2:]   # last two items in the array
    # a[:-2]   # everything except the last two items
    # Similarly, step may be a negative number:

    # a[::-1]    # all items in the array, reversed
    # a[1::-1]   # the first two items, reversed
    # a[:-3:-1]  # the last two items, reversed
    # a[-3::-1]  # everything except the last two items, reversed