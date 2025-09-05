# =========================
# suhu.py
# Modul konversi suhu
# =========================

def konversi_suhu(nilai ,dari, ke):
    nilai = float(nilai)
    dari = dari.lower()
    ke = ke.lower()

# jika user tidak memasukkan antara C, F, atau K maka akan terjadi error
    if dari not in ["c","f","k"]:
        return "Error: Format asal tidak sesuai, gunakan antara C, F, atau K"

    if ke not in ["c","f","k"]:
        return "Error: Format tujuan tidak sesuai, gunakan antara C, F, atau K"

# Rumus Fisika Dasar Konverensi Suhu:

    if dari == 'c':
      if ke == 'f':
        return nilai * 9/5 +  32
      elif ke == 'k':
        return nilai + 273.15
      elif ke == 'c':
        return nilai

    if dari == 'f':
      if ke == 'c':
        return (nilai - 32) * 5/9
      elif ke == 'k':
        return (nilai - 32) * 5/9 + 273.15
      elif ke == 'f':
        return nilai

    if dari == 'k':
      if ke == 'c':
        return nilai - 273.15
      elif ke == 'f':
        return (nilai - 273.15) * 9/5 + 32
      elif ke == 'k':
        return nilai
