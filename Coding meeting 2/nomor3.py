def fibonacci(n):
    a, b = 0, 1
    hasil = []
    while a <= n:
        hasil.append(a)
        a, b = b, a + b
    return hasil


def print_fibonacci_up_to_n():
    n = int(input("Masukkan Nilai Maksimum: "))
    series = fibonacci(n)
    
    print(f"Fibonacci series up to {n}:")
    for number in series:
        print(number, end=" ")


print_fibonacci_up_to_n()