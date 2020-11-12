from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.myproject


@app.route('/')
def home():
    return render_template('select_gu.html')


# @app.route('/memo', methods=['POST'])
# def post_article():
#     # 1. 클라이언트로부터 데이터를 받기
#     # 2. meta tag를 스크래핑하기
#     # 3. mongoDB에 데이터 넣기
#     return jsonify({'result': 'success', 'msg': 'POST 연결되었습니다!'})


@app.route('/gu', methods=['GET'])
def show_gu_parks():
    gu_receive = request.args.get('gu_give')
    parks = list(db.gu_parks.find({'gu': gu_receive}, {'_id': 0}))
    print(gu_receive)
    return jsonify({'result': 'success', 'parks': parks})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
