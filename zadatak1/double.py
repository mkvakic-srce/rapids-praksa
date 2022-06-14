# pomnozi listu brojeva s dva

if __name__ == '__main__':

    # definiraj listu brojeva od 1 do 10**8
    numbers = list(range(0, 10**8))
    numbers_double = numbers.copy()

    # izracunaj listu udvostrucenih brojeva - ovo treba for petljom
    for i in numbers_double:
        numbers_double[i] = i*2

    # isprintaj prvih pet brojeva u originalnoj i udvostrucenoj listi
    print(numbers[:5])
    print(numbers_double[:5])