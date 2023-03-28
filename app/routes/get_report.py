import os
from flask import Blueprint, jsonify, send_file

from app.models.report import Report

get_report = Blueprint('get_report', __name__)

@get_report.route('/get_report/<report_id>', methods=['GET'])
def fetch_report(report_id):
    report = Report.query.filter_by(report_id=report_id).first()

    if report is None:
        return jsonify({'status': f'Report {report_id} Not Found, most likely was never requested'}), 404

    if report.status == 'STARTED':
        return jsonify({'status': 'Report is being generated'}), 202

    if report.status == 'COMPLETED' and report.file_path is None:
        return jsonify({'status': 'Report could not be generated'}), 500

    if not os.path.exists(report.filepath):
        return jsonify({'status': 'Report file not found'}), 500

    # send the file as response
    return send_file(report.file_path, as_attachment=True, attachment_filename=f'report_{report_id}.csv')