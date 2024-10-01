users = {"ghesya": "23"}

upayalogin = 0
maksimallogin = 3

while upayalogin < maksimallogin:
    print("===== LOGIN MENU =====")
    username = input("Input username anda: ")
    password = input("Input password anda: ")
    
    
    if username in users and users[username] == password:
        print("Login berhasil")
        break
    else:
        print("Username dan password yang dimasukkan tidak benar")
        upayalogin +=1
        print(f"Kesempatan login tersisa: {maksimallogin - upayalogin}")
        
if maksimallogin == upayalogin:
    print("Batas maksimal kesempatan login anda telah habis")
    
else:
    while True:
        print("===== BMR PRIA ATAU WANITA =====")
        print("1. Pria")
        print("2. Wanita")
        gender = input("Input jenis kelamin anda (1/2): ")
        
        berat  = float(input("Input berat badan anda (kg): "))
        tinggi = float(input("Input tinggi badan anda (cm): "))
        umur   = int(input("Input umur anda : "))
        
        if gender == "1":
            bmr = (10*berat)+(6.25*tinggi)-(5*umur)+5
        elif gender == "2":
            bmr = (10*berat)+(6.25*tinggi)-(5*umur)-161
            
        print("===== AKTIVITAS HARIAN =====")
        print("1. Aktivitas Minimal")
        print("2. Aktivitas Sedang")
        print("3. Aktivitas Tinggi")
        aktivitas = input("Input pilihan aktivitas harian anda (1/2/3)")
        
        if aktivitas == "1":
            tdee = bmr*1.25
        elif aktivitas == "2":
            tdee = bmr*1.36
        elif aktivitas == "3":
            tdee = bmr*1.72
            
        print(f"BMR anda adalah {bmr} kalori")
        print(f"Kebutuhan kalori harian anda adalah {tdee} kalori")
        
        respon = input("Apakah anda masih mau menghitung (y/n): ")
        if respon != "y":
            break
    print(f"Terima kasih sudah menggunakan kalkulator ini {username}")