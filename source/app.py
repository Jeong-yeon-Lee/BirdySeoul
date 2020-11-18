from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

##
open_url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1114052000'

res = requests.get(open_url)
soup = BeautifulSoup(res.content, 'html.parser')

data = soup.find_all('item')
##
app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.myproject


# 1. home
@app.route('/')
def home():
    return render_template('index.html')


### 2. select_gu
@app.route('/gu')
def select_gu():
    return render_template('select_gu.html')


# _api
@app.route('/api/gu', methods=['GET'])
def show_gu_parks():
    gu_receive = request.args.get('gu_give')
    parks = list(db.gu_parks.find({'gu': gu_receive}, {'_id': 0}))
    print(gu_receive)
    return jsonify({'result': 'success', 'parks': parks})


### 3. show_all_post
@app.route('/all_post')
def show_all_post():
    return render_template('show_all_post.html')


# api
@app.route('/api/option', methods=['GET'])
def make_options():
    result = list(db.gu_parks.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'gus': result})


@app.route('/api/all_post', methods=['GET'])
def show_all_posts():
    result = list(db.posts.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'posts': result})


@app.route('/api/selected_park_post', methods=['GET'])
def show_parks_posts():
    park_receive = request.args.get('park_give')
    result = list(db.posts.find({'park': park_receive}, {'_id': 0}))
    return jsonify({'result': 'success', 'posts': result})


### 4. show_park
@app.route('/park')
def show_park():
    return render_template('show_park.html')


# api
@app.route('/api/post', methods=['GET'])
def show_park_posts():
    park_receive = request.args.get('park_give')
    print(park_receive)
    result = list(db.posts.find({'park': park_receive}, {'_id': 0}))
    return jsonify({'result': 'success', 'park_posts': result})


@app.route('/api/park_info', methods=['GET'])
def show_park_info():
    park_receive = request.args.get('park_give')
    print(park_receive)
    result = list(db.park_info.find({'name': park_receive}, {'_id': 0}))
    return jsonify({'result': 'success', 'park_info': result})


### 5. posting_box
@app.route('/posting')
def posting_box():
    return render_template('posting_box.html')


# api
@app.route('/api/birds_list', methods=['GET'])
def make_bird_list():
    result = list(db.birds.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'birds': result})


@app.route('/api/gus_list', methods=['GET'])
def make_gu_list():
    result = list(db.gu_parks.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'gus': result})


@app.route('/api/park_list', methods=['GET'])
def make_park_list():
    gu_receive = request.args.get('gu_give')
    result = list(db.gu_parks.find({'gu': gu_receive}, {'_id': 0}))
    return jsonify({'result': 'success', 'gus': result})


@app.route('/api/posting', methods=['POST'])
def make_post():
    url_receive = request.form['url_give']
    gu_receive = request.form['gu_give']
    park_receive = request.form['park_give']
    bird_receive = request.form['bird_give']
    review_receive = request.form['review_give']
    date_receive = request.form['date_give']
    print(url_receive, gu_receive, park_receive, bird_receive, review_receive)
    post = {
        'url': url_receive,
        'gu': gu_receive,
        'park': park_receive,
        'bird': bird_receive,
        'review': review_receive,
        'date': date_receive
    }
    db.posts.insert_one(post)
    return jsonify({'result': 'success', 'msg': '기록완료!'})


### 6. show_a_post
@app.route('/a_post')
def a_post():
    return render_template('show_a_post.html')


#######################################################
@app.route('/map')
def test_map():
    return render_template('test_map.html')


### xy 좌표
@app.route('/api/gu_xy', methods=['GET'])
def gu_xy():
    gu_receive = request.args.get('gu_give')
    result = list(db.gu_xy.find({'gu': gu_receive}, {'_id': 0}))
    return jsonify({'result': 'success', 'xy': result})


@app.route('/api/park_xy', methods=['GET'])
def park_xy():
    park_receive = request.args.get('park_give')
    result = list(db.park_xy.find({'park': park_receive}, {'_id': 0}))
    return jsonify({'result': 'success', 'xy': result})


### 실시간 날씨정보

@app.route('/api/weather', methods=['GET'])
def get_weather():
    for item in data:
        weather = item.find_all('wfkor')
        today_now = str(weather[-1].text)
        return today_now

now_list = []
now_weather = get_weather()
now_list.append(now_weather)
def give_weather():
    for now in now_list:
        return jsonify({'result': 'success', 'today_now': now})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
