from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<body style="background-color:LightBlue;"> <p style="color:blue; font-size:30px"> This is the Blue App </p> </body>'

app.run(host='0.0.0.0', port=80)

