# 03
# menjemput tuan kil
'''edan iki nguli'''
'''more random test case on this would be good'''

# KAMUS
# jam, menit, lamaTerbang, bedaWaktu: int
# jamTerbang, menitTerbang: int
# jamSampai, menitSampai: int
# bedaAwal: bool
# jamBeda, menitBeda: int
# jamKompeng, menitKompeng: int
# tepatJam, tepatMenit: int
# awalJam, awalMenit: int
# telatJam, telatMenit: int

# INPUT
print("Masukkan waktu berangkat Tuan Kil")
jam=int(input("jam: "))
menit=int(input("menit: "))
lamaTerbang=int(input("Masukkan lama penerbangan (menit): "))
bedaWaktu=int(input("Masukkan perbedaan waktu (menit): "))

# ALGORITMA
# durasi terbang
jamTerbang=lamaTerbang//60
menitTerbang=lamaTerbang-(jamTerbang*60)

# waktu Kota A
jamSampai=jam+jamTerbang
menitSampai=menit+menitTerbang

print(f"{jamSampai}.{menitSampai}")

# perbedaan waktu
if (bedaWaktu<0):
    bedaAwal=True
    bedaWaktu=(-1)*bedaWaktu
else: # (bedaWaktu>=0)
    bedaAwal=False

jamBeda=bedaWaktu//60
menitBeda=bedaWaktu-(jamBeda*60)

# waktu Kota Kompeng
if(bedaAwal==True):
    jamKompeng=jamSampai-jamBeda
    menitKompeng=menitSampai-menitBeda
    if(menitKompeng<0):
        menitKompeng=(menitSampai+60)-menitBeda
        jamKompeng=(jamSampai-1)-jamBeda
else: # (bedaAwal != True)
    jamKompeng=jamSampai+jamBeda
    menitKompeng=menitSampai+menitBeda
    if (menitKompeng>=60):
        menitKompeng -= 60 # menitKompeng=menitKompeng-60
        jamKompeng += 1 # jamKompeng=jamKompeng+1

print(f"{jamKompeng}.{menitKompeng}")

# OUTPUT
tepatJam=11
tepatMenit=45

if ((jamKompeng<=tepatJam) and (menitKompeng<tepatMenit)):
    awalJam=tepatJam-jamKompeng
    awalMenit=tepatMenit-menitKompeng

    if (awalMenit<0):
        awalMenit=(menitKompeng+60)-tepatMenit
        awalJam=(jamKompeng-1)-tepatJam

    if ((awalJam!=0) and (awalMenit!=0)):
        print(f"Tuan Leo berhasil menjemput Tuan Kil {awalJam} jam {awalMenit} menit lebih awal.")
    elif((awalJam==0) and (awalMenit!=0)):
        print(f"Tuan Leo berhasil menjemput Tuan Kil {awalMenit} menit lebih awal.")
    elif((awalJam!=0) and (awalMenit==0)):
        print(f"Tuan Leo berhasil menjemput Tuan Kil {awalJam} jam lebih awal.")
elif((jamKompeng==tepatJam) and (menitKompeng==tepatMenit)):
    print(f"Tuan Leo berhasil menjemput Tuan Kil tepat waktu.")
else: # ((jamKompeng>tepatJam) or ((jamKompeng==tepatJam) and (menitKompeng>tepatMenit))):
    telatJam=jamKompeng-tepatJam
    telatMenit=menitKompeng-tepatMenit

    if(telatMenit<0):
        telatMenit=(menitKompeng+60)-tepatMenit
        telatJam=(jamKompeng-1)-tepatJam

    if ((telatJam!=0) and (telatMenit!=0)):
        print(f"Tuan Leo telah meninggalkan bandara selama {telatJam} jam {telatMenit} menit.")
    elif((telatJam==0) and (telatMenit!=0)):
        print(f"Tuan Leo telah meninggalkan bandara selama {telatMenit} menit.")
    elif((telatJam!=0) and (telatMenit==0)):
        print(f"Tuan Leo telah meninggalkan bandara selama {telatJam} jam.")
'''


'''
# 03 v.2
# contributor: Ervina
'''jika selang waktu, konversi menjadi detik cara universal yg ternyata efektif'''

print("Masukkan waktu berangkat Tuan Kil")
Jam     = int(input("jam     : "))
Menit   = int(input("menit   : "))
LamaPenerbangan = int(input("Masukkan lama penerbangan (menit)  : "))
PerbedaanWaktu  = int(input("Masukkan perbedaan waktu (menit)   : "))

WaktuA = ((Jam*60) + Menit + LamaPenerbangan + PerbedaanWaktu)
if WaktuA < 705 :
    Awal = 705 - WaktuA # 705=(11*60)+45
    if Awal >= 60 :
        j = Awal // 60
        m = Awal - (j*60)
        print("Tuan Leo berhasil menjemput Tuan Kil", j, "jam", m, "menit lebih awal.")
    else : 
        print("Tuan Leo berhasil menjemput Tuan Kil", Awal, "menit lebih awal.")
elif WaktuA > 705 :
    Awal = WaktuA - 705  
    if Awal >= 60 :
        j = Awal // 60
        m = Awal - (j*60)
        print("Tuan Leo telah meninggalkan bandara selama", j, "jam", m, "menit.")
    else : 
        print("Tuan Leo telah meninggalkan bandara selama", Awal, "menit.")
else : # (WaktuA=705)
    print("Tuan Leo berhasil menjemput Tuan Kil tepat waktu.")