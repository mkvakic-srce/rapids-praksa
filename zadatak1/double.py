# pomnozi listu brojeva s dva
def double(numbers):
    doubled = []
    for number in numbers:
        double = number*2
        doubled.append(double)
    return doubled

if __name__ == '__main__':

    # definiraj listu brojeva od 1 do 10**8
    n = 10**8
    numbers = list(range(n))

    # izracunaj listu udvostrucenih brojeva
    doubled = double(numbers)

    # isprintaj prvih pet brojeva u originalnoj i udvostrucenoj listi
    print('numbers : %s' % numbers[:5])
    print('doubled : %s' % doubled[:5])
