from flask import url_for
from flask import Flask
from flask import render_template


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
@app.route('/users/')
@app.route('/users/<username>/')

def profile(username = 'Silva'):
    return 'User {}'.format(username)

@app.route('/url/')
def show_url():
    return url_for('profile', username='Pylady')


@app.route('/hello/')
@app.route('/hello/<name>/')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == "__main__":
    app.run()
