from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.myproject  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('posting_box.html')


## API 역할을 하는 부분
@app.route('/birds', methods=['GET'])
def make_bird_list():
    result = list(db.birds.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'birds': result})


@app.route('/gus', methods=['GET'])
def make_gu_list():
    result = list(db.gu_parks.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'gus': result})


@app.route('/post', methods=['POST'])
def test_post():
    gu_receive = request.form['gu_give']
    park_receive = request.form['park_give']
    bird_receive = request.form['bird_give']
    review_receive = request.form['review_give']
    print(gu_receive, park_receive, bird_receive, review_receive)
    post = {
        'gu': gu_receive,
        'park': park_receive,
        'bird': bird_receive,
        'review': review_receive
    }
    db.posts.insert_one(post)
    return jsonify({'result': 'success', 'msg': '기록완료!'})


# ## API 역할을 하는 부분
# @app.route('/birds', methods=['GET'])
# def test_get():
#     title_receive = request.args.get('title_give')
#     print(title_receive)
#     return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
