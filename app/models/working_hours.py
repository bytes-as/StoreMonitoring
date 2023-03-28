from app import db
from app.constants import TIME_FORMAT

from datetime import datetime

class WorkingHours(db.Model):
    __tablename__ = "working_hours"
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.String(64), nullable=False)
    day = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.Time, nullable=True)
    end_time = db.Column(db.Time, nullable=True)

    def __init__(self, storeId, day, startTime, endTime):
        self.store_id = storeId
        self.day = day
        self.start_time = datetime.strptime(startTime, TIME_FORMAT).time()
        self.end_time = datetime.strptime(endTime, TIME_FORMAT).time()

    def to_dict(self, ):
        return {
            'store_id': self.store_id,
            'day': self.day,
            'start_time': self.start_time,
            'end_time': self.end_time
        }
    
    def __repr__(self, ):
        return f'< id: {self.store_id} | day: {self.day} | start_time: {self.start_time} | end_time: {self.end_time}>'
