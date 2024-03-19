import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import folium
from matplotlib import font_manager, rc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd

file1 = pd.read_excel('연령층별교통법규위반.xlsx', skiprows=[1,2])
data = pd.concat([file1])

# 사고와 사망 데이터 나누기
sago = data[data['법규위반내용 중분류']=='사고[건]']
samang = data[data['법규위반내용 중분류']=='사망[명]']
# 사고와 사망데이터를 나눴으니 사고,사망에 대한 데이터가 들어있는 열 제거
sago.drop('법규위반내용 중분류', axis='columns', inplace=True)
samang.drop('법규위반내용 중분류', axis='columns', inplace=True)


# 엑셀 데이터가 원하는 그래프에 적합하지 않아 데이터로 변경

# 사고 유형을 행의 숫자많큼 리스트에 넣기
df = []
for i in range(len(sago)):
    for j in sago.columns[1:] :
        df.append(j)
# 사고자의 나이를 열의 숫자만큼 리스트에 넣기
age_list = []
for j in sago['기본계획 연령별1'] :
    for i in range(len(sago.columns)-1) :
        age_list.append(j)
# 각 행의 데이터를 리스트에 넣기(사고자)
acd_count = []
for i in range(len(sago)):
    i = (i+1)*2-2
    # i = 사고의 인덱스 번호(사망,사고로 자른 탓에 인덱스 번호가 0,2,4... 짝수)
    for j in sago.loc[i,'과로':].to_list() :
        acd_count.append(j)
# 각 행의 데이터를 리스트에 넣기(사망자)
die_count = []
for i in range(len(samang)):
    i = (i+1)*2-1
    # i = 사망의 인덱스 번호(사망,사고로 자른 탓에 인덱스 번호가 1,3,5... 홀수)
    for j in samang.loc[i,'과로':].to_list() :
        die_count.append(j)


# 구한 리스트들을 데이터프레임에 넣기(사고)
data={'법규위반종류':df,'사고유형자나이':age_list,'사고수':acd_count}
df2 = pd.DataFrame(data=data)
df2 = df2.replace('-', np.nan) # 데이터가 없는 문자열 '-'를 NaN으로 변경
df2 = df2.replace({np.nan: None}) #NaN을 None으로 변환
# 구한 리스트들을 데이터프레임에 넣기(사망)
data2={'법규위반종류':df,'사고유형자나이':age_list,'사망수':die_count}
df3 = pd.DataFrame(data=data2)
df3 = df3.replace('-', np.nan) # 데이터가 없는 문자열 '-'를 NaN으로 변경
df3 = df3.replace({np.nan: None}) #NaN을 None으로 변환

fig = px.sunburst(df2, path=['법규위반종류', '사고유형자나이'], values='사고수')
# 사망자
# samang_last = px.sunburst(df3, path=['법규위반종류', '사고유형자나이'], values='사망수')

fig.show()
fig.write_html('3.교통사고 법귀위반.html')


