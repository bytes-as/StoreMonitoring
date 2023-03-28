from app import db

class StoreTimezone(db.Model):
    __tablename__ = "store_timezone"
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.String(64), nullable=False)
    timezone_str = db.Column(db.String(64), nullable=True)

    def __init__(self, storeId, ts):
        self.store_id = storeId
        self.timestamp_str = ts

    def to_dict(self):
        return {
            'store_id': self.store_id,
            'timezone_str': self.timezone_str
        }

    def __repr__(self) -> str:
        return f'<store_id: {self.store_id} | timezone_str: {self.timezone_str}>'
