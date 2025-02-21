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
i1 = st.number_input("Masukan Arus Listriknya(Ampere)")
with st.form(key="my_form"):
    r = st.number_input("Masukan Hambatan Listriknya(Ω)")
    submit_button = st.form_submit_button("Hitung")

v = i1 * r1
st.header("Volt")
st.subheader(v)

st.header("Rumus")
st.subheader("I = V/R")
st.header("Mencari Ampere :")
v1 = st.number_input("Masukan Tegangan Listriknya(Volt)")
r2 = st.number_input("Masukan Hambatan Listriknya(Ω)")
try:
    i = v1 / r2
except ZeroDivisionError:
    i = 0  # Bisa diganti dengan nilai default atau error handling yang sesuai
st.header("Ampere")
st.subheader(i)

st.header("Rumus")
st.subheader("R = V/I")
st.header("Mencari Hambatan Listrik (Ω) :")
v2 = st.number_input("Masukan Tegangan Listriknya(Volt)")
i2 = st.number_input("Masukan Arus Listriknya(Ampere)")
try:
    r = v2 / i1
except ZeroDivisionError:
    r = 0  # Bisa diganti dengan nilai default atau error handling yang sesuai
st.header("Hambatan Listrik (Ω)")
st.subheader(r)
