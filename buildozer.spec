[app]

# (str) Judul aplikasi
title = UnityPy Swapper

# (str) Nama package (tanpa spasi)
package.name = unitypyswapper

# (str) Domain package
package.domain = org.modder

# (str) Berkas sumber kode aplikasi (dipisahkan koma)
source.include_exts = py,png,jpg,kv,atlas

# (list) Aplikasi membutuhkan modul apa saja?
requirements = python3,kivy,pillow,unitypy,cython

# (str) Versi aplikasi
version = 0.1

# (list) Izin aplikasi Android (Penting untuk akses file asset game)
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE

# (str) Target API Android
android.api = 33
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1
