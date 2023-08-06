import streamlit as st
import pandas as pd
import numpy as np
from common import page_config
page_config.set_page_config()

st.write("""
# Example 4 uses data from Google Sheets  
url: https://docs.google.com/spreadsheets/d/1V4fwE7kxV0h_YqXCbHbOcUrtKBV4oYNL4D-mZuwp09I/edit?usp=sharing
""")

from data import google_sheets
chart_data = google_sheets.get_data(sheet_name="campaign")

fields = ["Date", "Campaign", "Visitors", "Engagements", "Conversions"]

st.vega_lite_chart(chart_data, {
    'mark': {'type': 'line', 'tooltip': True},
    'encoding': {
        'x': {'field': 'Date', 'type': 'temporal'},
        'y': {'field': 'Conversions', 'type': 'quantitative'},
        'color': {'field': 'Campaign', 'type': 'nominal'},
    },
}, use_container_width=True)
