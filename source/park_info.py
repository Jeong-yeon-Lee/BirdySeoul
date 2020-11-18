from pymongo import MongoClient  # pymongo를 임포트 하기

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.myproject

park = ["광나루한강공원", "서울 강동구 암사동 659-1", "02-3780-0501"]

doc = {
    'name': park[0],
    'address': park[1],
    'phone': park[2]

}

db.park_info.insert_one(doc)
