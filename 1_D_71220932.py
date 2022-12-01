print("Halo selamat datang di bioskop!")
def lokasi():
    1=XII Empire
    2=XII Amplaz
    3=XII JCM
    print("1) XXI Empire")
    print("2) XXI Amplaz")
    print("3) XXI JCM")
    milih=int(input("Masukkan pilihanmu:"))
        if milih<3:
            print("Pilihan tidak tersedia")
        else:
            lokasi()

def judulfilm():
    print("Mau nonton film apa nih? Ada film:")
    print("1. Frozen")
    print("2. Keramat")
    print("3. KKN di Desa Penari")
    pilihan=int(input("Pilih nomer film: "))
        if pilihan>=3:
            print("Pilihan tidak tersedia")
        else:
            judulfilm()

def bioskop():
    print("Mau nonton layar bioskop apa:")
    print("1. Reguler")
    print("2. Dolby Almos")
    print("3. Premier")
    milihlah=int(input("Pilih nomor tipe layar: "))
        if milihlah>=3:
            print("Pilihan tidak tersedia")
        else:
            bioskop()

print("Berapa banyak tiket?")

def jamNonton():
    print("Mau nonton jam berapa:")
    print("1. 12.32")
    print("2. 14.45")
    print("3. 16.55")
    print("4. 19.05")
    pilihlagi=int(input("Masukkan angka pilihan anda:"))
    if pilihlagi>=3:
        print("Pilihan tidak tersedia")
    else:
        jamNonton()

if(milih,pilihan,milihlah,pilihlagi<=3)
    print("oke berhasil!, silahkan dinikmati di jam")