# 🛒 Analisis Interaktif Transaksi E-Commerce

## 📌 Gambaran Umum Proyek

Proyek ini menyajikan analisis data interaktif dari dataset publik e-commerce asal Brasil, yang mengintegrasikan informasi pelanggan, pesanan, produk, ulasan, hingga pembayaran. Tujuan utama proyek ini adalah menggali wawasan mengenai perilaku pelanggan, tren pembayaran, performa pengiriman, sebaran penjual, serta hubungan antara harga dan tingkat kepuasan — semua dikemas dalam **dashboard dinamis berbasis Streamlit**.

## 🗂️ Ringkasan Dataset

Data yang digunakan berasal dari dataset e-commerce multi-tabel, yang mencakup:

* Informasi pelanggan
* Metadata produk (kategori, harga)
* Linimasa pesanan dan estimasi pengiriman
* Skor ulasan dan metode pembayaran
* Detail dan lokasi penjual

🔗 Sumber: [Brazilian E-Commerce Public Dataset](https://www.kaggle.com/olistbr/brazilian-ecommerce)

## 📊 Fitur Utama & Insight Dashboard

Dashboard memungkinkan pengguna untuk:

* Menyaring data berdasarkan **rentang tanggal pembelian** dan **metode pembayaran**
* Melihat perbandingan bulanan atas **total penjualan, jumlah pesanan, dan skor ulasan**
* Menganalisis **efisiensi pengiriman** (tepat waktu, lebih cepat, atau terlambat)
* Mengetahui **korelasi antara harga dan skor ulasan**
* Mengeksplorasi **distribusi skor ulasan berdasarkan kategori harga produk**
* Mengidentifikasi **kota dengan jumlah pelanggan dan penjual terbanyak**

## 📁 Struktur Direktori

```
ProjectDataAnalysis-DBS/
│── Dashboard/
│   ├── e-commerce_dashboard.py
│   ├── e-commerce_dataset.csv 
│
│── Data/ 
│   ├── customer_dataset.csv
│   ├── geolocation_dataset.7z
│   ├── order_items_dataset.csv
│   ├── order_payments_dataset.csv
│   ├── order_reviews_dataset.csv
│   ├── orders_dataset.csv
│   ├── product_category_name_translation.csv
│   ├── products_dataset.csv
│   ├── sellers_dataset.csv
│
│── e-commerce_analysis.ipynb 
│── requirements.txt      
│── url.txt 
│── README.md
```

## 🚀 Cara Menjalankan Dashboard

Ikuti langkah-langkah berikut untuk menyiapkan dan menjalankan dashboard Streamlit secara lokal:

### 1️⃣ Instalasi Python

Pastikan Python telah terinstal di perangkat Anda.

### 2️⃣ Instalasi Library yang Dibutuhkan

```bash
pip install -r requirements.txt
```

### 3️⃣ Clone Repository dari GitHub

```bash
git clone https://github.com/ilhamramadhan-m/ProjectDataAnalysis-DBS.git
```

### 4️⃣ Buat dan Aktifkan Virtual Environment

```bash
# Instal pipenv (jika belum ada)
pip install pipenv

# Buat dan aktifkan environment
pipenv install
pipenv shell
```

### 5️⃣ Masuk ke Direktori Dashboard

```bash
cd ProjectDataAnalysis-DBS/Dashboard
```

### 6️⃣ Jalankan Dashboard Streamlit

```bash
streamlit run e-commerce_dashboard.py
```
