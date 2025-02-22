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
v1 = st.number_input("Masukan Tegangan Listriknya(Volt)", key = v1")
r1 = st.number_input("Masukan Hambatan Listriknya(Ω)"," key = r1)
i1 = v1 / r1
st.header("Ampere")
st.subheader(i1)
