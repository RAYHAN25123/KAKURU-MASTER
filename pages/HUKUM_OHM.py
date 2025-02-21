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

st.header("Rumus")
st.subheader("I = V/R")
st.header("Mencari Ampere :")
v = st.number_input("Masukan Tegangan Listriknya(Volt)")
r = st.number_input("Masukan Hambatan Listriknya(Ω)")
try:
    i = v / r
except ZeroDivisionError:
    i = 0  # Bisa diganti dengan nilai default atau error handling yang sesuai
st.header("Ampere")
st.subheader(i)

st.header("Rumus")
st.subheader("R = V/I")
st.header("Mencari Hambatan Listrik (Ω) :")
v = st.number_input("Masukan Tegangan Listriknya(Volt)")
i = st.number_input("Masukan Arus Listriknya(Ampere)")
try:
    r = v / i
except ZeroDivisionError:
    r = 0  # Bisa diganti dengan nilai default atau error handling yang sesuai
st.header("Hambatan Listrik (Ω)")
st.subheader(r)
