import flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<body style="background-color:#d6ffcb;"> <p style="color:green; font-size:30px"> This is the Green App </p> </body>'

app.run(host='0.0.0.0', port=80)

