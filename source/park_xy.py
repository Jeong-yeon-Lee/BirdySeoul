from pymongo import MongoClient  # pymongo를 임포트 하기

client = MongoClient('mongodb://test:test@localhost',
                      27017)
#client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.myproject

parks = [[37.580836, 127.007505, "낙산공원"], [37.590672, 126.990683, "와룡공원"],
         [37.571227, 126.988332, "탑골공원"], [37.590470, 126.985923, "삼청공원"],
         [37.580594, 127.002846, "마로니에공원"], [37.575815, 126.967641, "사직공원"],
         [37.590630, 126.966191, "청운공원"], [37.578864, 126.994859, "창경궁"],
         [37.555347, 126.964656, "손기정체육공원"], [37.551762, 126.988244, "남산공원"],
         [37.557858, 127.004376, "장충단공원"], [37.521796, 126.983992, "용산가족공원"],
         [37.524263, 126.953127, "이촌한강공원"], [37.545210, 126.960336, "효창공원"],
         [37.544820, 127.039237, "서울숲"], [37.572460, 127.038570, "청계8경버들습지"],
         [37.551755, 127.098536, "아차산생태공원"], [37.549036, 127.081559, "어린이대공원"],
         [37.529230, 127.071367, "뚝섬한강공원"], [37.581117, 127.063864, "배봉산근린공원"],
         [37.589385, 127.046238, "홍릉근린공원"], [37.593635, 127.043962, "홍릉숲"],
         [37.574550, 127.063448, "답십리공원"], [37.580176, 127.095286, "사가정공원"],
         [37.607552, 127.091927, "봉화산근린공원"], [37.596889, 127.070245, "중랑천길"],
         [37.620752, 127.006355, "북한산생태숲"], [37.595786, 127.007098, "성북근린공원"],
         [37.598153, 127.025396, "개운산공원"], [37.600752, 127.050264, "청량근린공원"],
         [37.621107, 127.008550, "삼각산도시자연공원"],
         [37.621036, 127.040798, "북서울꿈의숲"], [37.653044, 127.011841, "솔밭근린공원"],
         [37.610505, 127.043383, "오동근린공원 "], [37.689427, 127.048109, "서울창포원"],
         [37.647198, 127.045956, "초안산생태공원"], [37.653413, 127.028840, "쌍문근린공원"],
         [37.675884, 127.080915, "수락산공원"], [37.664548, 127.082440, "불암산자연공원"],
         [37.629497, 126.923957, "향림근린공원"], [37.592590, 126.910198, "신사근린공원"],
         [37.619678, 126.930085, "불광근린공원"], [37.640907, 126.925605, "진관근린공원"],
         [37.647036, 126.926369,
          "못자리골근린공원"], [37.639551, 126.914448, "탑골생태공원"],
         [37.611316, 126.940118, "북한산생태공원"], [37.654784, 126.945045, "진관동습지"],
         [37.571957, 126.942962, "안산도시자연공원"], [37.562549, 126.894631, "월드컵공원"],
         [37.572099, 126.868290, "난지한강공원생태습지원"],
         [37.512026, 126.834780, "힐링생태공원"], [37.527680, 126.829873, "서서울호수공원"],
         [37.542266, 126.877522, "용왕산근린공원"], [37.510361, 126.855472, "계남근린공원"],
         [37.534651, 126.877123, "파리근린공원"], [37.507275, 126.868794, "갈산근린공원"],
         [37.586572, 126.818705, "강서습지생태공원"],
         [37.573399, 126.836253, "서울식물원습지생태공원"],
         [37.542200, 126.854704, "봉제산공원"], [37.583396, 126.804813, "개화근린공원"],
         [37.581039, 126.813845, "방화근린공원"], [37.558231, 126.867512, "염창근린공원"],
         [37.554354, 126.845066,
          "우장산근린공원"], [37.580062, 126.815784, "꿩고개근린공원"],
         [37.484018, 126.825605, "푸른수목원"], [37.500511, 126.837052, "온수도시자연공원"],
         [37.488490, 126.846346, "개웅산근린공원"],
         [37.489846, 126.874155, "신구로유수지생태공원"],
         [37.469532, 126.908173, "감로천생태공원"], [37.473716, 126.909464, "독산자연공원"],
         [37.543221, 126.900117, "선유도공원"], [37.504072, 126.894785, "영등포생태공원"],
         [37.523893, 126.918937, "여의도공원"], [37.518504, 126.920401, "샛강생태공원"],
         [37.528975, 126.890122, "양평유수지생태공원"],
         [37.491914, 126.919365, "보라매공원"], [37.503549, 126.975505, "국립현충원"],
         [37.476919, 126.968564, "까치산근린공원"], [37.508337, 126.954072, "노량진공원"],
         [37.466825, 126.914711, "관악산생태공원"], [37.471186, 126.959980, "낙성대공원"],
         [37.470710, 127.035542, "양재시민의숲"], [37.521530, 127.011855, "잠원한강공원"],
         [37.480258, 127.075457, "인능산도시자연공원"],
         [37.467432, 127.019041,
          "우면산자연생태공원"], [37.509807, 126.994765, "반포한강공원"],
         [37.476523, 127.041788, "양재천근린공원"],
         [37.478066, 127.081247,
          "대모산도시자연공원"], [37.485108, 127.047070, "도곡근린공원"],
         [37.524505, 127.035355, "청담근린공원"], [37.521357, 127.052572, "청담근린공원"],
         [37.487631, 127.106349, "탄천어울림공원"], [37.520783, 127.121492, "올림픽공원"],
         [37.503542, 127.131377, "오금근린공원"], [37.500356, 127.156826, "천마근린공원"],
         [37.495457, 127.138390, "장지근린공원"], [37.523241, 127.099601, "생태화공원"],
         [37.512074, 127.139998, "방이동보전지역"], [37.555421, 127.122893, "암사생태공원"],
         [37.532168, 127.150892,
          "일자산도시자연공원"], [37.540621, 127.155319, "길동생태공원"],
         [37.544264, 127.126455, "천호공원"], [37.553028, 127.160757, "명일근린공원"],
         [37.548862, 127.119974, "광나루한강공원"]]

# add = 0
# for i in range(0, 104):
#     doc = {
#         'x': parks[i][0],
#         'y': parks[i][1],
#         'park': parks[i][2]
#     }
# print(doc)
# db.park_xy.insert_one(doc)

p = [37.524337, 127.035334, "도산근린공원"]
doc = {'x': p[0], 'y': p[1], 'park': p[2]}

db.park_xy.insert_one(doc)