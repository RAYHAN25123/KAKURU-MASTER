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
st.header("Hukum Newton ll (Rumus 1)")
m = st.number_input("Masukan Massanya(Kg)")
a = st.number_input("Masukan Percepatannya(m/s)")
f = m * a
st.header("Gaya (N)")
st.subheader(f)

st.header("Rumus Mencari Percepatan")
st.markdown("""
- A = F/M
""")
f1 = st.number_input("Masukan Gayanya(N)")
m1 = st.number_input("Masukkan Massanya", key ="m1")
if m1 != 0:
    a1 = f1 / m1
    st.header("Percepatan")
    st.subheader(f" {a1}")
st.header("Rumus Mencari Hambatan Listrik (Ω)")
st.markdown("""
R = V/I
""")
v2 = st.number_input("Masukan Tegangan Listriknya(Volt)", key ="v2")
i1 = st.number_input("Masukkan Arus Listriknya(Ω)", key ="i1")
if i1 != 0:
    r2 = v2 / i1
    st.header("Hambatan Listrik (Ω)")
    st.subheader(f" {r2}")
else:
    st.markdown("""
⚠️ Note: Hambatan tidak boleh 0! Masukkan nilai yang lebih besar dari 0.
""")
