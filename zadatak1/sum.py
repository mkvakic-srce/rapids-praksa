# sum

if __name__ == '__main__':

    # definiraj listu brojeva od 1 do 10**8
    numbers = list(range(0, 10**8))

    sum = 0
    for i in numbers:
        sum = sum + i

    print(sum)
    