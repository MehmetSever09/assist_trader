import streamlit as st

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://raw.githubusercontent.com/MehmetSever09/assist_trader/master/app/assets/images/logo_assist_traider.png);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "Assist Trader";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def get_css():
    return '''
            <style>
            div.css-6qob1r.e1fqkh3o3{
                background-color: #e78910;
                color:#1a2033;
            }
            div.css-bgg0o6.etr89bj0{
                color: #e78910;
                font-size: 24px;
            }
            button.css-10e6rh1.edgvbvh5{
                background-color: #e78910;
                color: #1a2033;
            }
            h1{
                color:#933beb;
                text-align: center;
                font-size: 36px;
            }
            </style>

               '''
