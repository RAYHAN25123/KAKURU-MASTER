import streamlit as st

st.title("Energi Potensial")
st.subheader("EP = Energi Potensial"
             "M = Massa Benda (Kg)"
             "G = Percepatan Gravitasi (m/s)"
             "H = Ketinggian")
st.subheader("Rumus = m x g x h")

m = st.number_input("Masukan Massanya")
h = st.number_input("Masukan Tingginya")
ep = m * 10 * h
st.header(ep)