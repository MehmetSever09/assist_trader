import streamlit as st

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

#data_bit = pd.read_csv("../raw_data/BTCUSDT_1h.csv")
#data_full = pd.read_csv("../notebook/clean_raw_data.csv")

#st.sidebar.image('../app/Stuff_for_app/logo_assist-traider.png', use_column_width=True)
#image = Image.open('../app/Stuff_for_app/logo_assist-traider.png')
st.markdown("""# Assist Traider
## Aim...
This is text""")

st.markdown("## Bitcoin base dataset:")



line_count_head = st.slider('Select a line count, head', 1, 100, 1)

head_df = data_bit.head(line_count_head)

head_df

column_names = data_full.columns.tolist()
st.markdown("## Parameters")
st.markdown(f"Parameters used: {column_names}")
st.markdown(f"total number of parameters used: {len(column_names)}")


st.markdown("## visual repesentaition of our data")

#sns.scatterplot(data=data_bit, x='close', y='open')
#fig = plt.gcf()
#st.pyplot(fig)

sns.lineplot(data_full["open"])
#sns.lineplot(data_full["close"])
sns.lineplot(data_full["close"])
fig = plt.gcf()
st.pyplot(fig)
