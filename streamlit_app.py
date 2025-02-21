import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.subheader("Testing")
x = st.number_input("Masukan nilai")
b = x + 1
st.title(b)
