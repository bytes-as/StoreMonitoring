from app import db
from app.constants import DATETIME_FORMAT, FALL_BACK_DATETIME_FORMAT

from datetime import datetime

class Report(db.Model):
    __tablename__ = "report"
    report_id = db.Column(db.String(128), primary_key=True)
    report_name = db.Column(db.String(64), nullable=True)
    report_status = db.Column(db.String(15), nullable=True)
    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)
    file_path = db.Column(db.String(256), nullable=True)

    # def __init__(self, report_id, report_name, report_status):
    #     self.report_id = report_id
    #     self.report_name = report_name
    #     self.report_status = report_status

    def __init__(self, report_id, report_status):
        self.report_id = report_id
        self.report_status = report_status

    # def __init__(self, report_status):
    #     self.report_status = report_status        

    def to_dict(self, ):
        return {
            'report_id': self.report_id,
            'report_name': self.report_name,
            'report_status': self.report_status,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'file_path': self.file_path
        }
    
    def __repr__(self, ):
        return f'<report_id: {self.report_id} | report_name: {self.report_name} | report_status: {self.report_status} | start_time: {self.start_time} | end_time: {self.end_time} | file_path: {self.file_path}>'