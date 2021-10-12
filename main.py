def is_prime(n):
    '''
    :param n: se va verifica daca n este prim
    :return: 1 daca n este prim ,0 in caz contrar
    '''
    if n < 2:
        return 0
    elif n == 2:
        return 1
    elif n % 2 == 0:
        return 0
    else:
        for i in range(3, n, 2):
            if n % i == 0:
                return 0
    return 1

def is_all_prime(l):
    '''
    determina daca toate elementele date sunt prime sau nu
    '''
    for i in l :
        if is_prime(i) == 0 :
            return  False
    return True

def test_get_longest_all_primes ():
    assert get_longest_all_primes([2 , 3 , 7 , 11]) == [2 , 3 , 7 , 11]
    assert get_longest_all_primes([2 , 2 , 7 , 23]) == [2 , 2 , 7 ,23]
    assert get_longest_all_primes([1 , 3 , 3 , 7]) == [3 , 3 ,7]
    assert get_longest_all_primes([1 , 1 , 0 , 1 ]) == []

def get_longest_all_primes(l):
    '''
    determina cea mai lunga segventa de numnere prime din vectorul dat
    '''
    subsecventa_max = []
    for i in range(len(l)):
        for j in range(i , len(l)+1):
            if(is_all_prime(l[i:j+1])) and len(l[i:j+1]) > len(subsecventa_max):
                subsecventa_max = l[i:j+1]
    return subsecventa_max

def test_get_longest_prime_digits():
    assert get_longest_prime_digits([2 , 2 , 2 , 3]) == [2 , 2 , 2 , 3]
    assert get_longest_prime_digits([1 , 2 , 7 , 9]) == [2 , 7]
    assert get_longest_prime_digits([2 , 2 , 7 , 5]) == [2 , 2 , 7 , 5]
    assert get_longest_prime_digits([1 , 3 , 5 , 7]) == [3 , 5 ,7]


def au_toate_cifrele_prime(n) :
    while n != 0 :
        c = n % 10
        if is_prime(c) == 0 :
            return False
        n = n // 10
    return True


def sunt_bune(l) :
    '''
    verifica daca toate numerele din secventa data au toate cifrele pare
    :param l: 
    :return: 
    '''
    for i in l :
        if au_toate_cifrele_prime(i) == 0 :
            return 0
    return 1


def get_longest_prime_digits(l):
    '''
    determina cea mai lunga secventa de numere a caror tuturor cifre sunt prime
    :param l: 
    :return: cea mai lunga secventa de numere a caror tuturor cifre sunt prime
    '''
    subsecventa_max = []
    for i in range(len(l)):
        for j in range(i , len(l)+1):
            if (sunt_bune(l[i:j + 1])) and len(l[i:j + 1]) > len(subsecventa_max):
                subsecventa_max = l[i:j + 1]
    return subsecventa_max


def citire_lista():
    l = []
    listasstring = input("Dati lista ")
    numberasstring = listasstring.split(",")
    for x in numberasstring:
        l.append(int(x))
    return l


def pare(l):
    '''
    determina daca toate numerele din secventa sunt pare
    :return:
    '''
    c = 0
    for i in l :
        if i % 2 == 1 :
            return 0
    return 1


def get_longest_all_even(l):
    '''

    :return: cea mai lunga secventa de numere pare
    '''
    subsecventa_max = []
    for i in range(len(l)):
        for j in range(i, len(l) + 1):
            if (pare(l[i:j + 1])) and len(l[i:j + 1]) > len(subsecventa_max):
                subsecventa_max = l[i:j + 1]
    return subsecventa_max


def test_get_longest_all_even():
    assert get_longest_all_even([ 2 , 4 , 6 ,22 , 3]) == [2 , 4 , 6 ,22]
    assert get_longest_all_even([4 , 6 ,23 , 1 , 1]) == [4 , 6]
    assert get_longest_all_even([3 , 1]) == []
    assert get_longest_all_even([22 , 24 , 88 , 54 , 24 , 56]) == [22 , 24 , 88 , 54 , 24 , 56]


def print_menu():
    print("1. Citire lista")
    print("2. Afisare cea mai lunga secventa de numere prime")
    print("3. Afisare cea mai lunga secventa de numere ale caror cifre sunt prime")
    print("4. Afisare cea mai lunga secventa de numere pare")
    print("5. Iesire")


def main():
    test_get_longest_all_primes()
    test_get_longest_prime_digits()
    test_get_longest_all_even()
    l = []
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == "1" :
            l = citire_lista()
        elif optiune == "2" :
            print(get_longest_all_primes(l))
        elif optiune == "3" :
            print(get_longest_prime_digits(l))
        elif optiune == "4" :
            print(get_longest_all_even(l))
        elif optiune == "5" :
            break
        else  :
            print("Optiune gresita! Reincercati: ")

if __name__ == "__main__":
    main()