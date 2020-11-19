from pymongo import MongoClient  # pymongo를 임포트 하기

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.myproject

park = ["서울숲", "서울특별시 성동구 성수동1가 뚝섬로 273", "02-460-2905"]

doc = {
    'name': park[0],
    'address': park[1],
    'phone': park[2]

}

db.park_info.insert_one(doc)
