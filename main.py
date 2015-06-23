from flask import Flask, send_file

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    # send static file instad of template rendering
    # since the architecture of app is SPA.
    return send_file('./templates/index.html')


