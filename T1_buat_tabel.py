import sqlite3

nama_database = "mahasiswa.db"

# 1 membuat obyek koneksi (connection) dengan database
koneksi = sqlite3.connect(nama_database)
# 2 membuat obyek kursor (cursor) yang siap untuk mengeksekusi perintah sql
kursor = koneksi.cursor()
# 3 menyiapkan kueri, yaitu:
# membuat tabel, memasukkan data, dan melihat data
kueri_hapus_tabel = 'DROP TABLE IF EXISTS mahasiswa'
kueri_buat_tabel = '''CREATE TABLE IF NOT EXISTS mahasiswa(
                        nim INTEGER PRIMARY KEY,
                        nama TEXT,
                        alamat TEXT
                    )'''

kueri_tambah_data = '''INSERT INTO mahasiswa 
                        values("1", "Galih Hermawan", "Bandung"),
                        ("2", "Budi Santosa", "Jakarta"),
                        ("3", "Intan Permata", "Surabaya")'''

kueri_lihat_data = 'SELECT * FROM mahasiswa'
# 4 mengeksekusi kueri (bisa juga melewati langkah ke-3,
# dengan memasukkan langsung kueri sql di perintah execute)
kursor.execute(kueri_hapus_tabel)
kursor.execute(kueri_buat_tabel)
kursor.execute(kueri_tambah_data)
kursor.execute(kueri_lihat_data)
# 5 menerapkan setiap perubahan data ke dalam database
koneksi.commit()
# 6 mengambil data setelah dilakukan operasi seleksi
data_mahasiswa = kursor.fetchall()
# 7 menutup koneksi
koneksi.close()
# 8 melihat data
print(f'Data asli: {data_mahasiswa}')
print('\nData rapi.')
for dmhs in data_mahasiswa:
    print(f'NIM: {dmhs[0]}')
    print(f'Nama: {dmhs[1]}')
    print(f'Alamat: {dmhs[2]}\n')