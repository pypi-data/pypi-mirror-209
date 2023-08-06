import streamlit as st
import pandas as pd
import numpy as np
from common import page_config
page_config.set_page_config()

st.write("# Example 3 uses Altair Charts ")

@st.cache_data
def get_chart_74954(use_container_width: bool):
    import pandas as pd
    import altair as alt
    import numpy as np
    np.random.seed(42)

    # Generating Data
    source = pd.DataFrame({
        'Trial A': np.random.normal(0, 0.8, 1000),
        'Trial B': np.random.normal(-2, 1, 1000),
        'Trial C': np.random.normal(3, 2, 1000)
    })

    chart = alt.Chart(source).transform_fold(
        ['Trial A', 'Trial B', 'Trial C'],
        as_=['Experiment', 'Measurement']
    ).mark_bar(
        opacity=0.3,
        binSpacing=0
    ).encode(
        alt.X('Measurement:Q', bin=alt.Bin(maxbins=100)),
        alt.Y('count()', stack=None),
        alt.Color('Experiment:N')
    )

    st.altair_chart(chart, theme="streamlit", use_container_width=True)

get_chart_74954(True)