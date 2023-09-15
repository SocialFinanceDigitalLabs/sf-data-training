import streamlit as st
import pandas as pd
from io import StringIO
import plotly.express as px

def pp_plot(df):
    # aggregate data per provider and plot children's count
    pp_count_df = df.groupby(['PLACE_PROVIDER']).count()
    st.write(pp_count_df)
    fig = px.bar(
        pp_count_df,
        y="CHILD",
    )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)


uploaded_file = st.file_uploader("Upload an episodes csv file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.title('Original dataset')
    st.write(df)

    st.title('Children count per provider')
    pp_plot(df)
    
    
    st.title('Children count per provider with CIN filter')
    cin_option = st.selectbox(
    'Choose a CIN option',
    df.CIN.unique())

    df_filtered = df[df.CIN == cin_option]
    pp_plot(df_filtered)
   