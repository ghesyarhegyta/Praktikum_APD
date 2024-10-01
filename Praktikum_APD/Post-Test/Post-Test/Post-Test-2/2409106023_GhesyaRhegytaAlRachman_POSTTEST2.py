nama_lengkap    = str(input("Input nama lengkap anda: "))
nama_panggilan  = str(input("Input nama panggilan anda: "))
nim             = int(input("Input NIM anda: "))
prodi           = str(input("Input asal prodi anda: "))
umur            = int(input("Input umur anda: "))
berat_badan     = float(input("Input berat badan anda: "))
dua_digit_nim   = int(input("Input dua digit angka dibelakang nim anda: "))
mod             = 6

print(f"Nama lengkap saya adalah {nama_lengkap} dengan nim {nim} prodi {prodi}, saya biasa dipanggil {nama_panggilan} sekarang saya berumur {umur} tahun dan berat badan saya adalah {berat_badan} berikut adalah hasil dari dua digit angka dibelakang nim saya jika dimodulus dengan {mod} adalah {dua_digit_nim%mod}")