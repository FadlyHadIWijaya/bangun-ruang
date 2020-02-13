class Menu:

    def __init__(self):
        print('RUMUS BANGUN DATAR')
        print('\t1.PERSEGI')
        print('\t2.PERSEGI PANJANG')


class Hitung:

    def __init__(self):
        user = input('MASUKAN PILIHAN  [1/2] : ')

        if user == '1':
            Persegi()
        elif user == '2':
            PersegiPanjang()
        else:
            print("KATA KUNCI YANG ANDA MASUKAN SALAH!!!!!")


class Persegi:

    def __init__(self):
        a = float(input(' MASUKAN SISI  : '))
        hasil = float(a ** 2)
        print('HASIL LUAS PERSEGI ADALAH : ', hasil)


class PersegiPanjang:

    def __init__(self):
        a = float(input(' MASUKAN SISI PERTAMA  : '))
        b = float(input('MASUKAN SISI KEDUA : '))
        hasil = float(a * b)
        print('HASIL LUAS PERSEGI ADALAH : ', hasil)
