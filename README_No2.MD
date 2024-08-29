Struktur Modul

Modul ini memiliki struktur sebagai berikut:

ruangan_pemesanan/
│
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── master_ruangan.py
├── controllers/
│   ├── __init__.py
│   └── track_pemesanan.py
└── views/
    ├── ruangan.xml
    └── pemesanan.xml

File dan Deskripsinya
1. __manifest__.py
File manifest yang mendefinisikan metadata modul.

2. models/__init__.py
File ini mengimpor model Python.

3. models/master_ruangan.py
Model untuk mengelola data ruangan, pemesanan ruangan dan validasi

4. controllers/__init__.py
File ini mengimpor controller API.
from . import track_pemesanan

5. controllers/track_pemesanan.py
Controller API untuk melacak status pemesanan.

6. views/master_ruangan_views.xml
Tampilan untuk model master.ruangan.

7. views/pemesanan_ruangan_views.xml
Tampilan untuk model pemesanan.ruangan.

Cara Menjalankan Modul
Persiapkan Direktori Modul:

Salin folder ruangan_pemesanan ke dalam direktori addons Odoo Anda. Misalnya, jika direktori addons Anda adalah /opt/odoo/addons, salin folder ke /opt/odoo/addons/ruangan_pemesanan.
Update Daftar Modul:

Restart server Odoo Anda agar Odoo dapat mendeteksi modul baru:
sh
Copy code
sudo service odoo restart
Masuk ke antarmuka web Odoo, buka menu Apps, dan klik Update Apps List.
Instal Modul:

Setelah daftar modul diperbarui, cari modul Ruangan dan Pemesanan di daftar aplikasi.
Klik Install untuk menginstal modul.
Gunakan Modul:

Setelah modul diinstal, Anda akan melihat menu baru Master Ruangan dan Pemesanan Ruangan di antarmuka pengguna Odoo.
Anda dapat mengelola data ruangan dan pemesanan melalui menu ini.
Akses API:

Anda dapat mengakses API pelacakan status pemesanan dengan menggunakan URL berikut:
http://<your-odoo-instance>/api/track_pemesanan/<pemesanan_id>
Gantilah <your-odoo-instance> dengan URL Odoo Anda dan <pemesanan_id> dengan ID pemesanan yang ingin Anda lacak.
