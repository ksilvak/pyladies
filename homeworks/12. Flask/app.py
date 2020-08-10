from flask import Flask
from flask import url_for
from flask import render_template
import json

app = Flask(__name__)
app.config['DEBUG'] = True


json_string = """ {
    "name": "Silva",
    "town": "Brno",
    "language": "Javascript"
}
"""

data = json.loads(json_string)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/user/')
@app.route('/user/<name>/')
def user_name(name=data['name']):
    return render_template('index.html', name=name)

@app.route('/language/')
@app.route('/language/<language>/')
def user_language(language=data['language']):
    return render_template('index.html', language=language)

@app.route('/town/')
@app.route('/town/<town>/')
def user_town(town=data['town']):
    return render_template('index.html', town=town)

if __name__ == "__main__":
    app.run()