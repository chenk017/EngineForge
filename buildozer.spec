[app]

# (str) Judul aplikasi
title = UnityPy Swapper

# (str) Nama package (tanpa spasi)
package.name = unitypyswapper

# (str) Domain package
package.domain = org.modder

# (str) Direktori sumber kode (titik berarti direktori saat ini / root)
source.dir = .

# (str) Berkas sumber kode aplikasi (dipisahkan koma)
source.include_exts = py,png,jpg,kv,atlas

# (list) Aplikasi membutuhkan modul apa saja?
requirements = python3,kivy,pillow,unitypy,cython

# (str) Versi aplikasi
version = 0.1

# (list) Izin aplikasi Android (Penting untuk akses file asset game)
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE

# (str) Target API Android (Menggunakan API 34 yang stabil dan kompatibel)
android.api = 34
android.minapi = 21

# (str) Orientasi layar (portrait, landscape, all)
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1
