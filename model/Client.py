import datetime
from marshmallow import fields, Schema
from core.database import db

class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    client_id = db.Column(db.String(255), nullable=False)
    client_secret = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, data):
        self.name = data.get('name')
        self.client_id = data.get('client_id')
        self.client_secret = data.get('client_secret')
        self.user_id = data.get('user_id')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Client.query.all()

    @staticmethod
    def get_by_id(id):
        return Client.query.filter_by(client_id=id).first()
    
    @staticmethod
    def get_by_user_id(user_id):
        return Client.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_by_auth(client_id, client_secret):
        return Client.query.filter_by(client_id=client_id, client_secret=client_secret).first()

    def __repr(self):
        return '<id {}>'.format(self.id)
