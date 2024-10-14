def find_largest(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3
    return largest


num1 = int(input("Masukkan Nomor Pertama: "))
num2 = int(input("Masukkan Nomor Kedua: "))
num3 = int(input("Masukkan Nomor Ketiga: "))


largest = find_largest(num1, num2, num3)
print(f"Angka Terbesarnya adalah: {largest}")
#print("Angka Terbesarnya adalah:", largest)