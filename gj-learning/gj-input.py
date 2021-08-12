# Inputan dinamis

data = input("Masukkan data : ")

print("data berisi : ", data, " tipe = ", type(data))

# inputan dinamis dengan casting
angka1 = float(input("Masukkan nilai float : "))
print("data berisi : ", angka1, " tipe = ", type(angka1))

# untuk inputan nilai bool harus dicasting ke nilai int terlebih dahulu
biner = bool(int(input("Masukkan nilai boolean : ")))
print("data bernilai : ", biner, " dengan type ", type(biner))