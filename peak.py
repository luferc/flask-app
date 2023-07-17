
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    frameworks = ['Flask', 'Django', 'Laravel']
    return render_template('index.html', framework=frameworks)

@app.route('/framework/<frw>')
def framework(frw):
    return "This is " + str(frw)

if __name__== "__main__":
    app.run(host="0.0.0.0", port=5000)
