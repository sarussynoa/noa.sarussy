from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/contacts-list', methods=['GET'])
def contact_list():
    return render_template('contacts-list.html')


@app.route('/assignment8', methods=['GET'])
def assignment8():
    return render_template('template.html', title='Hobbies')


if __name__ == '__main__':
    app.run('localhost', '5555', debug=True)
