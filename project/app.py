from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/gu')
def select_gu():
    return render_template('select_gu.html')


@app.route('/gu/park')
def show_park():
    return render_template('show_park.html')


@app.route('/all')
def show_all_post():
    return render_template('show_all_post.html')


## API 역할을 하는 부분
@app.route('/gu', methods=['GET'])
def show_gu_park():
    gu_receive = request.args.get('gu_give')
    print(gu_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
