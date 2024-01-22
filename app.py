from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text


app = Flask(__name__)
# engine = create_engine("postgresql://postgres:55555555@127.0.0.1/km-test", echo=True)
# con = engine.connect()
# res = con.execute(text("SELECT * FROM cards"))
# for row in res:
#     print(row)
#     print(type(row))

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:55555555@127.0.0.1/km-test'
db = SQLAlchemy(app)
with app.app_context():
    res = db.session.execute(text("SELECT * FROM cards"))
    for row in res:
        print(row)
        print(type(row))




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
