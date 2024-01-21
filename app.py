from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    resp = {}
    resp['message'] = 'Hello, World!'
    return resp

if __name__ == '__main__':
    app.debug = True
    app.run()
