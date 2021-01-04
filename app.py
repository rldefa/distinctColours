
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import DataModel

@app.route('/')
def index():
    return render_template('index.html')


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
