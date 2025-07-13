import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Perhitungan EOQ", layout="centered")

st.title("📦 Aplikasi Perhitungan EOQ (Economic Order Quantity)")
st.write("Hitung jumlah pemesanan optimal berdasarkan permintaan, biaya pemesanan, dan biaya penyimpanan.")

# Input
st.subheader("📥 Input Data")
D = st.number_input("Permintaan Tahunan (D) - unit/tahun", min_value=1, step=1, value=1200)
S = st.number_input("Biaya Pemesanan per Order (S)", min_value=1, step=1, value=200000)
H = st.number_input("Biaya Penyimpanan per Unit per Tahun (H)", min_value=1, step=1, value=5000)

# Tombol hitung
if st.button("🔢 Hitung EOQ"):
    EOQ = math.sqrt((2 * D * S) / H)
    frekuensi_pesan = D / EOQ
    total_biaya = (EOQ / 2 * H) + (D / EOQ * S)

    st.subheader("📊 Hasil Perhitungan EOQ")
    st.write(f"**EOQ (Jumlah Pemesanan Optimal):** {EOQ:.2f} unit")
    st.write(f"**Jumlah Pemesanan per Tahun:** {frekuensi_pesan:.2f} kali")
    st.write(f"**Total Biaya Persediaan:** Rp {total_biaya:,.2f}")

    st.subheader("📈 Visualisasi Biaya vs Jumlah Pesanan (Q)")
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
