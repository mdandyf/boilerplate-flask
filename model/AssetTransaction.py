from core.database import db 

class AssetTransaction(db.Model):
    __tablename__ = 'asset_transaction'
    id = db.Column('id', db.BigInteger, primary_key = True)
    src_wallet_id = db.Column(db.BigInteger)
    src_asset_id = db.Column(db.BigInteger)
    dest_wallet_id = db.Column(db.BigInteger)
    dest_asset_id = db.Column(db.BigInteger)
    amount = db.Column(db.Numeric(16,8))
    gas_fee = db.Column(db.Numeric(16,8))
    total = db.Column(db.Numeric(16,8))

    def __init__(self, src_wallet_id, src_asset_id, dest_wallet_id, dest_asset_id, amount, gas_fee, total):
        self.src_wallet_id = src_wallet_id
        self.src_asset_id = src_asset_id
        self.dest_wallet_id = dest_wallet_id
        self.dest_asset_id = dest_asset_id
        self.amount = amount
        self.gas_fee = gas_fee
        self.total = total

    def get():
        return AssetTransaction.query.all()

    def fetch(data_id):
        return AssetTransaction.query.filter_by(id=data_id).first()

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