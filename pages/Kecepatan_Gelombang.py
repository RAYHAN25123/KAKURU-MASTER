import streamlit as st

st.title("Kecepatan Gelombang")
st.markdown("""
- v = kecepatan gelombang (m/s)
- f = frekuensi gelombang (Hz atau 1/s)
- λ = panjang gelombang (m)
""")
st.subheader("Rumus")
st.markdown("""
- V = f x λ
""")
f = st.number_input("Masukan Frekuensinya(Hertz)")
1 = st.number_input("Masukan Panjang Gelombangnya(Meter)")
v = f * 1
st.header("Kecepatan Gelombang(m/s)")
st.subheader(v)
