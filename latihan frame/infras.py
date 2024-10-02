import string
abjad = string.printable

def enkrip(pesan):
    global abjad

    key = int(input('Masukan Key  :'))
    cipher = ' ' #menampilkan chipher enkripsi sesuai kaidah chiper caesar
    for i in pesan:
        if i in abjad:
            k = abjad.find(i) #menentukan variable sebelumnya yang sudah dijadikan pemanggil
            k = (k + key) %100
            cipher = cipher+abjad[k]
        else:
            cipher = cipher + i
    return cipher
        
def dekrip(cipher):
            global abjad
            key = int (input('Masukan Key  :'))
            pesan = ' '#menampilkan pesan deskripsi sesuai kaidah chiper caesar
            for i in cipher:
                if i in abjad:
                    k = abjad.find(i)
                    k = (k - key)%100
                    pesan = pesan+abjad[k]
                else:
                    pesan = pesan + i
            return pesan
                
if __name__ == '__main__':
                print('--------------------------------------')
                print('-----2213030107 M Abdilah Saputra-----')
                print('--------------------------------------')

                option = int(input('1. Enkripsi\n2. Deskripsi\n pilih option   :'))
                if option == 1:
                    pesan = input('Masukan Pesan (Plaintext)     :')
                    print(enkrip(pesan))
                elif option == 2:
                     cipher = input('Masukan pesan (chipertext):')
                     print(dekrip(cipher))
                else:
                     print('Masukan option 1 atau 2!!')
    
