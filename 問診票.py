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


def register(df):
    df_log = pd.read_csv("df_log.csv",encoding="utf-8_sig")
    all_data = pd.concat([df_log,df])
    all_data.to_csv("df_log.csv",index=False,encoding="utf-8_sig")

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
    hospital = st.text_input("●病院名")
    consultation_date = str(st.date_input("●受診日"))

    st.write("______________________")
    st.subheader("基本情報")
    gender = st.radio("●性別",["男性", "女性"],horizontal=True)
    if gender == "男性":
        gender_value = 0
    else:
        gender_value = 1

    age = st.number_input("●初診時年齢[歳]",step=1)
    age_value = int(age)

    # st.write("______________________")
    height = st.number_input("●身長[cm]",step=0.1)
    weight = st.number_input("●体重[kg]",step=0.1)
    try:
        bmi = weight/(height/100)/(height/100)
        bmi = np.round(bmi,2)
        st.write("BMI:",bmi)
    except:
        bmi = 0

    height_value = float(height)
    weight_value = float(weight)
    bmi_value = float(bmi)

    hand = st.radio("●利き手",["右", "左"],horizontal=True)
    alchol = st.radio("●飲酒",["なし", "たまに","習慣的"],horizontal=True)
    smoke = st.radio("●喫煙",["なし", "過去にあり","現在あり","自分は吸わないが受動喫煙あり"],horizontal=True)

    if hand == "右":
        hand_value = 0
    elif hand == "左":
        hand_value = 1

    if alchol == "なし":
        alchol_value = 0
    elif alchol == "たまに":
        alchol_value = 1
    elif alchol == "習慣的":
        alchol_value = 2

    if smoke == "なし":
        smoke_value = 0
    elif smoke == "過去にあり":
        smoke_value = 1
    elif smoke == "現在あり":
        smoke_value = 2
    elif smoke == "自分は吸わないが受動喫煙あり":
        smoke_value = 3

    st.write("______________________")

    start_symptom_list = ["1週間以内", "1ヵ月以内","3ヵ月以内","1年以内","1年以上前から"]
    start_symptom = st.radio("●今の頭痛はいつ頃からありますか?",start_symptom_list,horizontal=True)
    start_symptom_lists = list()
    for start_symptom_value in start_symptom_list:
        if start_symptom == start_symptom_value:
            start_symptom_lists.append(1)
        else:
            start_symptom_lists.append(0)


    st.write("______________________")
    last_symptom = st.radio("●以前にも頭痛はありましたか？",["なし", "あり"],horizontal=True)
    if last_symptom == "なし":
        last_symptom_value = 0
    elif last_symptom == "あり":
        last_symptom_value = 1

    st.write("______________________")
    freq_symptom_list = ["年に数回", "月に数回", "15日/月以上", "ほぼ毎日","不定期"]
    freq_symptom = st.radio("●頭痛の起きる頻度は、おおむね、次のどれですか？",freq_symptom_list,horizontal=True)
    freq_symptom_lists = list()
    for freq_symptom_value in freq_symptom_list:
        if freq_symptom == freq_symptom_value:
            freq_symptom_lists.append(1)
        else:
            freq_symptom_lists.append(0)

    st.write("______________________")
    time_symptom_list = ["起床時", "午前中", "昼", "夕方","夜","寝る前","特になし"]
    time_symptom_title = '<p style="font-family:sans-serif; color:Black; font-size: 14px;">●痛みの強い時間帯はありますか？ (複数選択可)</p>'
    st.markdown(time_symptom_title, unsafe_allow_html=True)
    time_symptom0 = st.checkbox(time_symptom_list[0])
    time_symptom1 = st.checkbox(time_symptom_list[1])
    time_symptom2 = st.checkbox(time_symptom_list[2])
    time_symptom3 = st.checkbox(time_symptom_list[3])
    time_symptom4 = st.checkbox(time_symptom_list[4])
    time_symptom5 = st.checkbox(time_symptom_list[5])
    time_symptom6 = st.checkbox(time_symptom_list[6])

    time_list = [time_symptom0,time_symptom1,time_symptom2,time_symptom3,time_symptom4,time_symptom5,time_symptom6]
    time_lists = list()
    for action in time_list:
        if action == True:
            time_lists.append(1)
        else:
            time_lists.append(0)



    st.write("______________________")
    duration_symptom_list = ["常に", "2～3日", "1日", "4時間～半日","15分～3時間","2分～30分","5秒～3分","一瞬","寝ると良くなっている"]
    duration_symptom_title = '<p style="font-family:sans-serif; color:Black; font-size: 14px;">●１回の頭痛はどのくらい続きますか？ (複数選択可)</p>'
    st.markdown(duration_symptom_title, unsafe_allow_html=True)
    duration_symptom0 = st.checkbox(duration_symptom_list[0])
    duration_symptom1 = st.checkbox(duration_symptom_list[1])
    duration_symptom2 = st.checkbox(duration_symptom_list[2])
    duration_symptom3 = st.checkbox(duration_symptom_list[3])
    duration_symptom4 = st.checkbox(duration_symptom_list[4])
    duration_symptom5 = st.checkbox(duration_symptom_list[5])
    duration_symptom6 = st.checkbox(duration_symptom_list[6])
    duration_symptom7 = st.checkbox(duration_symptom_list[7])
    duration_symptom8 = st.checkbox(duration_symptom_list[8])

    duration_list = [duration_symptom0,duration_symptom1,duration_symptom2,duration_symptom3,duration_symptom4,duration_symptom5,duration_symptom6,duration_symptom7,duration_symptom8]
    duration_lists = list()
    for duration in duration_list:
        if duration == True:
            duration_lists.append(1)
        else:
            duration_lists.append(0)

    st.write("______________________")
    how_symptom_list = ["脈打つよう", "締め付けられるよう", "刺されるよう", "ガーン","ズキン","ドクンドクン","ギュー","チクチク","ピリピリ","突然の強い痛み","1分以内に最大の痛みになる","徐々に痛みがましてくる","だらだらと同じ程度の痛みが続く","重苦しい","押されるような","帽子をかぶったような"]
    how_symptom_title = '<p style="font-family:sans-serif; color:Black; font-size: 14px;">●どんな痛みですか？当てはまるもの全てにチェックをしてください。 (複数選択可)</p>'
    st.markdown(how_symptom_title, unsafe_allow_html=True)
    how_symptom0 = st.checkbox(how_symptom_list[0])
    how_symptom1 = st.checkbox(how_symptom_list[1])
    how_symptom2 = st.checkbox(how_symptom_list[2])
    how_symptom3 = st.checkbox(how_symptom_list[3])
    how_symptom4 = st.checkbox(how_symptom_list[4])
    how_symptom5 = st.checkbox(how_symptom_list[5])
    how_symptom6 = st.checkbox(how_symptom_list[6])
    how_symptom7 = st.checkbox(how_symptom_list[7])
    how_symptom8 = st.checkbox(how_symptom_list[8])
    how_symptom9 = st.checkbox(how_symptom_list[9])
    how_symptom10 = st.checkbox(how_symptom_list[10])
    how_symptom11 = st.checkbox(how_symptom_list[11])
    how_symptom12 = st.checkbox(how_symptom_list[12])
    how_symptom13 = st.checkbox(how_symptom_list[13])
    how_symptom14 = st.checkbox(how_symptom_list[14])
    how_symptom15 = st.checkbox(how_symptom_list[15])

    how_list = [how_symptom0,how_symptom1,how_symptom2,how_symptom3,how_symptom4,how_symptom5,how_symptom6,how_symptom7,how_symptom8,how_symptom9,how_symptom10,how_symptom11,how_symptom12,how_symptom13,how_symptom14,how_symptom15]
    how_lists = list()
    for how in how_list:
        if how == True:
            how_lists.append(1)
        else:
            how_lists.append(0)

    st.write("______________________")
    parts_symptom_list = ["右側", "左側", "両側", "前頭部","頭頂部","側頭部","後頭部","頸部","頭全体","眼球項部","肩","耳","鼻","頬","顎","上の歯","下の歯"]
    parts_symptom_title = '<p style="font-family:sans-serif; color:Black; font-size: 14px;">●痛む部位全てにチェックをしてください (複数選択可)</p>'
    st.markdown(parts_symptom_title, unsafe_allow_html=True)
    parts_symptom0 = st.checkbox(parts_symptom_list[0])
    parts_symptom1 = st.checkbox(parts_symptom_list[1])
    parts_symptom2 = st.checkbox(parts_symptom_list[2])
    parts_symptom3 = st.checkbox(parts_symptom_list[3])
    parts_symptom4 = st.checkbox(parts_symptom_list[4])
    parts_symptom5 = st.checkbox(parts_symptom_list[5])
    parts_symptom6 = st.checkbox(parts_symptom_list[6])
    parts_symptom7 = st.checkbox(parts_symptom_list[7])
    parts_symptom8 = st.checkbox(parts_symptom_list[8])
    parts_symptom9 = st.checkbox(parts_symptom_list[9])
    parts_symptom10 = st.checkbox(parts_symptom_list[10])
    parts_symptom11 = st.checkbox(parts_symptom_list[11])
    parts_symptom12 = st.checkbox(parts_symptom_list[12])
    parts_symptom13 = st.checkbox(parts_symptom_list[13])
    parts_symptom14 = st.checkbox(parts_symptom_list[14])
    parts_symptom15 = st.checkbox(parts_symptom_list[15])
    parts_symptom16 = st.checkbox(parts_symptom_list[16])

    parts_list = [parts_symptom0,parts_symptom1,parts_symptom2,parts_symptom3,parts_symptom4,parts_symptom5,parts_symptom6,parts_symptom7,parts_symptom8,parts_symptom9,parts_symptom10,parts_symptom11,parts_symptom12,parts_symptom13,parts_symptom14,parts_symptom15,parts_symptom16]
    parts_lists = list()
    for parts in parts_list:
        if parts == True:
            parts_lists.append(1)
        else:
            parts_lists.append(0)

    st.write("______________________")
    pain_score = st.slider("●痛くないときを0点、想像できる最悪の痛みを100点としたら、最もひどい頭痛の強さは何点になりますか？50点は顔をしかめる程度です。",0,100,50)


    st.write("______________________")
    change_symptom_list =["日に日に強くなっている", "日によって程度が違う","変化なし"]
    change_symptom = st.radio("●痛みについて教えてください",change_symptom_list,horizontal=True)
    change_symptom_lists = list()
    for change_symptom_value in change_symptom_list:
        if change_symptom == change_symptom_value:
            change_symptom_lists.append(1)
        else:
            change_symptom_lists.append(0)

    st.write("______________________")
    difficulty_symptom_list = ["全く支障なし","気になるが集中すると忘れる","我慢が必要で生活に支障がある","通常の仕事や生活が困難である","横にならないと我慢ができない","横になっても激しく痛む"]
    difficulty_symptom_title = '<p style="font-family:sans-serif; color:Black; font-size: 14px;">●頭痛のために生活に支障がありますか？すべて選んでください。 (複数選択可)</p>'
    st.markdown(difficulty_symptom_title, unsafe_allow_html=True)
    difficulty_symptom0 = st.checkbox(difficulty_symptom_list[0])
    difficulty_symptom1 = st.checkbox(difficulty_symptom_list[1])
    difficulty_symptom2 = st.checkbox(difficulty_symptom_list[2])
    difficulty_symptom3 = st.checkbox(difficulty_symptom_list[3])
    difficulty_symptom4 = st.checkbox(difficulty_symptom_list[4])
    difficulty_symptom5 = st.checkbox(difficulty_symptom_list[5])
    difficulty_list = [difficulty_symptom0,difficulty_symptom1,difficulty_symptom2,difficulty_symptom3,difficulty_symptom4,difficulty_symptom5]
    difficulty_lists = list()
    for difficulty in difficulty_list:
        if difficulty == True:
            difficulty_lists.append(1)
        else:
            difficulty_lists.append(0)

    st.write("______________________")
    reason_symptom_list = ["なし", "入浴", "頭を振る", "体動","飲酒","喫煙","寝不足","寝過ぎ","天候の悪化","まぶしい光","騒音","におい","冷やす","冷たい物を食べる","辛い物を食べる","人ごみ","休日","過労"]
    reason_symptom_title = '<p style="font-family:sans-serif; color:Black; font-size: 14px;">●以下の様なことや、どのようなときに頭痛を悪化させますか。すべて選んでください。(複数選択可)</p>'
    st.markdown(reason_symptom_title, unsafe_allow_html=True)
    reason_symptom0 = st.checkbox(reason_symptom_list[0])
    if reason_symptom0 == True:
        reason_value = False  
        reason_disabled = True
        reason_symptom1 = st.checkbox(reason_symptom_list[1],value=reason_value,disabled=reason_disabled)
        reason_symptom2 = st.checkbox(reason_symptom_list[2],value=reason_value,disabled=reason_disabled)
        reason_symptom3 = st.checkbox(reason_symptom_list[3],value=reason_value,disabled=reason_disabled)
        reason_symptom4 = st.checkbox(reason_symptom_list[4],value=reason_value,disabled=reason_disabled)
        reason_symptom5 = st.checkbox(reason_symptom_list[5],value=reason_value,disabled=reason_disabled)
        reason_symptom6 = st.checkbox(reason_symptom_list[6],value=reason_value,disabled=reason_disabled)
        reason_symptom7 = st.checkbox(reason_symptom_list[7],value=reason_value,disabled=reason_disabled)
        reason_symptom8 = st.checkbox(reason_symptom_list[8],value=reason_value,disabled=reason_disabled)
        reason_symptom9 = st.checkbox(reason_symptom_list[9],value=reason_value,disabled=reason_disabled)
        reason_symptom10 = st.checkbox(reason_symptom_list[10],value=reason_value,disabled=reason_disabled)
        reason_symptom11 = st.checkbox(reason_symptom_list[11],value=reason_value,disabled=reason_disabled)
        reason_symptom12 = st.checkbox(reason_symptom_list[12],value=reason_value,disabled=reason_disabled)
        reason_symptom13 = st.checkbox(reason_symptom_list[13],value=reason_value,disabled=reason_disabled)
        reason_symptom14 = st.checkbox(reason_symptom_list[14],value=reason_value,disabled=reason_disabled)
        reason_symptom15 = st.checkbox(reason_symptom_list[15],value=reason_value,disabled=reason_disabled)
        reason_symptom16 = st.checkbox(reason_symptom_list[16],value=reason_value,disabled=reason_disabled)
        reason_symptom17 = st.checkbox(reason_symptom_list[17],value=reason_value,disabled=reason_disabled)
        reason_symptom1 = False
        reason_symptom2 = False
        reason_symptom3 = False
        reason_symptom4 = False
        reason_symptom5 = False
        reason_symptom6 = False
        reason_symptom7 = False
        reason_symptom8 = False
        reason_symptom9 = False
        reason_symptom10 = False
        reason_symptom11 = False
        reason_symptom12 = False
        reason_symptom13 = False
        reason_symptom14 = False
        reason_symptom15 = False
        reason_symptom16 = False
        reason_symptom17 = False
    else:
        reason_symptom1 = st.checkbox(reason_symptom_list[1])
        reason_symptom2 = st.checkbox(reason_symptom_list[2])
        reason_symptom3 = st.checkbox(reason_symptom_list[3])
        reason_symptom4 = st.checkbox(reason_symptom_list[4])
        reason_symptom5 = st.checkbox(reason_symptom_list[5])
        reason_symptom6 = st.checkbox(reason_symptom_list[6])
        reason_symptom7 = st.checkbox(reason_symptom_list[7])
        reason_symptom8 = st.checkbox(reason_symptom_list[8])
        reason_symptom9 = st.checkbox(reason_symptom_list[9])
        reason_symptom10 = st.checkbox(reason_symptom_list[10])
        reason_symptom11 = st.checkbox(reason_symptom_list[11])
        reason_symptom12 = st.checkbox(reason_symptom_list[12])
        reason_symptom13 = st.checkbox(reason_symptom_list[13])
        reason_symptom14 = st.checkbox(reason_symptom_list[14])
        reason_symptom15 = st.checkbox(reason_symptom_list[15])
        reason_symptom16 = st.checkbox(reason_symptom_list[16])
        reason_symptom17 = st.checkbox(reason_symptom_list[17])

    reason_list = [reason_symptom0,reason_symptom1,reason_symptom2,reason_symptom3,reason_symptom4,reason_symptom5,reason_symptom6,reason_symptom7,reason_symptom8,reason_symptom9,reason_symptom10,reason_symptom11,reason_symptom12,reason_symptom13,reason_symptom14,reason_symptom15,reason_symptom16,reason_symptom17]

    reason_lists = list()
    for reason in reason_list:
        if reason == True:
            reason_lists.append(1)
        else:
            reason_lists.append(0)

    st.write("______________________")
    concurrence_symptom_list = ["悪心　はきけ", "嘔吐", "音に過敏になる　うるさい", "光に過敏になる　まぶしい","臭いに過敏になる","目の充血","涙が出る","鼻詰まり","鼻水が出る","まぶたがむくむ、腫れる","顔に汗をかく","顔が赤らむ","耳が詰まった感じ","まぶたが重くなる、下がる","めまい","手足のしびれ","手足の脱力","肩首こり","意識が遠のく"]
    concurrence_symptom_title = '<p style="font-family:sans-serif; color:Black; font-size: 14px;">●以下の様なことが頭痛と一緒に起こることがありますか。すべて選んでください。(複数選択可)</p>'
    st.markdown(concurrence_symptom_title, unsafe_allow_html=True)
    concurrence_symptom0 = st.checkbox(concurrence_symptom_list[0])
    concurrence_symptom1 = st.checkbox(concurrence_symptom_list[1])
    concurrence_symptom2 = st.checkbox(concurrence_symptom_list[2])
    concurrence_symptom3 = st.checkbox(concurrence_symptom_list[3])
    concurrence_symptom4 = st.checkbox(concurrence_symptom_list[4])
    concurrence_symptom5 = st.checkbox(concurrence_symptom_list[5])
    concurrence_symptom6 = st.checkbox(concurrence_symptom_list[6])
    concurrence_symptom7 = st.checkbox(concurrence_symptom_list[7])
    concurrence_symptom8 = st.checkbox(concurrence_symptom_list[8])
    concurrence_symptom9 = st.checkbox(concurrence_symptom_list[9])
    concurrence_symptom10 = st.checkbox(concurrence_symptom_list[10])
    concurrence_symptom11 = st.checkbox(concurrence_symptom_list[11])
    concurrence_symptom12 = st.checkbox(concurrence_symptom_list[12])
    concurrence_symptom13 = st.checkbox(concurrence_symptom_list[13])
    concurrence_symptom14 = st.checkbox(concurrence_symptom_list[14])
    concurrence_symptom15 = st.checkbox(concurrence_symptom_list[15])
    concurrence_symptom16 = st.checkbox(concurrence_symptom_list[16])
    concurrence_symptom17 = st.checkbox(concurrence_symptom_list[17])
    concurrence_symptom18 = st.checkbox(concurrence_symptom_list[18])

    concurrence_list = [concurrence_symptom0,concurrence_symptom1,concurrence_symptom2,concurrence_symptom3,concurrence_symptom4,concurrence_symptom5,concurrence_symptom6,concurrence_symptom7,concurrence_symptom8,concurrence_symptom9,concurrence_symptom10,concurrence_symptom11,concurrence_symptom12,concurrence_symptom13,concurrence_symptom14,concurrence_symptom15,concurrence_symptom16,concurrence_symptom17,concurrence_symptom18]
    concurrence_lists = list()
    for concurrence in concurrence_list:
        if concurrence == True:
            concurrence_lists.append(1)
        else:
            concurrence_lists.append(0)
    st.write("______________________")
    sign_symptom_list = ["なし", "目の前に光が見える　チカチカ　ギザギザしたものが見える　視野がぼやける", "半身のしびれ感", "半身の脱力","食欲亢進","トイレが近くなる","ねむけ","なまあくび","むくみ","はきけ","嘔吐","音に過敏になる　うるさい","光に過敏になる　まぶしい","臭いに過敏になる","意識が遠のく"]
    sign_symptom_title = '<p style="font-family:sans-serif; color:Black; font-size: 14px;">●以下の様なことが頭痛のおこる前触れとしてありますか。すべて選んでください。(複数選択可)</p>'
    st.markdown(sign_symptom_title, unsafe_allow_html=True)
    sign_symptom0 = st.checkbox(sign_symptom_list[0],key=10)
    if sign_symptom0 == True:
        sign_value = False  
        sign_disabled = True
        sign_symptom1 = st.checkbox(sign_symptom_list[1],value=sign_value,disabled=sign_disabled)
        sign_symptom2 = st.checkbox(sign_symptom_list[2],value=sign_value,disabled=sign_disabled)
        sign_symptom3 = st.checkbox(sign_symptom_list[3],value=sign_value,disabled=sign_disabled)
        sign_symptom4 = st.checkbox(sign_symptom_list[4],value=sign_value,disabled=sign_disabled)
        sign_symptom5 = st.checkbox(sign_symptom_list[5],value=sign_value,disabled=sign_disabled)
        sign_symptom6 = st.checkbox(sign_symptom_list[6],value=sign_value,disabled=sign_disabled)
        sign_symptom7 = st.checkbox(sign_symptom_list[7],value=sign_value,disabled=sign_disabled)
        sign_symptom8 = st.checkbox(sign_symptom_list[8],value=sign_value,disabled=sign_disabled)
        sign_symptom9 = st.checkbox(sign_symptom_list[9],value=sign_value,disabled=sign_disabled)
        sign_symptom10 = st.checkbox(sign_symptom_list[10],value=sign_value,disabled=sign_disabled,key=11)
        sign_symptom11 = st.checkbox(sign_symptom_list[11],value=sign_value,disabled=sign_disabled,key=32)
        sign_symptom12 = st.checkbox(sign_symptom_list[12],value=sign_value,disabled=sign_disabled,key=31)
        sign_symptom13 = st.checkbox(sign_symptom_list[13],value=sign_value,disabled=sign_disabled,key=51)
        sign_symptom14 = st.checkbox(sign_symptom_list[14],value=sign_value,disabled=sign_disabled,key=15)
        sign_symptom1 = False
        sign_symptom2 = False
        sign_symptom3 = False
        sign_symptom4 = False
        sign_symptom5 = False
        sign_symptom6 = False
        sign_symptom7 = False
        sign_symptom8 = False
        sign_symptom9 = False
        sign_symptom10 = False
        sign_symptom11 = False
        sign_symptom12 = False
        sign_symptom13 = False
        sign_symptom14 = False
    else:
        sign_symptom1 = st.checkbox(sign_symptom_list[1])
        sign_symptom2 = st.checkbox(sign_symptom_list[2])
        sign_symptom3 = st.checkbox(sign_symptom_list[3])
        sign_symptom4 = st.checkbox(sign_symptom_list[4])
        sign_symptom5 = st.checkbox(sign_symptom_list[5])
        sign_symptom6 = st.checkbox(sign_symptom_list[6])
        sign_symptom7 = st.checkbox(sign_symptom_list[7])
        sign_symptom8 = st.checkbox(sign_symptom_list[8])
        sign_symptom9 = st.checkbox(sign_symptom_list[9])
        sign_symptom10 = st.checkbox(sign_symptom_list[10],key=12)
        sign_symptom11 = st.checkbox(sign_symptom_list[11],key=33)
        sign_symptom12 = st.checkbox(sign_symptom_list[12],key=41)
        sign_symptom13 = st.checkbox(sign_symptom_list[13],key=52)
        sign_symptom14 = st.checkbox(sign_symptom_list[14],key=16)

    sign_list = [sign_symptom0,sign_symptom1,sign_symptom2,sign_symptom3,sign_symptom4,sign_symptom5,sign_symptom6,sign_symptom7,sign_symptom8,sign_symptom9,sign_symptom10,sign_symptom11,sign_symptom12,sign_symptom13,sign_symptom14]
    sign_lists = list()
    for sign in sign_list:
        if sign == True:
            sign_lists.append(1)
        else:
            sign_lists.append(0)
    st.write("______________________")
    action_symptom_list = ["なにもしない", "横になって休む", "冷やす", "温める","マッサージ","入浴","ストレッチ"]
    action_symptom_title = '<p style="font-family:sans-serif; color:Black; font-size: 14px;">頭痛のとき、どのように対応しますか？すべて選んでください。(複数選択可)</p>'
    st.markdown(action_symptom_title, unsafe_allow_html=True)
    action_symptom0 = st.checkbox(action_symptom_list[0])
    if action_symptom0 == True:
        action_value = False  
        action_disabled = True
        action_symptom1 = st.checkbox(action_symptom_list[1],value=action_value,disabled=action_disabled)
        action_symptom2 = st.checkbox(action_symptom_list[2],value=action_value,disabled=action_disabled,key=21)
        action_symptom3 = st.checkbox(action_symptom_list[3],value=action_value,disabled=action_disabled)
        action_symptom4 = st.checkbox(action_symptom_list[4],value=action_value,disabled=action_disabled)
        action_symptom5 = st.checkbox(action_symptom_list[5],value=action_value,disabled=action_disabled,key=23)
        action_symptom6 = st.checkbox(action_symptom_list[6],value=action_value,disabled=action_disabled)
        action_symptom1 = False
        action_symptom2 = False
        action_symptom3 = False
        action_symptom4 = False
        action_symptom5 = False
        action_symptom6 = False
    else:
        action_symptom1 = st.checkbox(action_symptom_list[1])
        action_symptom2 = st.checkbox(action_symptom_list[2],key=22)
        action_symptom3 = st.checkbox(action_symptom_list[3])
        action_symptom4 = st.checkbox(action_symptom_list[4])
        action_symptom5 = st.checkbox(action_symptom_list[5],key=23)
        action_symptom6 = st.checkbox(action_symptom_list[6])

    action_list = [action_symptom0,action_symptom1,action_symptom2,action_symptom3,action_symptom4,action_symptom5,action_symptom6]
    action_lists = list()
    for action in action_list:
        if action == True:
            action_lists.append(1)
        else:
            action_lists.append(0)


    st.write("______________________")
    medicine_check_list = ["飲まない","飲む"]
    medicine_kind_list = ["市販薬","病院鎮痛薬","病院特効薬(レイボー、トリプタン)"]
    medicine_check = st.radio("●頭痛のとき、薬を飲みますか?",medicine_check_list,horizontal=True)
    if medicine_check == "飲む":
        medicine_check_value = 1
        medicine0 = st.checkbox(medicine_kind_list[0])
        medicine1 = st.checkbox(medicine_kind_list[1])
        medicine2 = st.checkbox(medicine_kind_list[2])
        if medicine0 == True:
            medicine0_value = 1
        elif medicine0 == False:
            medicine0_value = 0
        if medicine1 == True:
            medicine1_value = 1
        elif medicine1 == False:
            medicine1_value = 0
        if medicine2 == True:
            medicine2_value = 1
        elif medicine2 == False:
            medicine2_value = 0
    else:
        medicine_check_value = 0
        medicine0_value = 0
        medicine1_value = 0
        medicine2_value = 0

    medicine_list = [medicine_check_value,medicine0_value,medicine1_value,medicine2_value]

    if medicine_check == "飲む":
        st.write("______________________")
        medicine_effect_list = ["効く","あまり効かない","効かない","効かなくなってきた","まちまち"]
        medicine_effect = st.radio("●その薬の効果はどうですか？",medicine_effect_list,horizontal=True)
        medicine_effect_result = list()
        for check_list in medicine_effect_list:
            if check_list == medicine_effect:
                medicine_effect_result.append(1)
            else:
                medicine_effect_result.append(0)
    else:
        medicine_effect_result = list()
        for i in range(5):
            medicine_effect_result.append(0)

    st.write("______________________")
    family_symptom_list = ["父", "母", "配偶者", "子供","兄弟","祖父母"]
    family_symptom_title = '<p style="font-family:sans-serif; color:Black; font-size: 14px;">●家族・兄弟・親戚に頭痛持ちの人はいますか。すべて選んでください。(複数選択可)</p>'
    st.markdown(family_symptom_title, unsafe_allow_html=True)
    family_symptom0 = st.checkbox(family_symptom_list[0])
    family_symptom1 = st.checkbox(family_symptom_list[1])
    family_symptom2 = st.checkbox(family_symptom_list[2])
    family_symptom3 = st.checkbox(family_symptom_list[3])
    family_symptom4 = st.checkbox(family_symptom_list[4])
    family_symptom5 = st.checkbox(family_symptom_list[5])

    family_list = [family_symptom0,family_symptom1,family_symptom2,family_symptom3,family_symptom4,family_symptom5]
    family_lists = list()
    for family in family_list:
        if family == True:
            family_lists.append(1)
        else:
            family_lists.append(0)

    st.write("______________________")
    past_symptom_list = ["子供のころよく腹痛があった", "子供のころ乗物酔いをしやすかった", "朝早くに目が覚める", "熟睡感がない","同じ姿勢でいることがおおい","デスクワークがおおい","運動不足","行動を起こすまで時間がかかる、おっくうだ","心配事が多い","喘息といわれた","慢性腎不全といわれた","心臓病といわれた"]
    past_symptom_title = '<p style="font-past:sans-serif; color:Black; font-size: 14px;">●以下の項目で当てはまるもの全てにチェックしてください。(複数選択可)</p>'
    st.markdown(past_symptom_title, unsafe_allow_html=True)
    past_symptom0 = st.checkbox(past_symptom_list[0])
    past_symptom1 = st.checkbox(past_symptom_list[1])
    past_symptom2 = st.checkbox(past_symptom_list[2])
    past_symptom3 = st.checkbox(past_symptom_list[3])
    past_symptom4 = st.checkbox(past_symptom_list[4])
    past_symptom5 = st.checkbox(past_symptom_list[5])
    past_symptom6 = st.checkbox(past_symptom_list[6])
    past_symptom7 = st.checkbox(past_symptom_list[7])
    past_symptom8 = st.checkbox(past_symptom_list[8])
    past_symptom9 = st.checkbox(past_symptom_list[9])
    past_symptom10 = st.checkbox(past_symptom_list[10])
    past_symptom11 = st.checkbox(past_symptom_list[11])

    past_list = [past_symptom0,past_symptom1,past_symptom2,past_symptom3,past_symptom4,past_symptom5,past_symptom6,past_symptom7,past_symptom8,past_symptom9,past_symptom10,past_symptom11]
    past_lists = list()
    for past in past_list:
        if past == True:
            past_lists.append(1)
        else:
            past_lists.append(0)
    column = [
            "性別",
            "初診時年齢",
            "身長",
            "体重",
            "BMI",
            "利き手",
            "飲酒",
            "喫煙",
            "発症時期1週間",
            "発症時期1ヵ月",
            "発症時期3ヵ月",
            "発症時期1年以内",
            "発症時期1年以上",
            "頭痛の既往",
            "頻度　年",
            "頻度　月",
            "頻度　15日",
            "頻度　毎日",
            "頻度　不定期",

            "時間帯　起床時",
            "時間帯　午前中",
            "時間帯　昼",
            "時間帯　夕方",
            "時間帯　夜",
            "時間帯　寝る前",
            "時間帯　特になし",
            
            "持続　常に",
            "持続　2～3日",
            "持続　1日",
            "持続　4時間～",
            "持続　15分～",
            "持続　2分～",
            "持続　5秒～",
            "持続　一瞬",
            "持続　寝ると",

            "性状脈打つ",
            "性状締め付け",
            "性状刺される",
            "性状ガーン",
            "性状ズキン",
            "性状ドクン",
            "性状ギュー",
            "性状チクチク",
            "性状ピリピリ",
            "性状突然",
            "性状1分以内",
            "性状徐々に",
            "性状だらだら",
            "性状重苦しい",
            "性状押される",
            "性状帽子",

            "右側痛",
            "左側痛",
            "両方痛",
            "前頭部痛",
            "頭頂部痛",
            "側頭部痛",
            "後頭部痛",
            "頸部痛",
            "頭全体痛",
            "眼球項部痛",
            "肩痛",
            "耳痛",
            "鼻痛",
            "頬痛",
            "顎痛",
            "上歯痛",
            "下歯痛",

            "VAS",

            "変動日に日に増強",
            "変動日によ違う",
            "変動変化なし",

            "支障全く支障なし",
            "支障集中すると忘れる",
            "支障我慢が必要",
            "支障通常の仕事困難",
            "支障横になり我慢",
            "支障横になっても激痛",

            "悪化因子　なし",
            "悪化因子　入浴",
            "悪化因子　頭を振る",
            "悪化因子　体動",
            "悪化因子　飲酒",
            "悪化因子　喫煙",
            "悪化因子　寝不足",
            "悪化因子　寝過ぎ",
            "悪化因子　天候の悪化",
            "悪化因子　まぶしい光",
            "悪化因子　騒音",
            "悪化因子　におい",
            "悪化因子　冷やす",
            "悪化因子　冷たい物を食べる",
            "悪化因子　辛い物を食べる",
            "悪化因子　人ごみ",
            "悪化因子　休日",
            "悪化因子　過労",

            "随伴症状　悪心",
            "随伴症状　嘔吐",
            "随伴症状　音過敏",
            "随伴症状　光過敏",
            "随伴症状　臭い過敏",
            "随伴症状　目の充血",
            "随伴症状　流涙",
            "随伴症状　鼻閉",
            "随伴症状　鼻漏",
            "随伴症状　眼瞼浮腫",
            "随伴症状　顔面発汗",
            "随伴症状　顔面紅潮",
            "随伴症状　耳閉感",
            "随伴症状　眼瞼下垂",
            "随伴症状　めまい",
            "随伴症状　手足のしびれ",
            "随伴症状　手足の脱力",
            "随伴症状　肩首こり",
            "随伴症状　意識が遠のく",

            "前駆症状　なし",
            "前駆症状　閃輝暗点",
            "前駆症状　半身のしびれ感",
            "前駆症状　半身の脱力",
            "前駆症状　食欲亢進",
            "前駆症状　頻尿",
            "前駆症状　眠気",
            "前駆症状　なまあくび",
            "前駆症状　浮腫",
            "前駆症状　悪心",
            "前駆症状　嘔吐",
            "前駆症状　音過敏",
            "前駆症状　光過敏",
            "前駆症状　臭い過敏",
            "前駆症状　意識が遠のく",

            "対処　何もしない",
            "対処　横になる",
            "対処　冷やす",
            "対処　温める",
            "対処　マッサージ",
            "対処　入浴",
            "対処　ストレッチ",

            "頭痛薬の服用",
            "服薬　市販薬",
            "服薬　病院鎮痛薬",
            "服薬　病院特効薬",

            "薬効果　効く",
            "薬効果　あまり",
            "薬効果　効かない",
            "薬効果　効かなく",
            "薬効果　まちまち",

            "家族歴　父",
            "家族歴　母",
            "家族歴　配偶者",
            "家族歴　子供",
            "家族歴　兄弟",
            "家族歴　祖父母",

            "該当　子供腹痛",
            "該当　子供乗物酔い",
            "該当　早朝覚醒",
            "該当　熟睡感なし",
            "該当　同じ姿勢",
            "該当　デスクワーク",
            "該当　運動不足",
            "該当　おっくう",
            "該当　心配事",
            "該当　喘息",
            "該当　慢性腎不全",
            "該当　心臓病",

            ] 
    data = [[
            gender_value, 
            age_value, 
            height_value,
            weight_value,
            bmi_value,
            hand_value,
            alchol_value,
            smoke_value,
            start_symptom_lists[0],
            start_symptom_lists[1],
            start_symptom_lists[2],
            start_symptom_lists[3],
            start_symptom_lists[4],
            last_symptom_value,
            freq_symptom_lists[0],
            freq_symptom_lists[1],
            freq_symptom_lists[2],
            freq_symptom_lists[3],
            freq_symptom_lists[4],

            time_lists[0],
            time_lists[1],
            time_lists[2],
            time_lists[3],
            time_lists[4],
            time_lists[5],
            time_lists[6],
            
            duration_lists[0],
            duration_lists[1],
            duration_lists[2],
            duration_lists[3],
            duration_lists[4],
            duration_lists[5],
            duration_lists[6],
            duration_lists[7],
            duration_lists[8],

            how_lists[0],
            how_lists[1],
            how_lists[2],
            how_lists[3],
            how_lists[4],
            how_lists[5],
            how_lists[6],
            how_lists[7],
            how_lists[8],
            how_lists[9],
            how_lists[10],
            how_lists[11],
            how_lists[12],
            how_lists[13],
            how_lists[14],
            how_lists[15],

            parts_lists[0],
            parts_lists[1],
            parts_lists[2],
            parts_lists[3],
            parts_lists[4],
            parts_lists[5],
            parts_lists[6],
            parts_lists[7],
            parts_lists[8],
            parts_lists[9],
            parts_lists[10],
            parts_lists[11],
            parts_lists[12],
            parts_lists[13],
            parts_lists[14],
            parts_lists[15],
            parts_lists[16],

            int(pain_score),

            change_symptom_lists[0],
            change_symptom_lists[1],
            change_symptom_lists[2],

            difficulty_lists[0],
            difficulty_lists[1],
            difficulty_lists[2],
            difficulty_lists[3],
            difficulty_lists[4],
            difficulty_lists[5],

            reason_lists[0],
            reason_lists[1],
            reason_lists[2],
            reason_lists[3],
            reason_lists[4],
            reason_lists[5],
            reason_lists[6],
            reason_lists[7],
            reason_lists[8],
            reason_lists[9],
            reason_lists[10],
            reason_lists[11],
            reason_lists[12],
            reason_lists[13],
            reason_lists[14],
            reason_lists[15],
            reason_lists[16],
            reason_lists[17],

            concurrence_lists[0],
            concurrence_lists[1],
            concurrence_lists[2],
            concurrence_lists[3],
            concurrence_lists[4],
            concurrence_lists[5],
            concurrence_lists[6],
            concurrence_lists[7],
            concurrence_lists[8],
            concurrence_lists[9],
            concurrence_lists[10],
            concurrence_lists[11],
            concurrence_lists[12],
            concurrence_lists[13],
            concurrence_lists[14],
            concurrence_lists[15],
            concurrence_lists[16],
            concurrence_lists[17],
            concurrence_lists[18],

            sign_lists[0],
            sign_lists[1],
            sign_lists[2],
            sign_lists[3],
            sign_lists[4],
            sign_lists[5],
            sign_lists[6],
            sign_lists[7],
            sign_lists[8],
            sign_lists[9],
            sign_lists[10],
            sign_lists[11],
            sign_lists[12],
            sign_lists[13],
            sign_lists[14],

            action_lists[0],
            action_lists[1],
            action_lists[2],
            action_lists[3],
            action_lists[4],
            action_lists[5],
            action_lists[6],

            medicine_list[0],
            medicine_list[1],
            medicine_list[2],
            medicine_list[3],

            medicine_effect_result[0],
            medicine_effect_result[1],
            medicine_effect_result[2],
            medicine_effect_result[3],
            medicine_effect_result[4],

            family_lists[0],
            family_lists[1],
            family_lists[2],
            family_lists[3],
            family_lists[4],
            family_lists[5],

            past_lists[0],
            past_lists[1],
            past_lists[2],
            past_lists[3],
            past_lists[4],
            past_lists[5],
            past_lists[6],
            past_lists[7],
            past_lists[8],
            past_lists[9],
            past_lists[10],
            past_lists[11],
            
            ]]

    st.write("______________________")
    first_diag_list = ["片頭痛MOH","緊張型頭痛","TACs","その他一次性頭痛","二次性頭痛"]
    first_diag = st.radio("●診察医の最初の診断",first_diag_list,horizontal=True)

    if first_diag == first_diag_list[0]:
        first_diag_result = 1
        first_diag_result2 = first_diag_list[0]

    elif first_diag == first_diag_list[1]:
        first_diag_result = 2
        first_diag_result2 = first_diag_list[1]

    elif first_diag == first_diag_list[2]:
        first_diag_result = 3
        first_diag_result2 = first_diag_list[2]

    elif first_diag == first_diag_list[3]:
        first_diag_result = 4
        first_diag_result2 = first_diag_list[3]

    elif first_diag == first_diag_list[4]:
        first_diag_result = 0
        first_diag_result2 = first_diag_list[4]

    df = pd.DataFrame(data,columns=column)

    st.write("______________________")

    model = pickle.load(open("./test.pkl","rb"))

    pred = model.predict(data=df)
    pred_labels = np.argmax(pred,axis=1)

    if pred_labels == 0:
        result = "二次性頭痛"

    elif pred_labels == 1:
        result = "片頭痛MOH"

    elif pred_labels == 2:
        result = "緊張型頭痛"

    elif pred_labels == 3:
        result = "TACs"

    elif pred_labels == 4:
        result = "その他一次性頭痛"



    st.subheader("AI診断結果")
    with st.expander("診断結果を表示"):
        st.info("AI診断結果:"+result,icon="ℹ️")

    st.write("______________________")
    second_diag_list = ["片頭痛MOH","緊張型頭痛","TACs","その他一次性頭痛","二次性頭痛"]
    second_diag = st.radio("●診察医がAIの結果を見た後の診断",second_diag_list,horizontal=True,key=500)

    if second_diag == second_diag_list[0]:
        second_diag_result = 1
        second_diag_result2 = second_diag_list[0]

    elif second_diag == second_diag_list[1]:
        second_diag_result = 2
        second_diag_result2 = second_diag_list[1]

    elif second_diag == second_diag_list[2]:
        second_diag_result = 3
        second_diag_result2 = second_diag_list[2]

    elif second_diag == second_diag_list[3]:
        second_diag_result = 4
        second_diag_result2 = second_diag_list[3]

    elif second_diag == second_diag_list[4]:
        second_diag_result = 0
        second_diag_result2 = second_diag_list[4]
            
    df["AI前_診断結果名称"] = first_diag_result2
    df["AI前_診断結果"] = first_diag_result
    df["AI_診断結果名称"] = result
    df["AI_診断結果"] = pred_labels
    df["AI後_診断結果名称"] = second_diag_result2
    df["AI後_診断結果"] = second_diag_result
    df.insert(0, '病院名', hospital)
    df.insert(1, '受診日', consultation_date)
    csv = convert_df(df)
    if hospital == "":
        st.warning("病院名を入力してください")
        st.stop()
    if st.button(label="データ登録"):
        register(df)
        st.success("データ登録しました。")