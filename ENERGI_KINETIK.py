import streamlit as st

st.title("Energi Kinetik")
st.MARKDOWN("""
- EK = Energi Kinetik (Joule)
- M = Massa Benda (Kg)
- V = Kecepatan (m/v)
""")
st.subheader("Rumus")
st.markdown("""
- EK = 1/2 x m x v
""")

m = st.number_input("Masukan Massanya")
v = st.number_input("Masukan Kecepatannya")
ek = m * v /2
st.header(ek)
