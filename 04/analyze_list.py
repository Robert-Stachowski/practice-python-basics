def analyze_list(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    # byłem przekonany, 
    # że podstawiamy pod zmienną "numbers" liczby i operujemy na tej zmiennej, 
    # ale widzę ze jest tu trochę inaczej i definiujemy zmienne na obiekcie/nazwie funkcji na końcu przy wywołaniu,
    # natomiast sama zmienna zadeklarowana przy funkcji to jest tylko pojemnik na dane...
    # Uzupełnij kod, aby zwrócić długość listy, najmniejszą i największą liczbę
    return minimum, maximum, count
minimum, maximum, count = analyze_list([-4, 0, 4, 9, 14])
print(count, minimum, maximum)