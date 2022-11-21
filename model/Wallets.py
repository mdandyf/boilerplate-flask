from core.database import db 

class Wallets(db.Model):
    __tablename__ = 'wallets'
    id = db.Column('id', db.BigInteger, primary_key = True)
    name = db.Column(db.String(200))

    def __init__(self, name):
        self.name = name

    def get():
        return Wallets.query.all()

    def fetch(data_id):
        return Wallets.query.filter_by(id=data_id).first()

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            flash('Record was successfully added')
            return True
        except:
            flash('An error occured while adding data')
            return False
    
    def update(self, data):
        try:
            for key, item in data.items():
                setattr(self, key, item)
            db.session.commit()
            flash('Record was successfully altered')
            return True
        except:
            flash('An error occured while altering data')
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            flash('Record was successfully deleted')
            return True
        except:
            flash('An error occured while deleting data')
            return False

    def __repr(self):
        return '<id {}>'.format(self.id)