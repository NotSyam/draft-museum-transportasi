import asyncio
import os
import edge_tts

VOICE_TEACHER = "id-ID-GadisNeural"
VOICE_CERI = "id-ID-GadisNeural"
VOICE_RIO = "id-ID-ArdiNeural"

AUDIO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio")
os.makedirs(AUDIO_DIR, exist_ok=True)

SCRIPTS = {
    1: [
        {"voice": VOICE_CERI, "pitch": "+20Hz", "rate": "+4%", "text": "Halo teman-teman! Aku Ceri!"},
        {"voice": VOICE_RIO, "pitch": "+25Hz", "rate": "+4%", "text": "Dan aku Rio! Pagi ini kita mau jalan-jalan seru ke Museum Transportasi! Ayo ikut kami!"},
        {"voice": VOICE_RIO, "pitch": "+20Hz", "rate": "+2%", "text": "Wah, Ibu Guru! Kita pergi naik mobil besar ini ya?"},
        {"voice": VOICE_TEACHER, "pitch": "+0Hz", "rate": "-2%", "text": "Iya, Rio dan Ceri! Ini adalah bis sekolah kita."},
        {"voice": VOICE_CERI, "pitch": "+20Hz", "rate": "+4%", "text": "Hebat sekali! Bis ini panjang dan muat banyak sekali teman-teman!"},
        {"voice": VOICE_TEACHER, "pitch": "+0Hz", "rate": "-2%", "text": "Yuk anak-anak pintar di rumah, sentuh tombol setir bis di layar untuk membunyikan klakson dan berangkat!"}
    ],
    2: [
        {"voice": VOICE_TEACHER, "pitch": "+0Hz", "rate": "-2%", "text": "Horeee! Rio, Ceri, dan teman-teman sudah sampai di Museum Transportasi!"},
        {"voice": VOICE_CERI, "pitch": "+20Hz", "rate": "+4%", "text": "Wahhh, lihat! Pintunya besar-besar sekali dan ada lambang gambarnya!"},
        {"voice": VOICE_TEACHER, "pitch": "+0Hz", "rate": "-2%", "text": "Betul sekali, Ceri! Di lobi ini ada tiga gerbang sahabat mobil kita. Pintu satu berwarna Biru untuk mobil yang membawa orang. Pintu dua berwarna Merah bersirine untuk mobil penolong bahaya. Dan pintu tiga berwarna Oranye untuk mobil pembawa barang-barang berat!"},
        {"voice": VOICE_RIO, "pitch": "+25Hz", "rate": "+4%", "text": "Ibu Guru, kita masuk ke pintu mana dulu ya?"},
        {"voice": VOICE_TEACHER, "pitch": "+0Hz", "rate": "-2%", "text": "Ayo anak-anak di rumah, sentuh Pintu Satu yang berwarna Biru bergambar mobil penumpang untuk masuk!"}
    ],
    3: [
        {"voice": VOICE_TEACHER, "pitch": "+0Hz", "rate": "-2%", "text": "Selamat datang di Ruang Mobil Penumpang! Mobil penumpang adalah mobil yang bertugas membawa kita semua bepergian, seperti pergi ke sekolah, ke rumah nenek, atau bertamasya bersama keluarga!"},
        {"voice": VOICE_CERI, "pitch": "+20Hz", "rate": "+4%", "text": "Wahhh, mobil penumpangnya bagus-bagus sekali ya!"},
        {"voice": VOICE_RIO, "pitch": "+25Hz", "rate": "+4%", "text": "Ada bis Transjakarta yang panjang, ada mobil angkot keliling kota, dan ada mobil taksi yang lincah!"},
        {"voice": VOICE_TEACHER, "pitch": "+0Hz", "rate": "-2%", "text": "Coba anak-anak sentuh gambar bis Transjakarta, angkot, dan taksi untuk mendengar bunyi klaksonnya masing-masing! Asyik sekali! Setelah itu, sentuh tombol merah untuk lanjut ke Ruang Mobil Penyelamat!"}
    ],
    4: [
        {"voice": VOICE_RIO, "pitch": "+25Hz", "rate": "+4%", "text": "Wah, jadi mobil yang mengeluarkan bunyi sirine kencang itu namanya mobil penyelamat ya, Bu Guru?"},
        {"voice": VOICE_TEACHER, "pitch": "+0Hz", "rate": "-2%", "text": "Betul, Rio! Selamat datang di Ruang Mobil Penyelamat, pahlawan penolong saat bahaya! Ada mobil pemadam kebakaran dengan tangga panjang dan semprotan air, serta mobil ambulans yang membawa dokter dan ranjang pasien."},
        {"voice": VOICE_CERI, "pitch": "+20Hz", "rate": "+3%", "text": "Ceri pernah lihat di jalan waktu ambulans lewat, semua mobil lain pada minggir. Kenapa mobil lain minggir ya, Bu?"},
        {"voice": VOICE_TEACHER, "pitch": "+0Hz", "rate": "-2%", "text": "Pertanyaan pintar, Ceri! Mobil penyelamat membawa orang sakit dan pemadam api, jadi jalannya harus didahulukan agar cepat menolong orang lain! Yuk sentuh tombol sirine pemadam dan ambulans, lalu kita lanjut ke Ruang Mobil Pengangkut!"}
    ],
    5: [
        {"voice": VOICE_CERI, "pitch": "+20Hz", "rate": "+3%", "text": "Ibu Guru, kalau kita mau membawa kasur, lemari, atau pasir semen, apakah mobil biasa muat ya?"},
        {"voice": VOICE_TEACHER, "pitch": "+0Hz", "rate": "-2%", "text": "Tentu tidak muat, Ceri! Ada mobil khusus yang bertenaga super kuat untuk mengangkat barang-barang berat: namanya Mobil Pengangkut!"},
        {"voice": VOICE_RIO, "pitch": "+25Hz", "rate": "+4%", "text": "Brummm! Rodanya banyak sekali dan bodinya kuat sekali!"},
        {"voice": VOICE_TEACHER, "pitch": "+0Hz", "rate": "-2%", "text": "Ada mobil box pengantar paket kurir ke rumah, ada truk kontainer raksasa, dan ada dump truck yang bak belakangnya bisa miring mengangkat pasir! Sentuh mobil box dan dump truck untuk melihat aksinya, lalu sentuh tombol hijau untuk bermain kuis tebak mobil!"}
    ],
    6: [
        {"voice": VOICE_TEACHER, "pitch": "+0Hz", "rate": "-2%", "text": "Saatnya bermain Kuis Cerdas Ceria Sahabat Mobil! Bantu Rio dan Ceri yuk! Caranya sangat mudah: sentuh salah satu gambar mobil di bawah, lalu sentuh pos tujuannya yang cocok! Tarik bis ke halte orang, mobil pemadam ke gambar api, dan truk ke gambar pasir batu! Ayo pasangkan dengan tepat!"}
    ],
    7: [
        {"voice": VOICE_TEACHER, "pitch": "+0Hz", "rate": "-2%", "text": "Horeee! Selamat anak-anak hebat! Kalian sudah berhasil menyelesaikan seluruh petualangan di Museum Transportasi bersama Ceri dan Rio!"},
        {"voice": VOICE_RIO, "pitch": "+25Hz", "rate": "+4%", "text": "Sekarang kita sudah tahu tiga sahabat mobil: mobil penumpang, mobil penyelamat, dan mobil pengangkut!"},
        {"voice": VOICE_CERI, "pitch": "+20Hz", "rate": "+4%", "text": "Terima kasih sudah jalan-jalan dan bermain bersama kami ya teman-teman!"},
        {"voice": VOICE_TEACHER, "pitch": "+0Hz", "rate": "-2%", "text": "Kalian berhak mendapatkan Lencana Penjelajah Transportasi Cilik! Jangan lupa ajak ayah dan bunda mengklik tombol unduh untuk mencetak lembar mewarnai dan lencanamu! Sampai jumpa lagi!"}
    ]
}

async def generate_unit_audio(unit_num, segments):
    target_path = os.path.join(AUDIO_DIR, f"unit_{unit_num}.mp3")
    print(f"Generating Unit {unit_num} audio...")
    combined_bytes = bytearray()
    
    for idx, seg in enumerate(segments):
        communicate = edge_tts.Communicate(
            text=seg["text"],
            voice=seg["voice"],
            rate=seg.get("rate", "+0%"),
            pitch=seg.get("pitch", "+0Hz")
        )
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                combined_bytes.extend(chunk["data"])
    
    with open(target_path, "wb") as f:
        f.write(combined_bytes)
    print(f"Unit {unit_num} saved to {target_path} ({len(combined_bytes)} bytes)")

async def main():
    tasks = [generate_unit_audio(u, segs) for u, segs in SCRIPTS.items()]
    await asyncio.gather(*tasks)
    print("All audio generation complete!")

if __name__ == "__main__":
    asyncio.run(main())
