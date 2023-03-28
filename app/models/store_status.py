from app import db
from app.constants import DATETIME_FORMAT, FALL_BACK_DATETIME_FORMAT

from datetime import datetime

class StoreStatus(db.Model):
    __tablename__ = "store_status"
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.String(64), nullable=False)
    timestamp_utc = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Boolean, nullable=False)

    def __init__(self, store_id, status, timestamp_utc):
        self.store_id = store_id
        self.status = True if status.lower() == 'active' else False 
        try:
            ts = datetime.strptime(timestamp_utc, DATETIME_FORMAT)
        except:
            try:
                ts = datetime.strptime(timestamp_utc, FALL_BACK_DATETIME_FORMAT)
            except:
                raise Exception('Given timestampes are not consistent')
        self.timestamp_utc = ts

    def to_dict(self, ):
        return {
            'store_id': self.store_id,
            'timestamp_utc': self.timestamp_utc,
            'status': self.status
        }
    
    def __repr__(self, ):
        return f'< id: {self.store_id} | ts: {self.timestamp_utc} | status: {self.status}'
