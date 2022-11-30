list = {}

while True:
    c = input("\n(T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar : ")

    # Menambahkan data
    if c.lower() == 't':
        print("Tambah Data")
        nama       = input("Nama           : ")
        nim        = int(input("NIM            : "))
        nilaiUTS   = int(input("Nilai UTS      : "))
        nilaiUAS   = int(input("Nilai UAS      : "))
        nilaiTugas = int(input("Nilai Tugas    : "))
        nilaiAkhir = (nilaiTugas * 30/100) + (nilaiUTS * 35/100) + (nilaiUAS * 35/100)
        list[nama] = [nim, nilaiTugas, nilaiUTS, nilaiUAS, nilaiAkhir]

    # Ubah data inputan
    elif c.lower() == 'u':
        print("Ubah Data")
        nama = input("Masukkan Nama  : ")
        if c.lower() == 't':
            print("Tambah Data")
            nama       = input("Nama           : ")
            nim        = int(input("NIM            : "))
            nilaiUTS   = int(input("Nilai UTS      : "))
            nilaiUAS   = int(input("Nilai UAS      : "))
            nilaiTugas = int(input("Nilai Tugas    : "))
            nilaiAkhir = (nilaiTugas * 30/100) + (nilaiUTS * 35/100) + (nilaiUAS * 35/100)
            list[nama] = [nim, nilaiTugas, nilaiUTS, nilaiUAS, nilaiAkhir]

        else:
            print("Nama {0} tidak ditemukan".format(nama))

    # Hapus inputan 
    elif c.lower() == 'h':
        print("Hapus Data")
        nama = input("Masukkan Nama  : ")
        if nama in list.keys():
            del list[nama]
        else:
            print("Nama {0} Tidak Ditemukan".format(nama))

    # Cari Inputan
    elif c.lower() == 'c':
        print("Cari Data")
        nama = input("Masukkan Nama : ")
        if nama in list.keys():
            print("\nNama        = {0}".format(nama))
            print("NIM         = {0}".format(nim))
            print("Nilai Tugas = {0}".format(nilaiTugas))
            print("Nilai UTS   = {0}".format(nilaiUTS))
            print("Nilai UAS   = {0}".format(nilaiUAS))                  
            print("Nilai Akhir = {0}".format(nilaiAkhir)) 
        else:
            print("Nama {0} Tidak Ditemukan".format(nama))

    # Keluar Program 
    elif c.lower() == 'k':
        break

    else:
        print("\nSilakan pilih menu yg tersedia")     