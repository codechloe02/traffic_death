import geokakao as gk
import pandas as pd
import json
#주소만으로 위도, 경도값 가져오기
#json 읽어 저장하는데 광역지자체는 Name으로 소재지는 adress로 변경
with open('전국자치도 주소.json','r',encoding='utf-8') as file:
    json_data = json.load(file)
    data=[{'Name':entry['광역지자체'], 'Address':entry['소재지']}for entry in json_data]
    print(data)
#데이터프레임으로 작업하기 위해 pd로 가져옴
df = pd.DataFrame(data)


#이 주소를 좌표로 변환하여 데이터프레임에 추가하고, 이를 CSV로 저장하는 작업을 수행 
gk.add_coordinates_to_dataframe(df, 'Address')
df.to_csv('korea_np.csv', index=False, encoding='utf-8')
