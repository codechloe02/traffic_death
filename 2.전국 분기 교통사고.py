import folium as fig
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
data = pd.read_excel('전국월별사고.xls', index_col='시도')
print(data)

fig = px.bar(data, x=data.index, y=data.columns, title="전국 분기별 사고건")
fig.update_layout(yaxis_tickformat='number',
    title="전국 분기별 사고건",title_x=0.5,xaxis=dict(title='지자체'),
    yaxis=dict(title='사고건수'))
fig.show()
fig.write_html('2.전국 분기 교통사고.html')