list = {
    "Arii" : "081267888", "Dina" : "087677776"  
}
print("\nTampilkan kontak Aari :")
print(29*"=")
print(" {0:^2} |".format("Nama"), "Nomor Telepon")      
print("=============================")

# Tampilkan Kontak Ari
print(" {0:^2} |".format("Arii") ,list["Arii"],"\n")

# Tambah Kontak baru
list["Riko"] = "087654544"

# Ubah kontak dina dengan nomor baru
list["Dina"] = "088999776"

# Tampilkan semua Nama 
print("Tampilan semua Nama :")
print("=============================")
# Setelah di ubah
print(" {0:^2} |".format("Nama"), "Nomor Telepon")
print("=============================")

for x in list.keys():
    print(" {0:^2} |".format(x))
print("\n")

# Tampilkan Semua Nomor 
print("Tampilan semua Nomor :")
print("=============================")
# Setelah di ubah
print(" {0:^2} |".format("Nama"), "Nomor Telepon")
print("=============================")

for x in list.values():
    print(" {0:^2} |".format(x))
print("\n")


# Tampilkan daftar Nama & Nomor
print("Tampilan daftar Nama & Nomor :")
print("=============================")
# Setelah di ubah
print(" {0:^2} |".format("Nama"), "Nomor Telepon")
print("=============================")

for x, y in list.items():
    print(" {0:^2} |".format(x), (y))
print("\n")

# Menghapus Kontak Dina
print("Menghapus Kontak Dina :")
print(29*"=")
del list["Dina"]

print(" {0:^2} |".format("Nama"), "Nomor Telepon")
print("=============================")

for x, y in list.items():
    print(" {0:^2} |".format(x), (y))
print("\n")





