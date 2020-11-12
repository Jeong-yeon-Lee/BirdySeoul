from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.myproject

@app.route('/')
def home():
    return render_template('show_all_post.html')



@app.route('/gus', methods=['GET'])
def make_options():
    result = list(db.gu_parks.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'gus': result})

@app.route('/posts', methods=['GET'])
def show_posts():
    result = list(db.posts.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'posts':result})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)