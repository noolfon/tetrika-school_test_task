from flask import Flask

from task3 import appearance

app = Flask(__name__)


@app.route('/api')
def hello_world():
    result = appearance({
        'lesson': [1594663200, 1594666800],
        'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
        'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
    })
    return f'Общее время присутствия ученика и учителя на уроке (в секундах) - {result}c'


if __name__ == '__main__':
    app.run()
