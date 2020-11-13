from pymongo import MongoClient  # pymongo를 임포트 하기

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.myproject

nack_san = ["낙산공원", "02-743-7985", "서울 종로구 낙산길 41", "매일 00:00-24:00", "무료입장"]

doc = {
    'name': nack_san[0],
    'phone': nack_san[1],
    'address': nack_san[2],
    'open': nack_san[3],
    'cost': nack_san[4],
}

db.park_info.insert_one(doc)
