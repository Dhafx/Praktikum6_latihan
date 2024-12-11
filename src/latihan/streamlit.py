import streamlit as st

st.title("Latihan Praktikum Modul 6")
st.write("Nama : Muhammad Dhafa Maulana")
st.write("NIM  : 202110370311100")

selected_content = st.sidebar.selectbox(
    "Pilih Modul",
    options=["Modul 1",
             "Modul 2",
             "Modul 3"]
)

if selected_content == "Modul 1":
    st.title("Modul 1")    
elif selected_content == "Modul 2":
    st.title("Modul 2")
elif selected_content == "Modul 3":
    st.title("Modul 3")