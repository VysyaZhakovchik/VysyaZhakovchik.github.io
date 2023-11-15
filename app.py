#wsk - wsl
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# db_name = 'database.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db = SQLAlchemy(app)

@app.route('/')
def page_home():
    return render_template('home.html')

@app.route('/personazhi')
def page_personazhi():
    return render_template('personazhi.html')

@app.route('/flour')
def page_flour():
    return render_template('flour.html')

@app.route('/apple')
def page_apple():
    return render_template('apple.html')

if __name__ == '__main__':
    app.run(debug=True)
