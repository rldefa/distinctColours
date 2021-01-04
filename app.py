from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost/data"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template('index.html')


class DataModel(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    c1_red = db.Column(db.Integer())
    c1_green = db.Column(db.Integer())
    c1_blue = db.Column(db.Integer())
    c2_red = db.Column(db.Integer())
    c2_green = db.Column(db.Integer())
    c2_blue = db.Column(db.Integer())
    distinct = db.Column(db.Boolean())

    def __init__(self, c1_red, c1_green, c1_blue, c2_red, c2_green, c2_blue, distinct):
        self.c1_red = c1_red
        self.c1_green = c1_green
        self.c1_blue = c1_blue
        self.c2_red = c2_red
        self.c2_green = c2_green
        self.c2_blue = c2_blue
        self.distinct = distinct


@app.route('/yeet', methods=['POST', 'GET'])
def handle_data():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            data = json.loads(data)
            entry = DataModel(
                c1_red=data['c1_red'],
                c1_green=data['c1_green'],
                c1_blue=data['c1_blue'],
                c2_red=data['c2_red'],
                c2_green=data['c2_green'],
                c2_blue=data['c2_blue'],
                distinct=data['distinct'])
            db.session.add(entry)
            db.session.commit()
            return {"message": "data collected"}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':

        entries = DataModel.query.all()
        results = [
            {
                "c1_red": entry.c1_red,
                "c1_green": entry.c1_green,
                "c1_blue": entry.c1_blue,
                "c2_red": entry.c2_red,
                "c2_green": entry.c2_green,
                "c2_blue": entry.c2_blue,
                "distinct": entry.distinct
            } for entry in entries]

        return {"count": len(results), "collected": results}


if __name__ == '__main__':
    app.run()
