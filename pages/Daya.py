import streamlit as st

st.title("Daya")
st.subheader("P = Daya (Watt)"
             "W = Usaha (Joule)"
             "T = Waktu (Sekon/Detik)")
st.subheader("P = W/T")
f = st.number_input("Masukan Gayanya(Newton)")
s = st.number_input("Masukan Perpindahan Bendanya(Meter)")
W = f * s
st.header(w)

t = st.number_input("Masukan Waktunya(sekon/Detik)")
p = w / t
st.header(p)