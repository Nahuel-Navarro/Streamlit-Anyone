import streamlit as st
from sklearn.datasets import load_wine


data = load_wine(as_frame = True)
df = data.frame

st.title("Aguante streamlit")
st.header("Streamlit Test")

st.dataframe()