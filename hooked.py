import sys
import logging
from flask import Flask
from flask import request, jsonify

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.INFO)


@app.route("/", methods=['POST', 'GET'])
def hooked():
    error = None
    if request.method == 'POST':
        app.logger.info(request.data)
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(port=5001, threaded=True, host=('0.0.0.0'))
