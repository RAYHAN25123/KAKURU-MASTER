import streamlit as st

st.title("Persegi")
st.subheader("Rumus = K = 4 x S")

s = st.number_input("Masukan Sisinya")
k = 4 * s
st.header("k")
