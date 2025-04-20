"""Flaskの実行"""

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return "top"


@app.route('/hello')
@app.route('/hello/<username>')
def hello_world2(username=None):
    return "hello world! {}".format(username)


def main():
    app.debug = True
    app.run()


if __name__ == '__main__':
    main()
