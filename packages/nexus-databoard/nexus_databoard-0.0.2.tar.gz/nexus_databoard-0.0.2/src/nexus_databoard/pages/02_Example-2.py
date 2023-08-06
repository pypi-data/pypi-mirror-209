import streamlit as st
import numpy as np
from common import page_config
page_config.set_page_config()

st.write("# Example 2 uses plotly charts")

@st.cache_data
def get_chart_86765810():
    import plotly.graph_objects as go

    import datetime
    import pandas as pd
    import plotly.express as px
    
    # initializing date
    test_date = datetime.datetime.strptime("01-7-2016", "%m-%d-%Y")
    
    # initializing K
    K = 20
    
    date_generated = pd.date_range(test_date, periods=K)
    #dateList = date_generated.strftime("%m-%d-%Y")
    random_data = pd.DataFrame(
        np.random.randn(50, len(date_generated)),
        columns=('col %d' % i for i in range(len(date_generated))))

    #fig = go.Figure()
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

    fig = px.line(df, x='Date', y='AAPL.High', range_x=['2016-07-01','2016-12-31'])

    fig.add_trace(go.Bar(
        x=df.axes[0],
        y=df.axes[1],
        xperiod="D1",
        xperiodalignment="middle",
        xhoverformat="Q%q",
        hovertemplate="%{y}%{_xother}"
    ))

    fig.add_trace(go.Scatter(
        x=date_generated,
        y=random_data.columns,
        xperiod="D1",
        xperiodalignment="middle",
        hovertemplate="%{y}%{_xother}"
    ))

    fig.update_layout(hovermode="x unified")

    st.plotly_chart(fig)

get_chart_86765810()