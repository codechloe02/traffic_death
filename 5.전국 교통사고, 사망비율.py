import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import folium
from matplotlib import font_manager, rc
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 한글 폰트 설정
font_path = 'C:/Windows/Fonts/malgun.ttf'  # 한글 폰트 파일 경로에 맞게 변경
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

#엑셀파일 읽어오기
file1 = pd.read_excel('지역별사망률.xls')
result = pd.concat([file1])
#읽어온것 확인해보기
print(result)
# 가공하기
column_name = '사고'
column_sum = file1[column_name].sum()
file1['사고율'] = (file1[column_name] / column_sum) * 100

file2 = file1.copy()
column_name2 = '사망'
column_sum2 = file2[column_name2].sum()
file2['사망율'] = (file2[column_name2] / column_sum2) * 100

labels = ["서울", "부산", "대구", "인천", "광주","대전","울산","세종","경기","강원","충북","충남","전북","전남","경북","경남","제주"]

# subplot 생성
fig = make_subplots(1, 2, specs=[[{'type':'domain'}, {'type':'domain'}]],
                    subplot_titles=['지역별 교통사고율', '지역별 교통사망율'])

# 첫 번째 subplot
fig.add_trace(go.Pie(labels=file1['광역지자체'], values=file1['사고'], scalegroup='one',
                     name="사고(횟수)"), 1, 1)

# 두 번째 subplot
fig.add_trace(go.Pie(labels=file2['광역지자체'], values=file2['사망'], scalegroup='two',
                     name="사망자(수)"), 1, 2)

fig.update_layout(title_text='지역별 사고와 사망 비율')
fig.show()
fig.write_html('5.전국 교통사고, 사망비율.html')