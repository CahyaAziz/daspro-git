# Nama  : Cahya Abdul Aziz
# NIM   : 2404096
# Kelas : 1C

def hitungSelisih(jMulai, mMulai, dMulai, jDone, mDone, dDone):
    totalMulai = (jMulai * 3600) + (mMulai * 60) + dMulai
    totalDone = (jDone * 3600) + (mDone * 60) + dDone
    sisa = totalDone - totalMulai

    jam = sisa // 3600
    menit = (sisa % 3600) // 60
    detik = sisa % 60

    return f"Output: {jam} Jam - {menit} Menit - {detik} Detik"

print("Input Mulai:")
jMulai = int(input("Jam: "))
mMulai = int(input("Menit: "))
dMulai = int(input("Detik: "))
print("\nInput Selesai:")
jDone = int(input("Jam: "))
mDone = int(input("Menit: "))
dDone = int(input("Detik: "))

print("\nHitung Selisih:")
print(hitungSelisih(jMulai, mMulai, dMulai, jDone, mDone, dDone))

