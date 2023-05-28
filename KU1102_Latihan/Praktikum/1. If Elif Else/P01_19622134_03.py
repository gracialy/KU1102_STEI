print("Masukkan waktu berangkat Tuan Kil")
jam=int(input("Jam :"))
menit=int(input("Menit :"))
durasi=int(input("Masukkan lama penerbangan (menit):"))
timediff=int(input("Masukkan perbedaan waktu (menit):"))

jamsampai=705-((jam*60)+menit+durasi+timediff)
if(jamsampai>0):
    if(jamsampai<60):
        print("Tuan Leo berhasil menjemput Tuan Kil",jamsampai,"menit lebih awal")
    elif(jamsampai>=60):
        print("Tuan Leo berhasil menjemput Tuan Kil",int(jamsampai/60),"jam",(jamsampai-(int(jamsampai/60)*60))%60,"menit lebih awal")
elif(jamsampai==0):
    print("Tuan Leo berhasil menjemput Tuan Kil tepat waktu ")
elif(jamsampai<0):
    if(jamsampai>-60):
        print("Tuan Leo telah meninggalkan bandara selama",jamsampai%60,"menit")
    elif(jamsampai<=-60):
        print("Tuan Leo telah meninggalkan bandara selama",int(-jamsampai/60),"jam",(-jamsampai-(int(-jamsampai/60)*60))%60,"menit")

