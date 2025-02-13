from database import connect
from buku import Buku

def tambah_buku(judul,penulis,tahun,status):
    try:
        with connect() as conn: # Menggunakan 'with' agar tidak usah (conn.close()). jadinya otomatis menutup setelah selesai
            cursor = conn.cursor()

            cursor.execute("INSERT INTO buku (judul,penulis,tahun,status) VALUES (?,?,?,?)",
                        (judul,penulis,tahun,status))
            conn.commit()
            conn.close()
            print("Buku Berhasil Ditambahkan")
    except Exception as e:
        print("Terjadi kesalahan", e)

def tampilkan_buku():
    with connect() as conn: # Menggunakan 'with' agar tidak usah (conn.close()). jadinya otomatis menutup setelah selesai
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM buku")
        data = cursor.fetchall()

        if not data:
            print("Tidak ada buku dalam database")
        else:
            for row in data:
                buku = Buku(*row)
                print(buku)

def perbaharui_status(id_buku,status_baru):
    with connect() as conn: # Menggunakan 'with' agar tidak usah (conn.close()). jadinya otomatis menutup setelah selesai
        cursor = conn.cursor()
        # Pengecekan Apakah ID Buku Tersedia
        cursor.execute("SELECT * FROM buku WHERE id = ?",(id_buku))
        data = cursor.fetchone()
        if data:
            cursor.execute("UPDATE buku SET status = ? WHERE id = ?", (status_baru,id_buku))
            conn.commit()
            print(f"Status Buku {id_buku} diperbaharui menjadi {status_baru}")
        else:
            print(f"Buku Dengan ID {id_buku} Tidak Ditemukan!")

def hapus_buku(id_buku):
    with connect() as conn: # Menggunakan 'with' agar tidak usah (conn.close()). jadinya otomatis menutup setelah selesai
        cursor = conn.cursor()
        # Pengecekan Apakah ID Buku Tersedia
        cursor.execute("SELECT * FROM buku WHERE id= ?",(id_buku))
        data = cursor.fetchone()
        if data:
            cursor.execute("DELETE FROM buku WHERE id = ?",(id_buku))
            conn.commit()
            print(f"Buku ID {id_buku} berhasil dihapus.")
        else:
            print(f"ID Buku {id_buku} Tidak Ditemukan!.")
