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
r = st.number_input("Masukan Hambatan Listriknya(Ω")
v = i1 * r1
st.header("Volt")
st.subheader(v)

