import fitur

def menu():
    while True:
        print("===== PROJEK PERPUSTAKAAN FCTECH =====")
        print("1. Tambah aja Buku")
        print("2. Lihat Buku")
        print("3. Perbaharui Status Buku")
        print("4. Hapus Buku")
        print("5. Keluar")

        pilihan = input("Pilih menu(1/2/3/4/5) : ")

        if pilihan =="1":
            judul = input("Masukkan Judul Buku : ")
            penulis = input("Masukkan Nama Penulis Buku : ")
            try:
                tahun = int(input("Masukkan Tahun Terbit : "))
            except ValueError:
                print(f"Tahun Harus Berupa Angka!")
                continue

            status = input("Masukkan Status Buku (Tersedia/Dipinjam) : ").strip()
            if status not in["Tersedia","Dipinjam"]:
                print("Status Tidak Valid. Hanya Masukkan 'Tersedia' atau 'Dipinjam'.")
                continue


            fitur.tambah_buku(judul,penulis,tahun,status)
        
        elif pilihan =="2":
            fitur.tampilkan_buku()
        
        elif pilihan =="3":
            try:
                id_buku = int(input("Masukkan ID Buku yang ingin diubah Status : "))
            except ValueError:
                print("ID Buku Harus Berupa Angka!")
                continue
            status =input("Masukkan Status Buku (Tersedia/Dipinjam): ").strip().lower()
            if status not in["tersedia","dipinjam"]:
                print("Status Tidak Valid. Hanya masukkan 'Tersedia' atau 'Dipinjam'. ")
            
            fitur.perbaharui_status(id_buku,status)
        
        elif pilihan =="4":
            try:
                id_buku = int(input("Masukkan ID Buku yang ingin dihapus : "))
            except ValueError:
                print("ID Buku Harus Berupa Angka!")
            fitur.hapus_buku(id_buku)
        
        elif pilihan =="5":
            print("Aplikasi Perpustakaan FCTECH dimatikan.")
            break
        
        else:
            print("Pilihan Tidak Valid")

menu()
