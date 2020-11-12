from pymongo import MongoClient  # pymongo를 임포트 하기

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.myproject

# nack_san = ["낙산공원", "02-743-7985", "서울 종로구 낙산길 41", "매일 00:00-24:00", "무료입장"]
#
# for park in nack_san:
#     doc = {
#         'name': park[0],
#         'phone': park[1],
#         'address': park[2],
#         'open': park[3],
#         'cost': park[4],
#     }
#
#     db.park_info.insert_one(doc)
