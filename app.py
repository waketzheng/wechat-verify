#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)


@app.route('/MP_verify_<identifier>.txt')
@app.route('/<path:pre_path>/MP_verify_<identifier>.txt')
def response_identifier(identifier, pre_path=''):
    return identifier

if __name__ == '__main__':
    app.run(port=10240)
