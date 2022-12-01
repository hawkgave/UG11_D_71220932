def ganjilgenap() :
    kata=(input("Masukkan kata :"))
    list=(kata)
    len(kata)
    if(len(kata)%2==0) :
        print("Huruf paling ujung pada kata", kata, "adalah", (kata[-3:len]))
    else :
        print("Huruf paling ujung pada kata", kata, "adalah",(kata[0:3]))
    return (kata)

ganjilgenap()

