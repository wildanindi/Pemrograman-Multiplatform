def pola(n):
    for i in range(1, n+1):
        for j in range(i):
            print(i, end=" ")  
        print() 


n = int(input("Masukkan Nilai n: "))
pola(n)