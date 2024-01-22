from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    resp = {}
    resp['It'] = 'Works!'
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

@app.route('/template/')
def template():
    user = request.args.get('user', 'Ahmad')
    return render_template('index.html', user=user)

if __name__ == '__main__':
    app.debug = True
    app.run()
