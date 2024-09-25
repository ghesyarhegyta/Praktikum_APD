# ulang = 15
# for i in range(ulang):
#     print(f"perulangan ke-{srt(i)}")

# simpan = [12, "udin petot", 14.5, True, 'A']
# for i in simpan:
#     print(i, end=' ')
    
# for i in range(1, 10, 2): #(awal, akhir, lompatan)
#     print(i)
    
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} x {j} = {i * j}")
#     print()
    
# a = 10
# b = 7
    
# print(f"nilai a : {a} dan nilai b : {b}")

# print("nilai a: (a)")

# hitung = 0

# while True: #kondisi/syarat
#     hitung +=1 #hitung = hitung + 1
#     ulang = input("ulang lagi tidak? : ")
#     if ulang == "tidak" or ulang =="Tidak":
#         break
    
# print(f"total perulangan : {hitung}")

# print("Daftar bilangan ganjil dari 1-10")
# for item in range(10):
#     if item % 3 == 0:
#         continue
#     print(item)

# bilangan = 0
# while True:
#     angka = int(input("Masukkan angka: "))
#     if angka < 0:
#         break
#     bilangan += angka
    
# print("Total bilangan: " + str(bilangan))
    
# for i in range(1, 20, 3):
#     if i % 2 == 0:
#     print(i)

buah = ["apel", 'pisang', 'jeruk', 'melon', 'semangka']
buah_baru = []

for i in buah:
    if "a" in i:
        buah_baru.append(i)
        
print(buah_baru)

# buah_baru = [i for i in buah if "e" in i]