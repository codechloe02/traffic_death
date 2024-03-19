import folium as fig
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
#데이터 가져오기
data = pd.read_excel('지자체 교통사고.xls')
print(data)
data.head()
#필요없는 데이터 삭제하기
data.drop(0, axis=0, inplace=True)
#사망률 구하기 밑에서 % 처리할 예정
data['사망률']=round((data['사망[명]']/data['사고[건]']),5)
print(data['사망률'])
print(data)
#사망률에 대하여 오름차순으로 정렬하기
data.sort_values(by=['사망률'],inplace=True)
print(data)
fig=go.Figure(
    #bar형식으로 시각화 하고 marker에 색 추가하기
    data=[go.Bar(y=data['사망률'],x=data['시도'],marker=dict(color=px.colors.qualitative.Dark24))])
#타이틀 설정, y축 %처리(소수 둘째자리까지)
fig.update_layout(yaxis_tickformat='.2%',
    title="지자체별 사고대비 사망률",title_x=0.5,xaxis=dict(title='지자체'),
    yaxis=dict(title='사망률(%)'))
fig.show()
fig.write_html('6.0전국 사고대비 사망률.html')