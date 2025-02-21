import streamlit as st

st.set_page_config(
    page_title="カクル/KAKURU MASTER",
    page_icon=":tada:",
    layout="wide"
    )

st.sidebar.success("👆SILAHKAN PILIH👆")

st.title("KAKURU (Kalkulator Rumus): Cara mudah menghitung cepat soal matematika")
st.markdown("""
    Orang yang terlibat :
- Raditya Rayhan Anjaya sebagai Programmer
- Khalil Ghibran Dzakwan Mulyadi sebagai Penyusun
### Apa Itu KAKURU?
**KAKURU** adalah sebuah mesin kalkulator yang berkerja layaknya kalkulator pada umumnya, hanya saja dirancang untuk mempermudah menyelesaikan masalah mengenai rumus matematika.
### Gimana cara kerjanya?
Gampang! Cuman pilih lewat sidebar di sini👈 terus tinggal satset satset deh.
""")

st.title("BANGUN RUANG BALOK")
p = st.number_input("Masukan Nilai Panjang:")
l = st.number_input("Masukan Nilai Lebar:")
t = st.number_input("Masukan Nilai Tinggi:")
st.header("KELILING")
k = 4 * ( p + l + t )
st.subheader(k)
st.header("LUAS BALOK")
l = ( p * l ) + ( p * t ) + ( l * t )
st.subheader(l)
st.header("VOLUME BALOK")
v = p * l * t
st.subheader(v)

