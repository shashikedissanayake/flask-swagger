from flask import Flask, request, jsonify, render_template

# Press the green button in the gutter to run the script.
app = Flask(__name__)


@app.route('/health_check', methods=['GET'])
def get_request():
    return jsonify({'code': 200, 'message': 'Success'}), 200


@app.route('/test', methods=['GET'])
def test_request():
    return jsonify({'code': 200, 'message': 'Test success'}), 200


@app.route('/api/docs')
def get_docs():
    print('sending docs')
    return render_template('swaggerui.html')


app.run(use_reloader=True, debug=False)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
