import streamlit as st

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

data_arima = pd.read_csv("../app/assets/Data/ARIMA_Model_prediction_outcome.csv")
data_arima['day'] = pd.to_datetime(data_arima['day'])
data_ets = pd.read_csv("../app/assets/data/ETS_prediction_outcome.csv")
data_ets['day'] = pd.to_datetime(data_ets['day'])
data_theta = pd.read_csv("../app/assets/data/THETA_Model_prediction_outcome.csv")
data_theta['day'] = pd.to_datetime(data_theta['day'])

data_bit = pd.read_csv("../data/raw_data/BTCUSDT_daily.csv")
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

st.write("# Compairing Models")
st.write("""The graph below shows the three models, ARIMA, ETS and THETA,
         being backtested on past bitcoin data over a 5 month period with
         a 1000€ starting trade.""")

sns.lineplot(x = data_arima['day'], y = data_arima['balance'], color="blue", label="ARIMA model")
sns.lineplot(x = data_ets['day'], y = data_ets['balance'], color = "green", label="ETS model")
sns.lineplot(x = data_theta['day'], y = data_theta['balance'], color="red", label="THETA model")
fig = plt.gcf()
st.pyplot(fig)

st.write("## Profit loss analysis")

st.write("""The graph below shows the profit that would have be made when the money would have
         been invested into bitcoin and held during in the same timeframe as the models were
         backtested in.""")

sns.lineplot(x = data_arima['day'], y = data_arima['balance'], color="blue", label="ARIMA model")
sns.lineplot(x = data_ets['day'], y = data_ets['balance'], color = "green", label="ETS model")
sns.lineplot(x = data_theta['day'], y = data_theta['balance'], color="red", label="THETA model")
sns.lineplot(x = data_bit['timestamp'], y = data_bit['CumulativeReturn'], color="yellow", label="hold model")
fig = plt.gcf()
st.pyplot(fig)

st.write("""Although holding the bitcoin would have resulted in a bigger profit, the graph makes it
         apperent that our models are not depend on bitcoin increasing in value since out model differs
         betwee long and short trades.""")

data_final_num = {'Model': ["ETS","ARIMA", "THETA", "Hold"],
        'Outcome': [final_ets, final_arima, final_theta, final_hold]}
df_final_num = pd.DataFrame(data_final_num)
st.table(df_final_num)

st.write(f"""Looking at the graph it becomes apperent that only two of your three models are
         profitable. The ETS model was the best model with a final balance of {final_arima}€,
         followed by ARIMA with a final balance of {final_arima}€, the unprofitable model was
         THETA with a final balance of {final_theta}€. During this timeperiod the most lucrative
         investment would have been to invest the money into bitcoin """)
