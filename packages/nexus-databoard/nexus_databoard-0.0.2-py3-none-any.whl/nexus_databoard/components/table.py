import streamlit as st

def display(df):
    numRows = df.shape[0]
    height = min(800, (numRows + 1) * 35 + 3)
    st.dataframe(data=df, height=height)