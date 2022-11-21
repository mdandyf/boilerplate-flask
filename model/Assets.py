from core.database import db 

class Assets(db.Model):
    __tablename__ = 'assets'
    id = db.Column('id', db.BigInteger, primary_key = True)
    wallet_id = db.Column(db.BigInteger)
    name = db.Column(db.String(255))
    symbol = db.Column(db.String(100))
    network = db.Column(db.String(100))
    address = db.Column(db.String(42))
    balance = db.Column(db.Numeric(16,8))

    def __init__(self, wallet_id, name, symbol, network, address, balance):
        self.wallet_id = wallet_id
        self.name = name
        self.symbol = symbol
        self.network = network
        self.address = address
        self.balance = balance

    def get():
        return Assets.query.all()

    def fetch(data_id):
        return Assets.query.filter_by(id=data_id).first()

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