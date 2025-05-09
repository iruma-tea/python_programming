"""Flaskの実行"""

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hello, world!"


def main():
    app.debug = True
    app.run()


if __name__ == '__main__':
    main()
