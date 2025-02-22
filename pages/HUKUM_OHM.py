import streamlit as st

st.title("Hukum Ohm(Listrik)")
st.header("Rumus")
st.subheader("V = I x R")
st.markdown("""
- V = Tegangan Listrik (Volt)
- I = Arus Listrik (Ampere)
- R = Hambatan listrik (Ohm, Simbol Ω)
""")
st.header("Mencari Volt :")
i = st.number_input("Masukan Arus Listriknya(Ampere)")
r = st.number_input("Masukan Hambatan Listriknya(Ω)")
v = i * r
st.header("Volt")
st.subheader(v)
st.header("Rumus Mencari Ampere")
st.subheader("I = V/R")
v1 = st.number_input("Masukan Tegangan Listriknya(Volt)")
r1 = st.number_input("Masukkan Hambatan Listrik (Ω)", key = r1)
try:
    i1 = v1 / r1
    st.write(f"Arus listrik (I) = {i1} A")
except ZeroDivisionError:
    st.error("⚠️ Error: Tidak bisa membagi dengan nol! Harap masukkan hambatan yang lebih besar dari 0.")
st.header("Ampere")
st.subheader(i1)
