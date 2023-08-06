import streamlit as st

@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

def show_download_csv_button(df, name: str):
    csv = convert_df(df)

    st.download_button(
        "Download " + name + " CSV",
        csv,
        name.lower() + ".csv",
        "text/csv",
        key=name.lower() + '-csv'
    )