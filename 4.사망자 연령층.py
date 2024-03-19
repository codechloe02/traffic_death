import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_excel('연령층별 사망자.xls')
print(df.head())
#필요없는 행열 삭제
df.drop('합계', axis='columns', inplace=True)
df.drop('불명', axis='columns', inplace=True)
df.drop(0, axis=0, inplace=True)
print(df)
sido = df[['시도']]
print(sido)
fig = go.Figure()
#x,y 데이터 넣기
x_data = df.loc[:,'시도'].to_list()
y_data = df.columns[1:].to_list()
print(type(x_data), " : ", x_data)
print(type(y_data), " : ", y_data)
#for문으로 시각화 scatter로 보여주기위해 데이터값 넣음 
for index, value in enumerate(y_data):
    fig.add_trace(go.Scatter
                  (
                    #x,y 지정
                    x=df.loc[:, '시도'].to_list(),
                    y=df.loc[:, value].to_list(),
                    mode='markers',
                    name=value,
                    #마커사이즈는 value값으로, 디자인적용
                    marker=dict(
                        size=df.loc[:, value].to_list(), line=dict(width=0.5,color='white'),
                    )
                  )
    )
#레이아웃 타이틀, 디자인 적용    
fig.update_layout(title='지역별 사망자 연령층',xaxis=dict(title='지자체'),yaxis=dict(title='사망자수'),
                  template='plotly_dark')
fig.show()
fig.write_html('4.사망자 연령층.html')
