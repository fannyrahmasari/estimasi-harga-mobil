# 🚗 Prediksi Harga Mobil Bekas dengan Streamlit

Proyek ini merupakan aplikasi web sederhana yang dapat memprediksi harga mobil bekas berdasarkan beberapa fitur penting seperti tahun pembuatan, kilometer yang telah ditempuh, pajak tahunan, efisiensi bahan bakar (mpg), dan ukuran mesin (engine size). Aplikasi ini dibuat menggunakan **Python**, **Scikit-learn**, dan **Streamlit**.

## 📌 Tujuan Proyek
- Memprediksi harga mobil bekas secara akurat.
- Menyediakan antarmuka pengguna yang interaktif dan mudah digunakan.
- Menerapkan end-to-end pipeline machine learning, mulai dari training model hingga deployment ke web app.

---

## 🔧 Teknologi yang Digunakan

| Tools        | Keterangan                          |
|--------------|-------------------------------------|
| Python       | Bahasa pemrograman utama            |
| Scikit-learn | Untuk model Linear Regression       |
| Streamlit    | Untuk membangun web aplikasi        |
| Pickle       | Untuk menyimpan model yang dilatih  |
| Pandas       | Untuk manipulasi data               |
| Numpy        | Operasi numerik                     |

---

## ⚙️ Fitur Aplikasi

- Input data seperti:
  - Tahun mobil (`year`)
  - Kilometer tempuh (`mileage`)
  - Pajak tahunan (`tax`)
  - Konsumsi BBM (`mpg`)
  - Ukuran mesin (`engineSize`)
- Output prediksi harga mobil dalam mata uang:
  - **Pound Sterling (₤)**
  - **Rupiah (IDR)** *(dengan asumsi konversi)*

---

## 🚀 Cara Menjalankan Aplikasi

1. **Clone repo ini**
   git clone https://github.com/username/nama-repo.git cd nama-repo
   
2. **Install dependencies**  
Pastikan kamu berada di virtual environment, lalu:
pip install -r requirements.txt

3. **Jalankan aplikasi Streamlit**
streamlit run app.py

4. **Aplikasi akan terbuka di browser secara otomatis**  
Jika tidak, buka link seperti ini: [http://localhost:8501](http://localhost:8501)

---

## 🧠 Tentang Model

- Model yang digunakan: **Linear Regression**
- Model telah dilatih pada dataset mobil bekas dari UK.
- Model disimpan dalam file `estimasi_mobil.sav` menggunakan Pickle.
- Akurasi model ditampilkan menggunakan skor `R²`.

---

## 📷 Screenshot Aplikasi

![Tampilan Streamlit](screenshot.png)

---

## 📝 Catatan

- Nilai tukar Pounds ke Rupiah disimulasikan sebesar **1 GBP = 19,000 IDR**.
- Prediksi bersifat estimasi dan bisa bervariasi tergantung kondisi mobil sebenarnya.

---

## 🙌 Kontribusi

Saran, perbaikan, atau pengembangan lebih lanjut sangat terbuka!  
Silakan open issue atau buat pull request. 😊

---

## 📫 Kontak

Untuk kolaborasi atau diskusi lebih lanjut:  
📧 fannyrhmsri1102@gmail.com  
🌐 www.linkedin.com/in/fanny-rahmasari

---

## ⭐ Jangan lupa beri bintang repo ini jika bermanfaat!

