# 📊 ExcelDataMerger

**ExcelDataMerger** adalah aplikasi berbasis Python untuk menggabungkan dan menata data dari beberapa file Excel (`.xlsx`) menjadi satu atau lebih file output, sesuai konfigurasi dan kebutuhan data. Aplikasi ini berjalan via CLI (Command Line Interface).

---

## 🔧 Fitur Utama

- ✅ **Pilih kolom/baris tertentu** dari sheet input.
- ✅ **Bersihkan data otomatis**: hapus spasi atau `'` di awal/akhir, tanpa ubah tipe data.
- ✅ **Mapping kolom fleksibel**: dari input ke output.
- ✅ **Isi otomatis** kolom tertentu berdasarkan sumber file (mis. `marketplace` = `A` jika dari `lap_penjualan1.xlsx`).
- ✅ **Deteksi data kosong wajib**: jika data penting hilang, dibuatkan workbook baru untuk pengisian manual.
- ✅ **Output rapi & tersortir**: misal, urut tanggal lalu berdasarkan `marketplace`.

---

## 📁 Struktur Direktori

```

ExcelDataMerger/
├── .venv/                # Virtual environment (tidak ikut Git)
├── input/                # Folder file Excel sumber
├── output/               # Hasil akhir dan file manual jika perlu
│   ├── hasil_merge.xlsx
│   └── Kode barang list.xlsx
├── config.json           # Konfigurasi kolom, sheet, mapping, autofill, dll
├── merge_excel.py        # Script utama
├── requirements.txt      # Daftar dependensi Python
├── .gitignore            # File untuk mengecualikan folder tertentu dari Git
└── README.md             # Dokumentasi proyek ini

````

---

## 🚀 Cara Instalasi

1. **Clone repository** ini dan pindah ke folder proyek:

```bash
git clone https://github.com/username/ExcelDataMerger.git
cd ExcelDataMerger
````

2. **Buat virtual environment** (opsional tapi disarankan):

```bash
python -m venv .venv
.\.venv\Scripts\activate  # Untuk PowerShell/Windows
```

3. **Install dependensi:**

```bash
pip install -r requirements.txt
```

---

## ▶️ Cara Menjalankan

1. Siapkan file Excel sumber di folder `input/`.
2. Atur konfigurasi mapping dan autofill di `config.json`.
3. Jalankan aplikasi:

```bash
python merge_excel.py
```

4. File hasil akan otomatis dibuat di folder `output/`.

---

## 📝 Contoh `config.json`

```json
{
  "sheets": [
    {
      "filename": "lap_penjualan1.xlsx",
      "sheet_name": "Sheet1",
      "columns_map": {
        "kode": "kode_barang",
        "nama": "nama_barang",
        "harga": "harga"
      },
      "auto_fill": {
        "marketplace": "A"
      }
    }
  ],
  "required_fields": ["kode_barang"],
  "output_sort": ["tanggal", "marketplace"]
}
```

---

## ⚙️ Kebutuhan Sistem

* Python 3.10 atau lebih baru
* pip (Python package manager)

---

## 📄 Lisensi

Proyek ini bersifat privat/internal. Hak cipta oleh pemilik repository.

---

## 🙋‍♂️ Bantuan

Silakan buka *Issue* jika mengalami error atau ingin mengusulkan fitur.
