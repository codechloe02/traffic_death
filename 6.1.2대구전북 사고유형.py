import numpy as np
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 한글 폰트 설정
font_path = 'C:/Windows/Fonts/malgun.ttf'  # 한글 폰트 파일 경로에 맞게 변경
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

#엑셀파일 읽어오기
file1 = pd.read_excel('사고유형.xls')
data = pd.concat([file1])
# 가공하기
daegu = data[data['시도']=='대구']
jeonbuk = data[data['시도']=='전북']

df = pd.concat([daegu, jeonbuk], ignore_index=True)
schools = ["횡단중","차도통행중","길가장자리구역통행중","보도통행중","기타","정면충돌","측면충돌","추돌","기타"]
df.drop('시도', axis='columns', inplace=True)
df.drop('사고유형중분류', axis='columns', inplace=True)
#print(df)
#print(df.loc[1])
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df.loc[0],
    y=schools,
    marker=dict(color="crimson", size=12),
    mode="markers",
    name="대구",
))

fig.add_trace(go.Scatter(
    x=df.loc[2],
    y=schools,
    marker=dict(color="gold", size=12),
    mode="markers",
    name="전북",
))


fig.update_layout(title="대구와 전북의 사고유형",
                  xaxis_title="사고발생 수",
                  yaxis_title="사고유형")

fig.show()
fig.write_html('6.1.2대구전북 사고유형.html')