from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    resp = {}
    resp['message'] = 'Hello, World!'
    return resp

@app.route('/html/')
def hello_world(user=None):
    user = user or 'Ahmad'
    return '''
<html>
    <head>
        <title>Flask Framework Cookbook</title>
    </head>
    <body>
        <h1>Hello %s!</h1>
        <p>Welcome to the world of Flask!</p>
    </body>
</html>''' % user

if __name__ == '__main__':
    app.debug = True
    app.run()
