from flask import Blueprint, jsonify, request, current_app
from datetime import datetime
from app.models.report import Report
from app import db
from app.tasks.generate_report import generate_report_task
import random
import logging
import string

logger = logging.getLogger(__name__)
trigger_report = Blueprint('trigger_report', __name__)

@trigger_report.route('/trigger_report', methods=['GET'])
def generate_report():
    try:
        report_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

        report = Report(report_id, "PROCESSING")
        db.session.add(report)
        db.session.commit()

        generate_report_task.delay(report_id)
        return jsonify({'status': 'success', 'message': f'Report {report_id} is getting generated... '})
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)})