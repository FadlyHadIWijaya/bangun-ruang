import fungsi as f

while True:
    try:

        f.Menu()
        f.Hitung()
    except ValueError:
        print('SALAH CUK')

    again = input("APAKAH ANDA MAU ULANG ? [y / n ]")
    if again == 'y' or again == 'Y':
        continue
    elif again == 'n' or again == 'N':
        break
    else:
        print(' KATA KUNCI SALAH ')
        break

print('TERIMA KASIHHH')
