import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import folium
from matplotlib import font_manager, rc
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#엑셀파일 읽어오기
file1 = pd.read_excel('도로종류최종.xlsx')
data = pd.concat([file1])
#읽어온것 확인해보기
print(data)

daegu = data[data['시도']=='대구']
jeonbuk = data[data['시도']=='전북']
print(daegu)
print(jeonbuk)

df = pd.concat([daegu, jeonbuk], ignore_index=True)
# 인덱스 이름 바꾸기
df2 = df.rename(index={0:'대구사고',1:'대구사망',2:'전북사고',3:'전북사망'})
# 필요없는 열 제거
df3 = df2.drop(['시도','기준년도','2022'], axis='columns', inplace=False)
# 인덱스 이름으로 원하는 행만 구하기
# df4 = df3.loc[['대구사고']]
# df5 = df3.loc[['대구사망']]
# print(df4)

labels=["일반국도", "지방도", "특별광역시도", "시도", "군도", "고속국도", "기타"]

fig = make_subplots(1, 4, specs=[[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}, {'type':'domain'}]],
                    subplot_titles=['대구의 도로별 교통사고율', '대구의 도로별 교통사망율','전북의 도로별 교통사고율', '전북의 도로별 교통사망율'])

# 첫 번째 subplot
fig.add_trace(go.Pie(labels=labels, values=df3.loc['대구사고'], scalegroup='one',
                     name="사고(횟수)"), 1, 1)

# 두 번째 subplot
fig.add_trace(go.Pie(labels=labels, values=df3.loc['대구사망'], scalegroup='two',
                     name="사망자(수)"), 1, 2)

# 세 번째 subplot
fig.add_trace(go.Pie(labels=labels, values=df3.loc['전북사고'], scalegroup='three',
                     name="사고(횟수)"), 1, 3)

# 네 번째 subplot
fig.add_trace(go.Pie(labels=labels, values=df3.loc['전북사망'], scalegroup='four',
                     name="사망자(수)"), 1, 4)

fig.show()
fig.write_html('6.2대구전북 도로별.html')



