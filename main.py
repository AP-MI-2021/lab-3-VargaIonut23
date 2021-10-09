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

def test_is_all_prime ():
    assert is_all_prime([2,3,7,11]) is True
    assert is_all_prime([2,2,7,23]) is True
    assert is_all_prime([1,3,3,7]) is False
    assert is_all_prime([1,1,0,1]) is False

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

def test_au_toate_cifrele_prime ():
    assert au_toate_cifrele_prime (2223) is True
    assert au_toate_cifrele_prime(37533) is True
    assert au_toate_cifrele_prime(1073) is False
    assert au_toate_cifrele_prime(53217) is False


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

def toate_cifrele_prime(l):
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

def print_menu():
    print("1. Citire lista")
    print("2. Afisare cea mai lunga secventa de numere prime")
    print("3. Afisare cea mai lunga secventa de numere ale caror cifre sunt prime")
    print("4. Iesire")

def main():
    test_is_all_prime()
    test_au_toate_cifrele_prime()
    l = []
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == "1" :
            l = citire_lista()
        elif optiune == "2" :
            print(get_longest_all_primes(l))
        elif optiune == "3" :
            print(toate_cifrele_prime(l))
        elif optiune == "4" :
            break
        else  :
            print("Optiune gresita! Reincercati: ")

if __name__ == "__main__":
    main()