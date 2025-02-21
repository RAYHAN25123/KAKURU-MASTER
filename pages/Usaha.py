import streamlit as st

st.title("Usaha")
st.subheader("W = Usaha(Joule)"
             "F = Gaya (Newton)"
             "S = Perpindahan Benda (Meter)")
st.subheader("Rumus = w = f x s")
f = st.number_input("Masukan Gaya(Newton)")
s = st.number_input("Perpindahan Benda(Meter)")
w = f * s
st.header(w)