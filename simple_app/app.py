import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Upload an episodes csv new file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.title('Episodes dataset:')
    st.write(df)