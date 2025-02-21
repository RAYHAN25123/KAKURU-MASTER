import streamlit as st

st.title("Daya")
st.markdown("""
- P = Daya (Watt)"
- W = Usaha (Joule)
- T = Waktu (Sekon/Detik)
""")
st.subheader("P = W/T")
st.subheader("Note : Cari (W) terlebih dahulu")
f = st.number_input("Masukan Gayanya(Newton)")
s = st.number_input("Masukan Perpindahan Bendanya(Meter)")
w = f * s
st.header(w)

t = st.number_input("Masukan Waktunya(sekon/Detik)")
p = w /t
st.header("Daya (Watt)")
st.subheader(p)
