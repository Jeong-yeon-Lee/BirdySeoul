from pymongo import MongoClient  # pymongo를 임포트 하기

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.myproject

jong_no = ["낙산공원", "와룡공원", "탑골공원", "삼청공원", "마로니에공원", "사직공원", "청운공원", "창경궁"]
jung = ["손기정체육공원", "남산공원", "장충단공원"]
yong_san = ["용산가족공원", "이촌한강공원", '효창공원']
seong_dong = ["서울숲", "청계8경버들습지"]
gwang_jin = ["아차산생태공원", "어린이대공원", "뚝섬한강공원"]
dong_dae_mun = ["배봉산근린공원", "홍릉근린공원", "홍릉숲", "답십리공원"]
jung_nang = ["사가정공원", "봉화산근린공원", "중랑천길"]
seong_buk = ["북한산생태숲", "성북근린공원", "개운산공원", "청량근린공원", ]
gang_buk = ["삼각산도시자연공원", "북서울꿈의숲", "솔밭근린공원", "오동근린공원"]
do_bong = ["서울창포원", "초안산생태공원", "쌍문근린공원"]
no_won = ["수락산공원", "불암산자연공원"]
eun_pyeong = ["향림근린공원", "신사근린공원", "불광근린공원", "진관근린공원", "못자리골근린공원", "탑골생태공원", "북한산생태공원", "진관동습지"]
seo_dae_mun = ["안산도시자연공원"]
ma_po = ["월드컵공원", "난지한강공원생태습지원"]
yang_cheon = ["힐링생태공원", "서서울호수공원", "용왕산근린공원", "계남근린공원", "파리근린공원", "갈산근린공원"]
gang_seo = ["강서습지생태공원", "서울식물원습지생태공원", "봉제산공원", "개화근린공원", "방화근린공원", "염창근린공원", "우장산근린공원", "꿩고개근린공원"]
gu_ro = ["푸른수목원", "온수도시자연공원", "개웅산근린공원", "신구로유수지생태공원"]
geum_cheon = ["만수천공원", "감로천생태공원", "독산자연공원", ]
yeong_deung_po = ["선유도공원", "영등포생태공원", "여의도공원", "샛강생태공원", "양평유수지생태공원"]
dong_jak = ["보라매공원", "국립현충원", "까치산근린공원", "노량진공원"]
gwan_ak = ["관악산생태공원", "낙성대공원"]
seo_cho = ["양재시민의숲", "잠원한강공원", "인능산도시자연공원", "우면산자연생태공원", "반포한강공원", "양재천근린공원"]
gang_nam = ["대모산도시자연공원", "도곡근린공원", "도산근린공원", "청담근린공원", "탄천어울림공원"]
song_pa = ["올림픽공원", "오금근린공원", "천마근린공원", "장지근린공원", "생태화공원", "방이동보전지역"]
gang_dong = ["암사생태공원", "일자산도시자연공원", "길동생태공원", "천호공원", "명일근린공원", "광나루한강공원"]

for park in jong_no:
    doc = {
        'name': park,
        'gu': "종로구"
    }

    db.gu_parks.insert_one(doc)


for park in jung:
    doc = {
        'name': park,
        'gu': "중구"
    }

    db.gu_parks.insert_one(doc)

for park in yong_san:
    doc = {
        'name': park,
        'gu': "용산구"
    }

    db.gu_parks.insert_one(doc)


for park in seong_dong:
    doc = {
        'name': park,
        'gu': "성동구"
    }

    db.gu_parks.insert_one(doc)

for park in gwang_jin:
    doc = {
        'name': park,
        'gu': "광진구"
    }

    db.gu_parks.insert_one(doc)

for park in dong_dae_mun:
    doc = {
        'name': park,
        'gu': "동대문구"
    }

    db.gu_parks.insert_one(doc)

for park in jung_nang:
    doc = {
        'name': park,
        'gu': "중랑구"
    }

    db.gu_parks.insert_one(doc)

for park in seong_buk:
    doc = {
        'name': park,
        'gu': "성북구"
    }

    db.gu_parks.insert_one(doc)

for park in gang_buk:
    doc = {
        'name': park,
        'gu': "강북구"
    }

    db.gu_parks.insert_one(doc)

for park in do_bong:
    doc = {
        'name': park,
        'gu': "도봉구"
    }

    db.gu_parks.insert_one(doc)

for park in no_won :
    doc = {
        'name': park,
        'gu': "노원구"
    }

    db.gu_parks.insert_one(doc)

for park in eun_pyeong:
    doc = {
        'name': park,
        'gu': "은평구"
    }

    db.gu_parks.insert_one(doc)

for park in seo_dae_mun:
    doc = {
        'name': park,
        'gu': "서대문구"
    }

    db.gu_parks.insert_one(doc)

for park in ma_po:
    doc = {
        'name': park,
        'gu': "마포구"
    }

    db.gu_parks.insert_one(doc)

for park in yang_cheon:
    doc = {
        'name': park,
        'gu': "양천구"
    }

    db.gu_parks.insert_one(doc)

for park in gang_seo:
    doc = {
        'name': park,
        'gu': "강서구"
    }

    db.gu_parks.insert_one(doc)

for park in gu_ro:
    doc = {
        'name': park,
        'gu': "구로구"
    }

    db.gu_parks.insert_one(doc)

for park in geum_cheon :
    doc = {
        'name': park,
        'gu': "금천구"
    }

    db.gu_parks.insert_one(doc)

for park in yeong_deung_po:
    doc = {
        'name': park,
        'gu': "영등포구"
    }

    db.gu_parks.insert_one(doc)

for park in dong_jak:
    doc = {
        'name': park,
        'gu': "동작구"
    }

    db.gu_parks.insert_one(doc)

for park in gwan_ak:
    doc = {
        'name': park,
        'gu': "관악구"
    }

    db.gu_parks.insert_one(doc)

for park in seo_cho:
    doc = {
        'name': park,
        'gu': "서초구"
    }

    db.gu_parks.insert_one(doc)

for park in gang_nam:
    doc = {
        'name': park,
        'gu': "강남구"
    }

    db.gu_parks.insert_one(doc)

for park in song_pa:
    doc = {
        'name': park,
        'gu': "송파구"
    }

    db.gu_parks.insert_one(doc)

for park in gang_dong:
    doc = {
        'name': park,
        'gu': "강동구"
    }

    db.gu_parks.insert_one(doc)


