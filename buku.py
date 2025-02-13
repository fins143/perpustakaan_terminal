class Buku:
    def __init__(self,id,judul,penulis,tahun,status):
        self.id = id
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.status = status
    
    def __str__(self):
        return f"{self.id}. {self.judul} - {self.penulis} - {self.tahun} - {self.status}"
        