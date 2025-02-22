import streamlit as st

st.title("Hukum Newton")
st.header("Macam-Macam Hukum Newton :")
st.markdown("""
- Hukum Newton l
- Hukum Newton ll
- Hukum Newton lll
""")

st.header("Hukum Newton l")
st.subheader("Rumus")
st.markdown("""
- ∑F=0
""")
st.header("Hukum Newton ll")
st.markdown("""
- F = Gaya (Newton)
- M = Massa Benda (Kg)
- A = Percepatan (m/s)
""")
st.subheader("Rumus")
st.markdown("""
- Rumus 1 : F = M x A
- Rumus 2 : A = F/M
- Rumus 3 : M = F/A
""")
st.header("Hukum Newton ll(Rumus 1)")
m = st.number_input("Masukan Massanya(Kg)")
a = st.number_input("Masukan Percepatannya(m/s)")
f = m * a
st.header("Gaya (N)")
st.subheader(f)
