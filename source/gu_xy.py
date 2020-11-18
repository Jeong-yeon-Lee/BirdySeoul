from pymongo import MongoClient  # pymongo를 임포트 하기

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.myproject


종로구 = [37.593447, 126.975096]
중구 = [37.560101, 126.995831]
도봉구 = [37.668868, 127.032700]
노원구 = [37.651611, 127.074264]
강북구 = [37.643405, 127.010816]
성북구 = [37.601372, 127.016652]
동대문구 = [37.581530, 127.055874]
중랑구 = [37.597221, 127.094161]
은평구 = [37.617777, 126.927491]
서대문구 = [37.576369, 126.939608]
마포구 = [37.558597, 126.909844]
용산구 = [37.530788, 126.980280]
성동구 = [37.549919, 127.041581]
광진구 = [37.545994, 127.087415]
강동구 = [37.549703, 127.146770]
송파구 = [37.506234, 127.116353]
강남구 = [37.496844, 127.064849]
서초구 = [37.473003, 127.030152]
동작구 = [37.499129, 126.950398]
관악구 = [37.467491, 126.946650]
영등포구 = [37.522463, 126.911609]
금천구 = [37.461483, 126.899549]
구로구 = [37.493989, 126.854779]
양천구 = [37.523479, 126.855878]
강서구 = [37.561841, 126.819118]

doc = {
    'x': 종로구[0],
    'y': 종로구[1],
    'gu': "종로구"
}

db.gu_xy.insert_one(doc)

doc = {
    'x': 중구[0],
    'y': 중구[1],
    'gu': "중구"
}

db.gu_xy.insert_one(doc)

doc = {
    'x': 도봉구[0],
    'y': 도봉구[1],
    'gu': "도봉구"
}

db.gu_xy.insert_one(doc)

doc = {
    'x': 노원구[0],
    'y': 노원구[1],
    'gu': "노원구"
}

db.gu_xy.insert_one(doc)

doc = {
    'x': 강북구[0],
    'y': 강북구[1],
    'gu': "강북구"
}

db.gu_xy.insert_one(doc)

doc = {
    'x': 성북구[0],
    'y': 성북구[1],
    'gu': "성북구"
}

db.gu_xy.insert_one(doc)

doc = {
    'x': 동대문구[0],
    'y': 동대문구[1],
    'gu': "동대문구"
}

db.gu_xy.insert_one(doc)

doc = {
    'x': 중랑구[0],
    'y': 중랑구[1],
    'gu': "중랑구"
}

db.gu_xy.insert_one(doc)

doc = {
    'x': 은평구[0],
    'y': 은평구[1],
    'gu': "은평구"
}

db.gu_xy.insert_one(doc)

doc = {
    'x': 서대문구[0],
    'y': 서대문구[1],
    'gu': "서대문구"
}

db.gu_xy.insert_one(doc)

doc = {
    'x': 마포구[0],
    'y': 마포구[1],
    'gu': "마포구"
}

db.gu_xy.insert_one(doc)

doc = {
    'x': 용산구[0],
    'y': 용산구[1],
    'gu': "용산구"
}

db.gu_xy.insert_one(doc)


doc = {
    'x': 성동구[0],
    'y': 성동구[1],
    'gu': "성동구"
}

db.gu_xy.insert_one(doc)

doc = {
    'x': 광진구[0],
    'y': 광진구[1],
    'gu': "광진구"
}

db.gu_xy.insert_one(doc)

doc = {
    'x': 강동구[0],
    'y': 강동구[1],
    'gu': "강동구"
}

db.gu_xy.insert_one(doc)

doc = {
    'x': 송파구[0],
    'y': 송파구[1],
    'gu': "송파구"
}

db.gu_xy.insert_one(doc)

doc = {
    'x': 강남구[0],
    'y': 강남구[1],
    'gu': "강남구"
}

db.gu_xy.insert_one(doc)

doc = {
    'x': 서초구[0],
    'y': 서초구[1],
    'gu': "서초구"
}

db.gu_xy.insert_one(doc)

doc = {
    'x': 동작구[0],
    'y': 동작구[1],
    'gu': "강남구"
}

db.gu_xy.insert_one(doc)

doc = {
    'x': 금천구[0],
    'y': 금천구[1],
    'gu': "금천구"
}

db.gu_xy.insert_one(doc)

doc = {
    'x': 구로구[0],
    'y': 구로구[1],
    'gu': "구로구"
}

db.gu_xy.insert_one(doc)


doc = {
    'x': 양천구[0],
    'y': 양천구[1],
    'gu': "양천구"
}

db.gu_xy.insert_one(doc)

doc = {
    'x': 강서구[0],
    'y': 강서구[1],
    'gu': "강서구"
}

db.gu_xy.insert_one(doc)