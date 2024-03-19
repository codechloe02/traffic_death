import folium
import pandas as pd 
from folium import Marker
#각 지자체 위도 경도가 들어있는 자료
data1=pd.read_csv('korea_np.csv')
#지자체 교통사고 자료
data2=pd.read_excel('지자체 교통사고.xls')
print(data1.columns)
print(data2.columns)

#두데이터 합치기 (기준열 이름이 달라 각각 정하고 합집합으로 가저오기)
data=pd.merge(data1,data2, left_on='Name',right_on='시도', how='outer')
print(data)
#빈값이 들어간 행렬 삭제
data.drop(17,axis=0,inplace=True)
print(data)
#지도맵 기준과 줌크기, 스타일 설정
m= folium.Map(location=[35.819437,127.106375], zoom_start=6.5,tiles='cartodbpositron')
#for문으로 맵에 marker 찍기
for _, i in data.iterrows():
        #팝업 설정 html문자로 저장함 크기, size 상세설정 가능
        popup_content=f"""
        <div style="max-width: 150px; font-size: 10px;">
            <strong>{i['Name']}</strong><br>
            사고: {i['사고[건]']}건<br>
            사망: {i['사망[명]']}명<br>
            부상: {i['부상[명]']}명
        </div>
        """ 
        #위도, 경도값 가져오기
        Marker(
        location=[i['decimalLatitude'],i['decimalLongitude']],
        #위의 팝업 설정한값 가져오고, 아이콘 지정
        popup=folium.Popup(popup_content,max_width=150),icon=folium.Icon(color='red',icon='info-sign')
        ).add_to(m)

m.save("1.Map.html")