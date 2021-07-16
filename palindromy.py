# sprawdzenie które słowo jest palindromem
# palindrom - słowo pisane w przud i od końca brzmi tak samo

def palindrome(lista):
    wynik = list()
    for text in lista:
        if text[::-1] == text:
            wynik.append(text)   
    return 'palindromy', wynik

zdanie = input('podaj zdanie: ') 
zdanie = zdanie.split()

print(palindrome(zdanie))
