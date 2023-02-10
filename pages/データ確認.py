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
if authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
else:
    st.subheader("仙台頭痛脳神経クリニックAI頭痛診断サポート")
    st.write("______________________")
    df_log = pd.read_csv("df_log.csv",encoding="utf-8_sig")
    st.dataframe(df_log)
    csv = convert_df(df_log)
    st.download_button(
        label="CSVデータダウンロード",
        data=csv,
        file_name='診断データ.csv',
        mime='text/csv',
    )
    