from app import db


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

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'c1_red': self.c1_red,
            'c1_green': self.c1_green,
            'c1_blue': self.c1_blue,
            'c2_red': self.c2_red,
            'c2_green': self.c2_green,
            'c2_blue': self.c2_blue,
            'distinct': self.distinct
        }
