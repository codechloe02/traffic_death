import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_excel('도로형태별 사고.xls')
print(data)
#한프레임에 그래프 2개 출력, y축 2개 사용지정
fig=make_subplots(rows=1,cols=2,                     
                  specs=[[{"secondary_y": True}, {"secondary_y": True}]])
#대구, 전북 데이터값만 불러오기
daegu = data[data['시도']=='대구']
jeonbuk = data[data['시도']=='전북']
print(daegu)
print(jeonbuk)
#두 데이터 합치기
df = pd.concat([daegu, jeonbuk], ignore_index=True)
#필요없는 데이터 제외 시키기
df.drop('도로형태대분류 ', axis='columns', inplace=True)
df.drop('철길건널목', axis='columns', inplace=True)
df.drop('시도', axis='columns', inplace=True)
#그래프 추가
fig.add_trace(
    #데이터값 지정, 위치지정, y축 활성화
    go.Scatter(y=df.loc[0], x=df.columns, name='대구 교통사고 건수'),row=1, col=1, secondary_y=True,)
fig.add_trace(
    go.Scatter(y=df.loc[2], x=df.columns, name='전북 교통사고 건수'),row=1, col=1, secondary_y=True,)
fig.add_trace(
    go.Scatter(y=df.loc[1], x=df.columns, name='대구 교통사고 사망자수'),row=1, col=2, secondary_y=True,)
fig.add_trace(
    go.Scatter(y=df.loc[3], x=df.columns, name='전북 교통사고 사망자수'),row=1, col=2, secondary_y=True,)
#그래프 디자인 상세 지정
fig.update_layout(title='도로형태별 교통사고 비교',template='plotly_dark')
fig.show()
fig.write_html('6.3대구전북 도로형태별사고.html')