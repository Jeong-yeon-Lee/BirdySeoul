from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.myproject  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.

@app.route('/')
def home():
    return render_template('show_park.html')


# @app.route('/memo', methods=['POST'])
# def post_article():
#     # 1. 클라이언트로부터 데이터를 받기
#     # 2. meta tag를 스크래핑하기
#     # 3. mongoDB에 데이터 넣기
#     return jsonify({'result': 'success', 'msg': 'POST 연결되었습니다!'})


@app.route('/park_post', methods=['GET'])
def show_park_posts():
    park_receive = request.args.get('park_give')
    print(park_receive)
    result = list(db.posts.find({'park':park_receive}, {'_id': 0}))
    return jsonify({'result': 'success', 'park_posts': result})

# @app.route('/posts', methods=['GET'])
# def show_posts():
#     result = list(db.posts.find({}, {'_id': 0}))
#     return jsonify({'result': 'success', 'msg':'가져왔다리'})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)