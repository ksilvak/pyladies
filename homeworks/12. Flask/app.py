import json 
from flask import url_for
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['DEBUG'] = True

filename = 'data.txt'
dict1 = {} 
  
with open(filename) as fh: 
    for line in fh: 
        command, description = line.strip().split(None, 1) 
  
        dict1[command] = description.strip() 


out_file = open("data.json", "w") 
json.dump(dict1, out_file, indent = 4, sort_keys = False) 
out_file.close() 


string_json= json.dumps(dict1) 

print(string_json)

@app.route('/')
@app.route('/users/')
@app.route('/users/<username>/')
def profile(username = 'Silva'):
    return 'Jmenuji se {}'.format(username)

@app.route('/hello/')
@app.route('/hello/<name>/')
def hello(name=None):
    return render_template('index.html', name=name)

    
if __name__ == "__main__":
    app.run()
