import streamlit as st
from streamlit_option_menu import option_menu

# Judul Aplikasi
st.title("Aplikasi Web - Kalkulator & Penghitung Luas Segitiga")

# Menu Navigasi
menu = st.sidebar.selectbox("Pilih Aplikasi", ["Kalkulator", "Luas Segitiga"])

# Fitur Kalkulator
if menu == "Kalkulator":
    st.header("Kalkulator Sederhana")
    
    # Input Angka
    num1 = st.number_input("Masukkan Angka Pertama", step=0)
    num2 = st.number_input("Masukkan Angka Kedua", step=0)

    # Pilih Operasi
    operasi = st.selectbox("Pilih Operasi", ["Tambah", "Kurang", "Kali", "Bagi"])

    # Hitung Hasil
    if st.button("Hitung"):
        if operasi == "Tambah":
            hasil = num1 + num2
        elif operasi == "Kurang":
            hasil = num1 - num2
        elif operasi == "Kali":
            hasil = num1 * num2
        elif operasi == "Bagi":
            if num2 != 0:
                hasil = num1 / num2
            else:
                hasil = "Tidak dapat membagi dengan nol"
        st.success(f"Hasil: {hasil}")

# Fitur Penghitungan Luas Segitiga
elif menu == "Luas Segitiga":
    st.header("Penghitungan Luas Segitiga")
    
    # Input Alas dan Tinggi
    alas = st.number_input("Masukkan Alas (cm)", step=0)
    tinggi = st.number_input("Masukkan Tinggi (cm)", step=0)

    # Hitung Luas
    if st.button("Hitung Luas"):
        luas = 0.5 * alas * tinggi
        st.success(f"Luas Segitiga: {luas} cm²")



st.markdown("*By Irsan*")