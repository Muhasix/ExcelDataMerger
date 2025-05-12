import os
import json
import pandas as pd

# Baca konfigurasi
with open("config.json", encoding="utf-8") as f:
    config = json.load(f)

all_data = []
input_folder = "input"

# Proses setiap sumber data
for sheet_cfg in config["sheets"]:
    path = os.path.join(input_folder, sheet_cfg["filename"])
    df = pd.read_excel(path, sheet_name=sheet_cfg["sheet_name"])

    # Ganti nama kolom
    df = df.rename(columns=sheet_cfg["columns_map"])

    # Bersihkan isi kolom string
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].map(lambda x: str(x).strip().strip("'") if isinstance(x, str) else x)

    # Auto-isi kolom jika diset
    for col, val in sheet_cfg.get("auto_fill", {}).items():
        df[col] = val

    all_data.append(df)

# Gabungkan semua data
result = pd.concat(all_data, ignore_index=True)

# Cek kolom wajib
for required in config.get("required_fields", []):
    if required not in result.columns:
        criteria_cols = ["nama_barang", "harga", "tanggal"]
        available_cols = [col for col in criteria_cols if col in result.columns]
        subset = result[available_cols]
        subset.to_excel("output/Kode barang list.xlsx", index=False)
        print(f"Kolom wajib '{required}' tidak ditemukan. Buat file manual.")
        break
else:
    result = result.sort_values(by=config.get("output_sort", []))
    result.to_excel("output/hasil_merge.xlsx", index=False)
    print("Berhasil digabung dan disimpan di output/hasil_merge.xlsx")
