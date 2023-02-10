import streamlit as st
import streamlit_authenticator as stauth
import numpy as np
import pandas as pd
import pickle
import sklearn
import yaml

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8_sig')

with open('./config.yaml') as file:
    config = yaml.safe_load(file)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

st.subheader("仙台頭痛脳神経クリニックAI頭痛診断サポート")
st.write("______________________")
file = st.file_uploader("置き換えたいデータを入力して下さい。",type=["csv"])
if file:
    df_new = pd.read_csv(file,encoding="utf-8_sig")
    df_new = df_new.dropna(axis=0)
    st.dataframe(df_new)

    if st.button("このデータに置き換える場合はクリックしてください"):
        df_new.to_csv("df_log.csv",encoding="utf-8_sig",index=False)

    