# 🚌 Modul Pembelajaran Interaktif: Study Tour Museum Transportasi
## "Mengenal 3 Sahabat Mobil Bersama Ceri & Rio"

Aplikasi media pembelajaran interaktif berbasis web (*standalone HTML5*) yang dirancang khusus untuk siswa-siswi Pendidikan Anak Usia Dini (PAUD) dan Taman Kanak-Kanak (TK) usia **5–6 tahun**.

---

## 🌟 Fitur Utama & Pendekatan Pedagogis

1. **Bebas Beban Membaca (*Zero-Reading Burden*):**
   - 100% narasi suara otomatis (*Edge-TTS*) oleh Ibu Guru, Ceri, dan Rio.
   - Piktogram dan gambar kendaraan berukuran besar dengan visual yang nyata dan bersahabat.
2. **Karakter Orisinal & Gaya Visual Grounded:**
   - Karakter **Ceri** dan **Rio** menggunakan aset asli tanpa modifikasi.
   - Seluruh aset visual lingkungan dan kendaraan dibuat dengan gaya **2D vector storybook realistis & grounded** (tidak terlalu colorful/rainbow berlebihan, tanpa wajah kartun aneh pada kendaraan).
3. **Efek Suara Riang (*Web Audio API* - Tanpa Dependensi):**
   - 📢 Klakson bis & taksi (*"Tut-tut! Tin-tin!"*)
   - 🚒 Sirine pemadam kebakaran (*"Nii-noo-nii-noo!"*)
   - 🚑 Sirine ambulans (*"Wiuw-wiuw-wiuw!"*)
   - 🚚 Gemuruh mesin truk & hidrolik bak dump truck
   - ⭐ Denting bintang magis & sorak tepuk tangan apresiasi
4. **Kuis Sentuh Ramah Motorik Anak (*Tap-to-Match*):**
   - Anak cukup menyentuh gambar mobil lalu menyentuh keranjang tugasnya (anti-gagal dan sangat cocok untuk layar sentuh tablet/iPad).
5. **Cetak Lencana & Lembar Mewarnai (*Print-to-PDF*):**
   - Dilengkapi tombol cetak instan format A4 Lanskap untuk memberikan apresiasi fisik yang dapat dibawa pulang ke rumah.
6. **Kompatibilitas Standalone & LMS:**
   - Dapat dibuka langsung dengan klik dua kali pada `index.html` di browser apa pun tanpa memerlukan server/instalasi.
   - Dilengkapi wrapper SCORM 1.2 untuk integrasi otomatis dengan LMS (Moodle, Canvas, dll.).

---

## 📁 Struktur Direktori

```
D:\Download\Museum Transportasi\
├── index.html                  # Aplikasi utama modul interaktif
├── generate_audio.py           # Script generator suara Edge-TTS
├── Ceri.jpg                    # Karakter asli Ceri
├── Rio.jpg                     # Karakter asli Rio
├── storyboard.html             # Naskah & spesifikasi instruksional
├── blocking.html               # Cetak biru spasial & tata letak
├── visual_asset.html           # Manifes aset visual & prompt
├── assets/                     # Koleksi gambar visual terintegrasi
│   ├── scene1_school_bus.jpg
│   ├── scene2_museum_lobby.jpg
│   ├── scene3_passenger_cars.jpg
│   ├── scene4_rescue_vehicles.jpg
│   ├── scene5_cargo_trucks.jpg
│   ├── scene7_museum_garden.jpg
│   ├── char_ibu_guru.jpg
│   ├── card_transjakarta.jpg
│   ├── card_fire_truck.jpg
│   └── card_dump_truck.jpg
├── audio/                      # Audio narasi per unit (MP3)
│   ├── unit_1.mp3
│   ├── unit_2.mp3
│   ├── unit_3.mp3
│   ├── unit_4.mp3
│   ├── unit_5.mp3
│   ├── unit_6.mp3
│   └── unit_7.mp3
└── README.md                   # Petunjuk penggunaan
```

---

## 🚀 Cara Menjalankan

1. **Jalankan Aplikasi:**
   - Cukup buka file `index.html` menggunakan browser modern (Google Chrome, Microsoft Edge, Safari, Mozilla Firefox).
2. **Uji Narasi Suara:**
   - Pastikan volume perangkat menyala. Suara pemandu Bu Guru dan anak-anak akan otomatis berputar pada setiap scene.
   - Anda juga dapat menekan tombol **"Ulangi Suara"** atau mengubah kecepatan pada bilah kontrol di bagian atas.
3. **Cetak Lencana:**
   - Di Scene 7, masukkan nama adik penjelajah cilik, lalu klik tombol **"Cetak Lencana & Mewarnai"** untuk mengunduh/mencetak dokumen PDF resmi.
