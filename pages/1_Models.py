import streamlit as st

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go


st.set_page_config(
    layout="wide"
)

## TITLES

col1, _, col3 = st.columns([0.50, 0.3, 0.20])

with col1:
    st.markdown(" ")
    st.title("Comparing Timeseries Models")
    # st.subheader("Building models to predict the next period of Cryptocurrency market for Traders")
    st.subheader("Which model performs better?")

with col3:

    # /home/lscr/code/lewagon/2023-q2-wagon/2023-q2-projects/assist_trader/assets/images/logo_assist_trader_cropped.png

    # st.image("app/assets/images/logo_assist_trader_cropped.png", use_column_width=True)
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

st.markdown(" ")


### Load Data for Graphs

x_date_ticks = [
    "2023-01-02",
    "2023-01-09",
    "2023-01-16",
    "2023-01-23",
    "2023-01-30",
    "2023-02-06",
    "2023-02-13",
    "2023-02-20",
    "2023-02-27",
    "2023-03-06",
    "2023-03-13",
    "2023-03-20",
    "2023-03-27",
    "2023-04-03",
    "2023-04-10",
    "2023-04-17",
    "2023-04-24",
    "2023-05-01",
    "2023-05-08",
    "2023-05-15",
    "2023-05-22",
    "2023-05-29",
    "2023-06-05",
    "2023-06-12",
]

pred_df = pd.read_csv("assets/data/streaml_models.csv")
pred_df = pred_df.drop(columns=['Unnamed: 0'])
pred_df["timestamp"] = pd.to_datetime(pred_df["timestamp"])

true_graph = go.Scatter(
    x=pred_df["timestamp"],
    y=pred_df["close"],
    mode="lines",
    marker= {"color":"#FF7F32"},
    # label="Actual Price"
)

arima_graph = go.Scatter(
    x=pred_df["timestamp"],
    y=pred_df["pred_arima"],
    mode="lines",
    marker= {"color":"green"},
)

theta_graph = go.Scatter(
    x=pred_df["timestamp"],
    y=pred_df["pred_theta"],
    mode="lines",
    marker= {"color":"yellow"},
)

ets_graph = go.Scatter(
    x=pred_df["timestamp"],
    y=pred_df["pred_etc"],
    mode="lines",
    marker= {"color":"blue"},
)

#### Generate bunch of different figures

col1, col2 = st.columns([0.8, 0.2])

with col2:
    st.write('<style>div[data-baseweb="radio"] label{font-size: 50px !important;}</style>', unsafe_allow_html=True)
    graph_type = st.radio(
        "What Timeseries Model would you like to compare to the outcome.",
        ("Baseline","ETS Model", "Theta Model", "ARIMA Model", "Compare them all!")
    )

with col1:

    # Create Fig
    # fig = go.Figure(
    #     data=[
    #         true_graph
    #     ])

    # if check_arima:
    #     pass

    if graph_type == "Baseline":
        fig = go.Figure(data=[true_graph])
    elif graph_type == "ETS Model":
        fig = go.Figure(data=[true_graph, arima_graph])
    elif graph_type == "ARIMA Model":
        fig = go.Figure(data=[true_graph, theta_graph])
    elif graph_type == "Theta Model":
        fig = go.Figure(data=[true_graph, ets_graph])
    elif graph_type == "Compare them all!":
        fig = go.Figure(data=[true_graph, arima_graph, theta_graph, ets_graph])

    # Update fig params
    fig.update_layout(
        title="Bitcoin - USDT",
        width=1000,
        height=500,
        xaxis = {
            # "title": "Time",
            "tickmode": "array",
            "tickvals": x_date_ticks,
            "tickangle": -45,
            "range": ["2023-01-01", "2023-06-01"],
            "rangeslider_visible": False
        },
        yaxis = {
            "title": "Close Price (USDT)",
        },
        showlegend=False,
        sliders=[],
    )

    # Plot
    st.plotly_chart(fig, use_container_width=True)


### About the Models

st.markdown("""## About the Models:""")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
                ### ETS :white_check_mark::star-struck:

                #### (MAPE: 0.73%)

                Predictions based on past observations.
                """)

with col2:
    st.markdown("""
                ### Theta :x: :no_good:

                #### (MAPE: 0.95%)

                Forecasts predictions based on timeseries decomposition.
                """)

with col3:
    st.markdown("""
                ### ARIMA :white_check_mark::sunglasses:

                #### (MAPE: 0.64%)

                Measures seasonal events over a given time period.
                """)


### Irina's graphs

# col1, col2, col3 = st.columns(3)

# with col1:
#    st.header("ETS :white_check_mark::star-struck:")
#    st.write('Forecasts predictions based on past observations')
#    sns.lineplot(x=data_bit['timestamp'],y=data_bit['close'])
#    sns.lineplot(x=data_bit['timestamp'],y=data_bit['pred_etc'])
#    fig=plt.gcf()
#    st.pyplot(fig)
#    st.write('Mape score:0.73%')

# with col2:
#    st.header("Theta :x: :no_good:")
#    st.write('Forecasts predictions based on decomposition')
#    sns.lineplot(x=data_bit['timestamp'],y=data_bit['close'])
#    sns.lineplot(x=data_bit['timestamp'],y=data_bit['pred_theta'])
#    fig=plt.gcf()
#    st.pyplot(fig)
#    st.write('Mape score:0.95%')

# with col3:
#    st.header("ARIMA :white_check_mark::sunglasses:")
#    st.write('Measures seasonal events over a period of time')
#    sns.lineplot(x=data_bit['timestamp'],y=data_bit['close'])
#    sns.lineplot(x=data_bit['timestamp'],y=data_bit['pred_arima'])
#    fig=plt.gcf()
#    st.pyplot(fig)
#    st.write('Mape score:0.64%')
