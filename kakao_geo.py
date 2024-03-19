
"""
geokakao는 주소 정보를 포함한 데이터프레임이 주어졌을 때, 
해당 주소로부터 좌표 정보(경도, 위도)를 알아내어 데이터프레임에 추가하고, 
이것을 다시 GeoPackage로 변환하는 과정을 처리합니다.

기능
Kakao API를 사용하여 주소를 좌표(경도, 위도)로 변환
주소 데이터를 포함하는 DataFrame에 좌표 정보 통합
보강된 DataFrame을 다시 GeoPackage 형식으로 변환

pip install geokakao

"""
import geokakao as gk
import pandas as pd
import json

# 샘플 데이터프레임을 생성해 보겠습니다. 데이터프레임의 "Address" 열은 주소 정보를 포함합니다.
data = {'Name': ['서울',
                 '부산',
                 '대구',
                 '인천',
                 '광주',
                 '대전',
                 '울산',
                 '세종',
                 '경기',
                 '강원',
                 '충북',
                 '충남',
                 '전북',
                 '전남',
                 '경북',
                 '강남',
                 '제주'
                 ],
        'Address': ['서울 중구 세종대로 110',
                    '부산 연제구 중앙대로 1001',
                    '대구 중구 공평로 88',
                    '인천 남동구 정각로 29',
                    '광주 서구 내방로 111',
                    '대전 서구 둔산로 100',
                    '울산 남구 중앙로 201',
                    '세종특별자치시 한누리대로 2130',
                    '경기 수원시 영통구 도청로 30',
                    '강원특별자치도 춘천시 중앙로 1',
                    '충북 청주시 상당구 상당로 82',
                    '충청남도 홍성군 홍북읍 충남대로 21',
                    '전북특별자치도 전주시 완산구 효자로 225',
                    '전라남도 무안군 삼향읍 오룡길 1',
                    '경상북도 안동시 풍천면 도청대로 455',
                    '경상남도 창원시 의창구 중앙대로 300',
                    '제주특별자치도 제주시 문연로 6'
                    ]}
df = pd.DataFrame(data)


# 이 주소를 좌표로 변환하여 데이터프레임에 추가하고, 이를 CSV로 저장하는 작업을 수행해 봅니다. 
gk.add_coordinates_to_dataframe(df, 'Address')
df.to_csv('korea_np.csv', index=False, encoding='utf-8')

# 이제 CSV 파일을 GeoPackage(GPKG) 파일로 변환할 수 있습니다.
input_csv = "korea_np.csv"
output_gpkg = "korea_np.gpkg"

gk.csv_to_gpkg(input_csv, output_gpkg)