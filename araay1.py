angka = []

# Meminta input pengguna
for i in range(5):
    elemen = int(input(f"masukan  angka ke-{i+1}: 1"))
    angka.append(elemen)
    
# Mengurutkan angka dalam array
angka.sort()

# Menampilkan aray yang sudah di urutkan
print(f"array yang sudah diurutkan: {angka}")    