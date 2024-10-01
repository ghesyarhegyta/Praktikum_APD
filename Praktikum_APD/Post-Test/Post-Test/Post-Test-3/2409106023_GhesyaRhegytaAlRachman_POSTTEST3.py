print("===== BMR PRIA ATAU WANITA =====")
print("1. Pria")
print("2. Wanita")
gender = input("Input jenis kelamin anda (1/2): ")


berat  = float(input("Input berat badan anda (kg): "))
tinggi = float(input("Input tinggi badan anda (cm): "))
umur   = int(input("Input umur anda: "))

if gender == "1":
    bmr = (10*berat)+(6.25*tinggi)-(5*umur)+5
elif gender == "2":
    bmr = (10*berat)+(6.25*tinggi)-(5*umur)-161


print("===== AKTIVITAS HARIAN =====")
print("1. Aktivitas Harian")
print("2. Aktivitas Sedang")
print("3. Aktivitas Tinggi")
aktivitas = input("Input pilihan aktivitas harian anda (1/2/3): ")

if aktivitas == "1":
    tdee = bmr*1.25

elif aktivitas == "2":
    tdee = bmr*1.36

elif aktivitas == "3":
    tdee = bmr*1.72
    
print(f"BMR anda adalah {bmr} kalori")
print(f"Kalori harian anda adalah {tdee} kalori")