import streamlit as st

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import plotly.graph_objects as go
import plotly.subplots as sp

st.set_page_config(
    layout="wide"
)

### Load Data for graphs

data_arima = pd.read_csv("assets/data/ARIMA_Model_prediction_outcome.csv")
data_arima['day'] = pd.to_datetime(data_arima['day'])
data_ets = pd.read_csv("assets/data/ETS_prediction_outcome.csv")
data_ets['day'] = pd.to_datetime(data_ets['day'])
data_theta = pd.read_csv("assets/data/THETA_Model_prediction_outcome.csv")
data_theta['day'] = pd.to_datetime(data_theta['day'])

data_bit = pd.read_csv("assets/data/BTCUSDT_daily.csv")
data_bit = data_bit[(data_bit['timestamp'] > '2023-01-01') & (data_bit['timestamp'] < '2023-06-04')]
data_bit['timestamp'] = pd.to_datetime(data_bit['timestamp'])
data_bit['timestamp_day'] = data_bit['timestamp'].dt.floor('D')
data_bit['PercentageChange'] = data_bit['close'].pct_change()
data_bit = data_bit.drop(1211)
data_bit['CumulativeReturn'] = 1000 * (1 + data_bit['PercentageChange']).cumprod()

final_arima = round(data_arima["balance"].iloc[-1])
final_ets = round(data_ets["balance"].iloc[-1])
final_theta = round(data_theta["balance"].iloc[-1])
final_hold = round(data_bit["CumulativeReturn"].iloc[-1])


### Headings and logo

col1, _, col3 = st.columns([0.50, 0.3, 0.20])

with col1:
    st.markdown(" ")
    st.title("ALGORITHMIC BACKTESTING")
    st.subheader("Back testing for Profit and Loss analysis")

with col3:

    image_path = "https://raw.githubusercontent.com/MehmetSever09/assist_trader/master/assets/images/logo_assist_trader_cropped.png"
    border_color = "#FF7F32"
    border_width = 3
    image_width = 250  # in pixels
    image_height = 250  # in pixels

    styled_image = f'<div style="border: {border_width}px solid {border_color}; ' \
                f'width: {image_width}px; height: {image_height}px; ' \
                f'overflow: hidden;">' \
                f'<img src="{image_path}" style="object-fit: cover; ' \
                f'width: 100%; height: 100%;">' \
                f'</div>'

    # Display the styled image
    st.markdown(styled_image, unsafe_allow_html=True)

st.write("\n")

### Graphs

col1, col2 = st.columns(2)

with col1:
    st.write("## Our Models")

    st.write("""The graph below shows the three models, ARIMA, ETS and THETA,
            being backtested on past bitcoin data over a 5-month period with
            a 1000€ starting trade. """)
    st.write("  ")
    st.write("  ")


    #sns.lineplot(x = data_arima['day'], y = data_arima['balance'], color="blue", label="ARIMA model")
    #sns.lineplot(x = data_ets['day'], y = data_ets['balance'], color = "green", label="ETS model")
    #sns.lineplot(x = data_theta['day'], y = data_theta['balance'], color="red", label="THETA model")
    #fig = plt.gcf()
    #st.pyplot(fig)
with col1:
    fig = sp.make_subplots(rows=1, cols=1)

    fig.add_trace(go.Scatter(x= data_arima['day'], y=data_arima['balance'], mode="lines", name="ARIMA model", line=dict(color="blue")))
    fig.add_trace(go.Scatter(x= data_ets['day'], y=data_ets['balance'], mode="lines", name="ETS model", line=dict(color = "green")))
    fig.add_trace(go.Scatter(x= data_theta['day'], y=data_theta['balance'], mode="lines", name="THETA model", line=dict(color="red")))

    fig.update_layout(title="ARIMA, EST, THETA",
                      xaxis_title="Timestamp",
                      yaxis_title="Balance",
                      legend=dict(x=0, y=1))

    st.plotly_chart(fig, use_container_width=True)

#y=#, final_ets["prediction"], final_theta["prediction"])

with col2:
    st.write("## Profit loss analysis")

    st.write("""The graph below shows how the 1000€ initial investment would have turned if
            it would have been invested into bitcoin and held in the same timeframe as the
            models were backtested in.""")

    #sns.lineplot(x = data_arima['day'], y = data_arima['balance'], color="blue", label="ARIMA model")
    #sns.lineplot(x = data_ets['day'], y = data_ets['balance'], color = "green", label="ETS model")
    #sns.lineplot(x = data_theta['day'], y = data_theta['balance'], color="red", label="THETA model")
    #sns.lineplot(x = data_bit['timestamp'], y = data_bit['CumulativeReturn'], color="yellow", label="hold model")
    #fig = plt.gcf()
    #st.pyplot(fig)
with col2:
    fig = sp.make_subplots(rows=1, cols=1)

    fig.add_trace(go.Scatter(x= data_arima['day'], y=data_arima['balance'], mode="lines", name="ARIMA model", line=dict(color="blue")))
    fig.add_trace(go.Scatter(x= data_ets['day'], y=data_ets['balance'], mode="lines", name="ETS model", line=dict(color = "green")))
    fig.add_trace(go.Scatter(x= data_theta['day'], y=data_theta['balance'], mode="lines", name="THETA model", line=dict(color="red")))
    fig.add_trace(go.Scatter(x= data_bit['timestamp'], y=data_bit['CumulativeReturn'], mode="lines", name="hold model", line=dict(color="yellow")))

    fig.update_layout(title="Hold Model",
                      xaxis_title="Timestamp",
                      yaxis_title="Balance",
                      legend=dict(x=0, y=1))

    st.plotly_chart(fig, use_container_width=True)


st.write("""Although holding the bitcoin would have resulted in a bigger profit, the graph makes it
         apperent that our models are not depend on bitcoin increasing in value since it can differ
         between long and short trades.""")

data_final_num = {'Model': ["ETS","ARIMA", "THETA", "Hold"],
        'Outcome': [final_ets, final_arima, final_theta, final_hold]}
df_final_num = pd.DataFrame(data_final_num)
st.table(df_final_num)

st.write(f"""Looking at the graph it becomes apperent that only two of your three models are
         profitable. The ETS model was the best model with a final balance of {final_arima}€,
         followed by ARIMA with a final balance of {final_arima}€, the unprofitable model was
         THETA with a final balance of {final_theta}€. During this timeperiod the most lucrative
         investment would have been to invest the money into bitcoin. """)
