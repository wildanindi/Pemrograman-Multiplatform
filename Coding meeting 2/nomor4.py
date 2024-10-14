def angkaganjil(n):
    print(f"angka ganjil sampai {n}:")
    for i in range(1, n+1):
        if i % 2 != 0:
            print(i, end=" ")


n = int(input("masukkan nilai maksimal: "))
angkaganjil(n)