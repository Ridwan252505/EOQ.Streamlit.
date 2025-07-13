import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

# Konfigurasi halaman
st.set_page_config(page_title="Perhitungan EOQ", layout="centered")

# Judul Aplikasi
st.title("📦 Aplikasi Perhitungan EOQ (Economic Order Quantity)")
st.markdown("""
Aplikasi ini membantu menghitung **jumlah pemesanan optimal (EOQ)** untuk meminimalkan total biaya persediaan.  
Gunakan data permintaan tahunan, biaya pemesanan, dan biaya penyimpanan untuk mendapatkan hasil yang efisien.
""")

# Studi Kasus (bisa dibuka/tutup)
with st.expander("📚 Studi Kasus: Toko Sembako Makmur Jaya"):
    st.markdown("""
**Deskripsi:**
Toko Makmur Jaya menjual 1.200 bungkus beras per tahun.  
- Biaya pemesanan per order: **Rp200.000**  
- Biaya penyimpanan per unit per tahun: **Rp5.000**

**Tujuan:**
Menentukan jumlah pesanan optimal agar total biaya persediaan minimal.

- Permintaan Tahunan = `1200`  
- Biaya Pemesanan = `200000`  
- Biaya Penyimpanan = `5000`
""")

# Input pengguna
st.subheader("📥 Input Data")
D = st.number_input("Permintaan Tahunan (D) - unit/tahun", min_value=1, step=1, value=1200)
S = st.number_input("Biaya Pemesanan per Order (S) - dalam Rupiah", min_value=1, step=1, value=200000)
H = st.number_input("Biaya Penyimpanan per Unit per Tahun (H) - dalam Rupiah", min_value=1, step=1, value=5000)

# Tombol perhitungan
if st.button("🔢 Hitung EOQ"):
    EOQ = math.sqrt((2 * D * S) / H)
    frekuensi_pesan = D / EOQ
    total_biaya = (EOQ / 2 * H) + (D / EOQ * S)

    st.subheader("📊 Hasil Perhitungan EOQ")
    st.success(f"**EOQ (Jumlah Pemesanan Optimal):** {EOQ:.2f} unit")
    st.info(f"**Frekuensi Pemesanan per Tahun:** {frekuensi_pesan:.2f} kali")
    st.warning(f"**Total Biaya Persediaan:** Rp {total_biaya:,.2f}")

    # Grafik biaya vs jumlah pesanan
    st.subheader("📈 Grafik: Total Biaya vs Jumlah Pesanan (Q)")
    Q = np.linspace(1, EOQ * 2, 100)
    TC = (Q / 2 * H) + (D / Q * S)

    fig, ax = plt.subplots()
    ax.plot(Q, TC, label='Total Cost (TC)', color='blue')
    ax.axvline(EOQ, color='red', linestyle='--', label=f'EOQ = {EOQ:.2f}')
    ax.set_xlabel('Jumlah Pesanan (Q)')
    ax.set_ylabel('Total Biaya (Rp)')
    ax.set_title('Grafik Total Biaya Persediaan vs Jumlah Pesanan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
