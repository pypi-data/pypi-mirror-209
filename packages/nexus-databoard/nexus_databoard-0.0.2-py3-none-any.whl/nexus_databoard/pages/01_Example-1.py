import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import date
from vega_datasets import data as vega_data
from common import page_config
page_config.set_page_config()

st.title("Example")

today = date.today()
yesterday = today - datetime.timedelta(days=1)
earliest_date = date(2020, 1, 1)
max_date = date(2023, 6, 1)
start_date_help = "The earliest date available is " + str(earliest_date)
end_date_help = "The latest date available is " + str(max_date)

col1, col2, col3 = st.columns(3)

with col1:
   start_date = st.date_input("Start Date", value=yesterday, min_value=earliest_date, max_value=max_date, help=start_date_help)

with col2:
   end_date = st.date_input("End Date", value=today, min_value=earliest_date, max_value=max_date, help=end_date_help)

df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

source = vega_data.cars()

chart = {
    "mark": "point",
    "encoding": {
        "x": {
            "field": "Horsepower",
            "type": "quantitative",
        },
        "y": {
            "field": "Miles_per_Gallon",
            "type": "quantitative",
        },
        "color": {"field": "Origin", "type": "nominal"},
        "shape": {"field": "Origin", "type": "nominal"},
    },
}



tab1, tab2 = st.tabs(["Chart", "Table"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.vega_lite_chart(
        source, chart, theme="streamlit", use_container_width=True
    )
with tab2:
    st.dataframe(df)

