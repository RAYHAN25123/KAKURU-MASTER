import streamlit as st

st.title("Energi Kinetik")
st.subheader("EK = Energi Kinetik (Joule)"
             "M = Massa Benda (Kg)"
             "V = Kecepatan (m/v)")
st.subheader("Rumus = 1/2 x m x v")

m = st.number_input("Masukan Massanya")
v = st.number_input("Masukan Kecepatannya")
ek = m * v /2
st.header(ek)