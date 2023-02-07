import streamlit as st
import numpy as np

st.subheader("仙台頭痛脳神経クリニックAI頭痛診断-ver.00-")
st.write("______________________")
st.subheader("基本情報")
gender = st.radio("●性別",["男性", "女性"],horizontal=True)

age = st.number_input("●初診時年齢[歳]",step=1)
# st.write("______________________")
height = st.number_input("●身長[cm]",step=0.1)
weight = st.number_input("●体重[kg]",step=0.1)
try:
    bmi = weight/(height/100)/(height/100)
    st.write("BMI:",np.round(bmi,2))
except:
    pass
hand = st.radio("●利き手",["右", "左"],horizontal=True)
alchol = st.radio("●飲酒",["なし", "たまに","習慣的"],horizontal=True)
smoke = st.radio("●喫煙",["なし", "過去にあり","現在あり","自分は吸わないが受動喫煙あり"],horizontal=True)
st.write("______________________")

start_symptom_list = ["1週間以内", "1ヵ月以内","3ヵ月以内","1年以内","1年以上前から"]
start_symptom = st.radio("●今の頭痛はいつ頃からありますか?",start_symptom_list,horizontal=True)
st.write("______________________")
last_symptom = st.radio("●以前にも頭痛はありましたか？",["なし", "あり"],horizontal=True)
st.write("______________________")
freq_symptom_list = ["年に数回", "月に数回", "15日/月以上", "ほぼ毎日","不定期"]
freq_symptom = st.radio("●頭痛の起きる頻度は、おおむね、次のどれですか？",freq_symptom_list,horizontal=True)
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

st.write("______________________")
pain_score = st.slider("●痛くないときを0点、想像できる最悪の痛みを100点としたら、最もひどい頭痛の強さは何点になりますか？50点は顔をしかめる程度です。",0,100,50)
st.write("______________________")
change_symptom = st.radio("●痛みについて教えてください",["日に日に強くなっている", "日によって程度が違う","変化なし"],horizontal=True)

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

st.write("______________________")
medicine_check_list = ["飲まない","飲む"]
medicine_kind_list = ["市販薬","病院鎮痛薬","病院特効薬(レイボー、トリプタン)"]
medicine_check = st.radio("●頭痛のとき、薬を飲みますか?",medicine_check_list,horizontal=True)
if medicine_check == "飲む":
    medicine0 = st.checkbox(medicine_kind_list[0])
    medicine1 = st.checkbox(medicine_kind_list[1])
    medicine2 = st.checkbox(medicine_kind_list[2])
else:
    medicine0 = 0
    medicine1 = 0
    medicine2 = 0

medicine_list = [medicine_check,medicine0,medicine1,medicine2]

st.write("______________________")
medicine_effect_list = ["効く","あまり","効かない","効かなく","まちまち"]
medicine_effect = st.radio("●その薬の効果はどうですか？",medicine_effect_list,horizontal=True)
medicine_effect_result = list()
for check_list in medicine_effect_list:
    if check_list == medicine_effect:
        medicine_effect_result.append(1)
    else:
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

st.write("______________________")
past_symptom_list = ["子供のころよく腹痛があった", "子供のころ乗物酔いをしやすかった", "朝早くに目が覚める", "熟睡感がない","同じ姿勢でいることがおおい","デスクワークがおおい","運動不足","行動を起こすまで時間がかかる、おっくうだ","心配事が多い","喘息といわれた","慢性腎不全といわれた","心臓病といわれた"]
past_symptom_title = '<p style="font-past:sans-serif; color:Black; font-size: 14px;">●家族・兄弟・親戚に頭痛持ちの人はいますか。すべて選んでください。(複数選択可)</p>'
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