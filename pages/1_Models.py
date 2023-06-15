import streamlit as st

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image


st.set_page_config(
    layout="wide"
)

data_bit = pd.read_csv("app/assets/data/streaml_models.csv")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("ETS :white_check_mark::star-struck:")
   st.write('Forecasts predictions based on past observations')
   sns.lineplot(x=data_bit['timestamp'],y=data_bit['close'])
   sns.lineplot(x=data_bit['timestamp'],y=data_bit['pred_etc'])
   fig=plt.gcf()
   st.pyplot(fig)
   st.write('Mape score:0.73%')

with col2:
   st.header("Theta :white_check_mark: :no_good:")
   st.write('Forecasts predictions based on decomposition')
   sns.lineplot(x=data_bit['timestamp'],y=data_bit['close'])
   sns.lineplot(x=data_bit['timestamp'],y=data_bit['pred_theta'])
   fig=plt.gcf()
   st.pyplot(fig)
   st.write('Mape score:0.95%')

with col3:
   st.header("ARIMA :white_check_mark::sunglasses:")
   st.write('Measures seasonal events over a period of time')
   sns.lineplot(x=data_bit['timestamp'],y=data_bit['close'])
   sns.lineplot(x=data_bit['timestamp'],y=data_bit['pred_arima'])
   fig=plt.gcf()
   st.pyplot(fig)
   st.write('Mape score:0.64%')




#sns.scatterplot(data=data_bit, x='timestamp', y='close')
#df.plot()
#val.plot()

#sns.lineplot(data_full["close"])
#sns.lineplot(data_full["predictions"])
#ns.lineplot(data_full["close"])
#fig = plt.gcf()
#st.pyplot(fig)
