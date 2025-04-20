"""Flaskの実行"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return "top"


@app.route('/hello')
@app.route('/hello/<username>')
def hello_world2(username=None):
    return render_template('hello.html', username=username)


def main():
    app.debug = True
    app.run()


if __name__ == '__main__':
    main()
