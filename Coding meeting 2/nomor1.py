def entahlah(persen):
    if persen >= 90:
        print ("Excellent performance")
    elif persen >= 80:
        print ("Very Good performance")
    elif persen >= 70:
        print ("Good performance")
    elif persen >= 60:
        print ("Average performance")
    else:
        print ("Ngulang Matkulll")

persen = int(input("Masukkan Persen : "))       


Nilai = entahlah(persen)


